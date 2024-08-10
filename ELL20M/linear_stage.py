############################
# Author: Ashutosh Singh
# Date: 10th Aug 2024
# Desc: Control linear stage ELL20/M
#       Written on Ubuntu 22.xx 
#       Port tied to hardware address
# Requirements: https://github.com/roesel/elliptec

import elliptec
import numpy as np
import serial.tools.list_ports

another_list = serial.tools.list_ports.grep("VID:PID=0403:6015", 'hwid')
connected2=[]
for element in another_list:
    connected2.append(element.device)
print("Linear stage at: ", connected2)
controller = elliptec.Controller(connected2[0])
ls = elliptec.Linear(controller)
# Home the linear stage before usage
ls.home()
x = np.linspace(0,10,11)
# Loop over a list of positions and measure gain for each
for distance in x:
  ls.set_distance(distance)
  # ... measure gain
