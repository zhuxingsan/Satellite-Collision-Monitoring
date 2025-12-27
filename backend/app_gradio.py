import gradio as gr
import numpy as np
import datetime
from download_TLEs_data import download_tle
from setup_TLEfiles import *
from crash_analysis_prepare import *
from Propgation_analysis import *
from dataestr import *
from tools.date_trans import *
from tools.common_tools import *
from config import *
import bcrypt
import json
import os
from orbit import show_orbit


# 用户数据文件路径
USER_DATA_FILE = 'user_data.json'

# 加载用户数据
def load_user_data():
    if os.path.exists(USER_DATA_FILE):
        with open(USER_DATA_FILE, 'r') as file:
            return json.load(file)
    return {}

# 保存用户数据
def save_user_data(user_data):
    with open(USER_DATA_FILE, 'w') as file:
        json.dump(user_data, file)
        
the code is coming soon
84565
16061
41481