import numpy as np
from sgp4.api import Satrec
from tools.date_trans import calculate_jday
from datetime import datetime
from tools.sgp4 import *



class ObjSatDetail:
    def __init__(self, objNum):
        self.satobj = [dict() for _ in range(objNum)]
        self.objpnow = np.zeros((objNum, 3))
        self.objvnow = np.zeros((objNum, 3))
        self.CurrentOr = np.zeros((objNum, 3))
        self.CurrentOt = np.zeros((objNum, 3))
        self.CurrentOh = np.zeros((objNum, 3))

the code is coming soon
94712
38027
11946