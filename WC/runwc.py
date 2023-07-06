"""
望潮 by Pearson
仅供学习使用
抓包练习  登录接口整个url,ua
wangchao = "url?ua@"
"""
import platform
import os


def load_so_file():
    system = platform.system().lower()
    if system == 'windows':
        file_ext = 'pyd'
    else:
        file_ext = 'so'
    machine_type = platform.machine().replace('aarch64', 'arm').replace('x86_64', 'amd').replace('AMD64', 'amd')
    python_version = f"py{platform.python_version_tuple()[0]}{platform.python_version_tuple()[1]}"
    so_filename = f"wc_{system}_{machine_type}_{python_version}.{file_ext}"
    os.system(f'cp ./{so_filename} ./wc.{file_ext}')
    return so_filename


print(load_so_file())
from wc import *

start()