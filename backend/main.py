import numpy as np
import datetime
from scipy.io import loadmat
from download_TLEs_data import download_tle
from setup_TLEfiles import *
from crash_analysis_prepare import *
from Propgation_analysis import *
from dataestr import *
from tools.date_trans import *
from tools.common_tools import *
#initialize
ConjStartDate = datetime.datetime(2025, 4, 7, 0, 0, 0)
ConjEndDate = datetime.datetime(2025, 4, 8, 0, 0, 0)
ConjStartJulian = date_to_julian(ConjStartDate)
ConjEndJulian = date_to_julian(ConjEndDate)



the code is coming soon
30838
98504
40014