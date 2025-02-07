"""
Short Desc: Control DC power Supply
##############################################################################################
Description: Python script to control scientific Programmable DC power supply (PSD7303B)
Current implementation uses USB to connect to the device. Network implementation
was avoided as the network might have multiple devices plugged in. 
##############################################################################################
Device uses SCPI command sequence. It is readily available in the datasheet
It requires a delay of about 20ms between successive commands. Query_delay is set
with the the module, however, read/write don't have a delay parameter, hence they
are put in manually. 
The commands are NOT case sensitive.
##############################################################################################
Features: 
read/write current, read/write voltage, turn on/off channel
##############################################################################################
Install pyvisa module
"""

import pyvisa                      ##install NI visa
import time
def delay():
    time.sleep(0.02)
rm=pyvisa.ResourceManager()
print(rm.list_resources())         ## list of all NI instruments connected to the PC 


# my_instrument = rm.open_resource("USB0::0x0483::0x7540::SPD3XIDD5R6197::INSTR")
my_instrument = rm.open_resource("USB0::0xF4EC::0x1430::SPD3XKGX803123::INSTR")
my_instrument.write_termination = "\n"                                  # setting character termination
my_instrument.read_termination = "\n"   
my_instrument.query_delay=0.02

my_instrument.write('CH1:curr 0.1')                 #Force the current to be 100mA
my_instrument.write('CH2:curr 0.1')                 #Force the current to be 100mA



def set_voltage_ch1(voltage :float) -> float:
    if not isinstance(voltage, float):
        raise TypeError("Voltage not float type")
    command = "CH1:VOLT "+f"{voltage:.2f}"
    print(command)
    my_instrument.write(command)
    delay() 


def set_voltage_ch2(voltage):
    if not isinstance(voltage, float):
        raise TypeError("Voltage not float type")
    command = "CH2:VOLT "+f"{voltage:.2f}"
    print(command)
    my_instrument.write(command) 
    delay()

def set_current_ch1(current :float) -> float:
    if not isinstance(current, float):
        raise TypeError("Current not float type")
    command = "CH1:CURR "+f"{current:.2f}"
    print(command)
    my_instrument.write(command)
    delay() 

def set_current_ch2(current):
    if not isinstance(current, float):
        raise TypeError("Current not float type")
    command = "CH2:CURR "+f"{current:.2f}"
    print(command)
    my_instrument.write(command) 
    delay()

def get_voltage_ch1():
    " This returns the set voltage on CH1"
    return my_instrument.query('CH1:VOLT?')

def get_voltage_ch2():
    " This returns the set voltage on CH1"
    return my_instrument.query('CH2:VOLT?')

def get_current_ch1():
    " This returns the set current on CH1"
    return my_instrument.query('CH1:CURR?')

def get_voltage_ch2():
    " This returns the set voltage on CH1"
    return my_instrument.query('CH2:CURR?')

def set_status_ch1(status: bool) -> bool:
    " This sets the channel status CH1: True = ON, False = Off"
    if not isinstance(status, bool):
           raise TypeError("Input not bool type")
    if status==True:
        my_instrument.write('OUTP CH1,ON')
    else:
        my_instrument.write('OUTP CH1,OFF')
    delay()

def set_status_ch2(status: bool) -> bool:
    " This sets the channel status CH2: True = ON, False = Off"
    if not isinstance(status, bool):
        raise TypeError("Input not bool type")
    if status==True:
        my_instrument.write('OUTP CH2,ON')
    else:
        my_instrument.write('OUTP CH2,OFF')
    delay()

def disconnect_power_supply(status: bool = True) -> bool:
    " This sets the channel status CH2: True = ON, False = Off"
    if not isinstance(status, bool):
           raise TypeError("Input not bool type")
    if status==True:
        my_instrument.close()
    else:
        print("Why have you written False as Arg")
    delay()