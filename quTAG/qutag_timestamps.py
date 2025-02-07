"""
Short Desc: Fetches timestamp from quTAG and writes it in a file.

Ensure that the DLL path is correct in QuTAG.py


"""






from datetime import datetime

try:
    import QuTAG
except:
    print("Time tagger wrapper is not in the search directory")



qutag=QuTAG.QuTAG()
qutag.enableChannels((1,2))
qutag.setSignalConditioning(1,qutag.SCOND_MISC,True,0.3)    # Set Channel Parameters
qutag.setSignalConditioning(2,qutag.SCOND_MISC,True,0.3)    # Set Channel Parameters

time.sleep(1)
print("Signal Cond. 1: ", qutag.getSignalConditioning(1))
print("Signal Cond. 2: ", qutag.getSignalConditioning(2))

# ########################################################################################

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
# ###########################################################################################

dataloss = qutag.getDataLost()
print("dataloss: " + str(dataloss))

filename = "data/"+datetime.now().strftime("%Y_%m_%d-%H_%M_%S_")
qutag.writeTimestamps(filename+"_"+str(rf_delay)+"_"+"PM1_ts.txt",qutag.FILEFORMAT_ASCII)
    time.sleep(1) # 1 second sleep time
    qutag.writeTimestamps('',qutag.FILEFORMAT_NONE)
qutag.deInitialize()