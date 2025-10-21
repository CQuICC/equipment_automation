## Equipments
* RTM3000:
  - Captures the waveform from Rohde & Schwarz RTM3004 oscilloscope and plots it on a PC. The data points are also written in a text file for post procesing (if necessary).
  - Changes to FFT mode, and collected the magnitude on the spectrum for a set frequency using cursor. 
* MXO4:
  - Controls the Rohde & Schwarz MXO4 oscilloscope over LAN using the RsInstrument library.
  - Enables FFT mode and measures amplitude at multiple frequency points between 10 MHz and 100 MHz.
  - Saves the measured amplitude data into a timestamped CSV file for analysis or post-processing.
* PSD7303B: Controls the programmable DC power supply. 
* MPC320: Control the paddle position of the motorised molarisation controller from Thorlabs.
* ELL20/M: Thorlabs Linear Stage. Travel Distance 60mm. 
* NRT-8000: An optical spectrum analyser from New Ridge Technologies. 
* quTAG:
  - Fetches timestamps from quTAG and writes it in a file
  - Fetches counts per exposure time and prints it
