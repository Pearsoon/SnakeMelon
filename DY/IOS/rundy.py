"""抖音极速版
by Pearson
https://github.com/Pears0nLee/SnakeMelon
bug提交https://t.me/+T8ozejX9rnkwZDE1
低保大约1r/d看号
变量名  dyjsb  -> url#cookie#argus#ladon@ <-多账号
            jsbua -> 随便编一个ua
"""
import platform
import os

name = ""
key = ""


def load_so_file():
    system = platform.system().lower()
    if system == 'windows':
        file_ext = 'pyd'
    else:
        file_ext = 'so'
    machine_type = platform.machine().replace('aarch64', 'arm').replace('x86_64', 'amd').replace('AMD64', 'amd')
    python_version = f"py{platform.python_version_tuple()[0]}{platform.python_version_tuple()[1]}"
    so_filename = f"dy_ios_{system}_{machine_type}_{python_version}.{file_ext}"
    os.system(f'cp ./{so_filename} ./dy_ios.{file_ext}')
    return so_filename


print(load_so_file())
from dy_ios import *

check(name, key)
