"""番茄小说,安卓需要替换so
IOS抓邀请好友页面
低保大约1r/d
变量名称fqxs  -> url#cookie#argus#ladon@ <-多账号
            fqxsua -> 随便编一个ua
            
使用前填入用户名和key
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
    so_filename = f"fqxs_{system}_{machine_type}_{python_version}.{file_ext}"
    os.system(f'cp ./{so_filename} ./fqxs.{file_ext}')
    return so_filename


print(load_so_file())
from fqxs import *

check(name, key)
