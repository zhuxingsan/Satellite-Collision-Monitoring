import numpy as np
from datetime import datetime
from sgp4.api import jday

def load_maneuver_data(fmaneverdata, ObjSat):
    """
    从推进数据文件中读取和加载推进数据
    """
    objNum = len(ObjSat)
    TotalManeuverData = 0
    PropStartjday = np.zeros(objNum)
    PropEndjday = np.zeros(objNum)
    pcovoffset = np.zeros((objNum, 6))
    ManeuverDuration = np.zeros(objNum)
    objmaxfuel = np.zeros(objNum)
    objdrymass = np.zeros(objNum)
    ae = np.zeros(objNum)
    cd = np.zeros(objNum)
    satmass = np.zeros(objNum)
    PropMethod = np.zeros(objNum)
    PropVsign = np.zeros(objNum)
    isSwitch = np.zeros(objNum)
    
    pressureprofile = [None] * objNum
    thrustprofile = [None] * objNum
    ispprofile = [None] * objNum



the code is coming soon
30591
29678
62174