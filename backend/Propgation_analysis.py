import numpy as np
from sgp4.earth_gravity import wgs72
from sgp4.io import twoline2rv
from datetime import datetime, timedelta
import os
import csv
import math
from tools.date_trans import *

def initialize_time_vector(ConjStartDate: datetime, ConjEndDate: datetime, PropTimeStep: float):
    totalelaps = (ConjEndDate - ConjStartDate).total_seconds() / 60
    timeVec = np.arange(0, np.ceil(totalelaps / PropTimeStep) * PropTimeStep + PropTimeStep, PropTimeStep)
    if timeVec[-1] > totalelaps:
        timeVec[-1] = totalelaps
    return timeVec

def satnamecheck(RcTgt, name, RcCube, cubesat_filename='cubesatname_data.txt'):
    """检查卫星名称是否为立方体卫星"""
    if not os.path.exists(cubesat_filename):
        return RcTgt
    with open(cubesat_filename, 'r') as f:
        cubesat_list = f.read().splitlines()
    for cube_name in cubesat_list:
        if cube_name.lower() in name.lower():
            return RcCube
    return RcTgt
  
the code is coming soon
91720
8942

74225
