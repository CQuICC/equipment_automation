"""
Short Desc: Code to control the paddle positions of motorized polarisation controller. 

Description:
The code is forked from archived thorlabs MPC repository with minor chages. The program uses .dll files
generated during the installation of Kinesis software available on ThorLabs website. 
Change the directory in the AddReference("...")

The software uses the serial number to identify the device. Serial number of the MPC available in the lab:
1. 38390134
2. 38388754


"""


import clr
import time

clr.AddReference("D:\\software\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.DeviceManagerCLI.dll")
clr.AddReference("D:\\software\\Thorlabs\\Kinesis\\Thorlabs.MotionControl.GenericMotorCLI.dll")
clr.AddReference("D:\\software\\Thorlabs\\Kinesis\\ThorLabs.MotionControl.PolarizerCLI.dll")

from Thorlabs.MotionControl.DeviceManagerCLI import *
from Thorlabs.MotionControl.GenericMotorCLI import *
from Thorlabs.MotionControl.PolarizerCLI import *
from System import Decimal

def main():
    try:
        # Build device list. 
        DeviceManagerCLI.BuildDeviceList()

        # create new device.
        serial_no = "38390134"
        device = Polarizer.CreatePolarizer(serial_no)

        # Connect to device.
        device.Connect(serial_no)

        # Ensure that the device settings have been initialized.
        if not device.IsSettingsInitialized():
            device.WaitForSettingsInitialized(10000)  # 10 second timeout.
            assert device.IsSettingsInitialized() is True

        # Start polling loop and enable device.
        device.StartPolling(250)  #250ms polling rate.
        time.sleep(5)
        device.EnableDevice()
        time.sleep(0.25)  # Wait for device to enable.

        # Get Device Information and display description.
        device_info = device.GetDeviceInfo()
        print(device_info.Description)

        # Call device methods.
        print("Homing Device")
        paddle1 = PolarizerPaddles.Paddle1#choose first paddle
        device.Home(paddle1,60000)  # 60 second timeout.
        paddle2 = PolarizerPaddles.Paddle2#choose first paddle
        device.Home(paddle2,60000)  # 60 second timeout.
        paddle3 = PolarizerPaddles.Paddle3#choose first paddle
        device.Home(paddle3,60000)  # 60 second timeout.
        print("Done")

        time.sleep(2)

        new_pos = Decimal(10.0)  # Must be a .NET decimal.
        print(f'Moving to {new_pos}')
        device.MoveTo(new_pos,paddle1, 60000)  # 60 second timeout.
        device.MoveTo(new_pos,paddle2, 60000)  # 60 second timeout.
        device.MoveTo(new_pos,paddle3, 60000)  # 60 second timeout.
        print("Done")


        # Stop polling loop and disconnect device before program finishes. 
        device.StopPolling()
        device.Disconnect()


    except Exception as e:
        print(e)
        
    #SimulationManager.Instance.UninitializeSimulations()

if __name__ == "__main__":
    main()



 

