"""悟空浏览器轮子版
by Pearson
https://github.com/Pears0nLee/SnakeMelon
bug提交https://t.me/+T8ozejX9rnkwZDE1
低保大约1r/d
变量名称wkllqs  -> url#cookie#argus#ladon@ <-多账号
            wkua -> 随便编一个ua
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
    so_filename = f"wk_{system}_{machine_type}_{python_version}.{file_ext}"
    os.system(f'cp ./{so_filename} ./wk.{file_ext}')
    return so_filename


print(load_so_file())
from wk import *

stat()
