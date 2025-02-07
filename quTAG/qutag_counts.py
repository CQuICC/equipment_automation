"""
Short Desc: Fetches counts per exposure time from quTAG and prints it.

Ensure that the DLL path is correct in QuTAG.py


"""






from datetime import datetime
try:
        import QuTAG
except:
        print("Time Tagger wrapper QuTAG.py is not in the search path.")


qutag = QuTAG.QuTAG()
timebase = qutag.getTimebase()
print("Device timebase:", timebase, "s")

qutag.enableChannels((1,2)) # Enables channel 1,2
qutag.setSignalConditioning(1,qutag.SCOND_MISC,True,0.8)    # Set Channel Parameters
qutag.setSignalConditioning(2,qutag.SCOND_MISC,True,0.8)    # Set Channel Parameters
time.sleep(1)
print("Signal Cond. 1: ", qutag.getSignalConditioning(1))
print("Signal Cond. 2: ", qutag.getSignalConditioning(2))

##########################################################################################

# rc = qutag.startCalibration()
# # wait a little to get the device started calibrating
# time.sleep(1)
# calibState = qutag.getCalibrationState()
# print("getCalibrationState", calibState)
# while calibState:
# 	time.sleep(0.1)
# 	calibState = qutag.getCalibrationState()
# 	# print("getCalibrationState: ", calibState)
# print("CalibrationState done:", calibState)
#############################################################################################

dataloss = qutag.getDataLost()
print("dataloss: " + str(dataloss))
qutag.setExposureTime(1000) # 1s Counting
time.sleep(1)
data,updates = qutag.getCoincCounters()
print(data)
qutag.deInitialize()