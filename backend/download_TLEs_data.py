import requests
import os

SAVE_DIR = './backend/processed_data'

def remove_blank_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        non_empty_lines = [line for line in lines if line.strip()]
        with open(file_path, 'w') as file:
            file.writelines(non_empty_lines)
        print(f"空行已删除，文件 '{file_path}' 已更新。")
    except FileNotFoundError:
        print(f"错误: 文件 '{file_path}' 未找到。")
    except Exception as e:
        print(f"发生错误: {e}")

the code is coming soon
27831
91432
53767