from RsInstrument import RsInstrument      # Import R&S instrument control library
import time                                # For timing delays
import csv                                 # For saving data as CSV
import os                                  # For directory operations
import datetime                            # For timestamping filenames

################################################################################
# Oscilloscope Setup (Rohde & Schwarz MXO4)
################################################################################

mxo = RsInstrument('TCPIP::10.21.0.237::INSTR', True, False)   # Connect via LAN (update IP if needed)
mxo.opc_timeout = 10000                                        # Timeout for operation complete (ms)
mxo.instrument_status_checking = True                          # Enable automatic status checking

print(f'Device IDN: {mxo.idn_string}')                         # Print instrument identification string
print(f'Device Options: {",".join(mxo.instrument_options)}\n') # Print installed options

################################################################################
# Spectrum Analyzer (FFT) Configuration
################################################################################

mxo.write("CALCulate:SPECTRum:STATe ON")                       # Turn on FFT/Spectrum mode
mxo.write("CALCulate:SPECTRum:SOURce C1")                      # Use Channel 1 as FFT input
mxo.write("CALCulate:SPECTRum:FREQuency:STARt 1E6")            # Start frequency = 1 MHz
mxo.write("CALCulate:SPECTRum:FREQuency:STOP 100E6")           # Stop frequency = 100 MHz
mxo.write("CALCulate:SPECTRum:FREQuency:WINDow:TYPE FLAT")     # Use flat-top window for accurate amplitude
mxo.write("CALCulate:SPECTRum:MAGNitude:SCALe DBM")            # Display FFT in dBm scale
mxo.write("*WAI")                                               # Wait for operations to complete

################################################################################
# Cursor Setup
################################################################################

mxo.write("CURSor1:STATe ON")                                  # Enable cursor 1
mxo.write("CURSor1:FUNCtion PAIRed")                           # Use paired vertical cursors
mxo.write("CURSor1:SOURce SPECNORM1")                          # Apply cursor to FFT trace

def measure_amplitude(freq_hz):
    """Move cursor to given frequency and return amplitude."""
    mxo.write(f"CURSor1:X1Position {freq_hz}")                 # Set cursor X position
    mxo.write("*WAI")                                          # Wait for update
    amp = float(mxo.query("CURSor1:Y1Position?"))              # Query Y (amplitude) at that frequency
    return amp

################################################################################
# Measurement Loop Configuration
################################################################################

frequencies = [i * 1e6 for i in range(10, 101, 10)]            # Frequencies from 10 MHz to 100 MHz in 10 MHz steps

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")  # Timestamp for this measurement run

folder = f"{timestamp}_scope_data"                             # Output folder name
os.makedirs(folder, exist_ok=True)                              # Create folder if not exists

csv_filename = os.path.join(folder, f"spectrum_results_{timestamp}.csv")  # CSV file path
with open(csv_filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    header = ["Reading#"] + [f"{int(f/1e6)}MHz_dBm" for f in frequencies] # Header row: frequency labels
    writer.writerow(header)                                     # Write header to CSV

################################################################################
# Data Acquisition
################################################################################

num_readings = 50                                               # Number of repeated readings
time_per_reading = 0.1                                            # Delay between readings (seconds)

print(f"\nCollecting {num_readings} readings...\n")

try:
    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        for n in range(1, num_readings + 1):                    # Loop over each reading
            row = [n]                                           # Start row with reading number
            for f in frequencies:
                amp = measure_amplitude(f)                      # Measure amplitude at each frequency
                row.append(amp)                                 # Append result
            writer.writerow([row[0]] + [f"{val:.2f}" for val in row[1:]])  # Write formatted row to CSV
            print(f"Reading {n}: " + ", ".join([f"{val:.2f}" for val in row[1:]]))  # Print to console
            time.sleep(time_per_reading)                        # Wait before next measurement

finally:
    mxo.close()                                                 # Close connection safely
    print("Oscilloscope disconnected.")                         # Notify user
