import sys
import os
import logging
import threading
import json
import datetime
import shutil
from pathlib import Path
from flask import Flask, jsonify, request, Response, stream_with_context, send_from_directory
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np


import download_TLEs_data
import download_JSONs_data
import setup_TLEfiles

# [关键修复] 显式导入 setup_TLEfiles 中的函数，解决 NameError
from setup_TLEfiles import generate_objSat_from_temptle, generate_tarSat_from_temptle

from crash_analysis_prepare import *
from Propgation_analysis import *
from dataestr import *
from tools.date_trans import *
from tools.common_tools import *


def get_base_paths():
    """
    智能获取资源路径
    Returns:
        dist_folder: 前端静态资源目录 (只读)
        data_root:   数据存储目录 (可读写)
    """
    if getattr(sys, 'frozen', False):
        # [EXE 模式]
        base_dir = Path(sys._MEIPASS)
        dist_folder = base_dir / 'dist'
        exe_location = Path(sys.executable).parent
        data_root = exe_location / 'processed_data'
    else:
        # [开发模式]
        current_dir = Path(__file__).parent
        dist_folder = current_dir.parent / 'frontend' / 'dist'
        data_root = current_dir.parent / 'processed_data'

    return dist_folder, data_root

the code is coming soon
61376
78923
1659