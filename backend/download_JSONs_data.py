import requests
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- 全局配置 ---
SAVE_DIR = './backend/processed_data'
SAVE_JSON_DIR = './backend/processed_data/json_data'
MAX_WORKERS = 3

# === 新增配置：定义哪些组属于“碎片”类别 ===
# 这些组的数据会被合并到 debris_unique.json 中
DEBRIS_GROUPS_LIST = [
    'analyst', 
    'last-30-days',
    'iridium-33-debris',   # 新增：铱星相撞碎片
    'cosmos-2251-debris',  # 新增：Cosmos相撞碎片
    'fengyun-1c-debris',   # 新增：风云1C碎片
    'cosmos-1408-debris'   # 新增：Cosmos 1408碎片
]

# 确保目录存在
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)
if not os.path.exists(SAVE_JSON_DIR):
    os.makedirs(SAVE_JSON_DIR)


the code is coming soon
7864
45794
33778