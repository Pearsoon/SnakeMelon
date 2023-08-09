"""
今日头条(注意不是极速版)
by Pearson
搜索 done/excitation_ad/ 抓该接口的url(...done/excitation_ad/?后的url)、cookie 、argus、ladon
cookies格式 jrtt = "url#cookie#argus#ladon#ua" 多账号@
小卖铺 http://www.pearsons.live/ 将收到的卡密
    name              key              账号限制         到期时间
{'Pearson': {'key': 'abcd123', 'chance': 3, 'data': '20230830'}
填到name = "Pearson"   key = "abcd123"

注意⚠ arm用户请用Debian版青龙
docker run -dit \
   -v $PWD/ql/data:/ql/data \
   -p 5600:5700 \
   --name qinglongdebian \
   --hostname qinglong \
   --restart always \
   whyour/qinglong:debian

"""
import platform
import os

name = ""
key = ""
githubProxy = "https://pears0n.xyz/"  # GitHub加速站


def load_so_file(filename):
    files = os.listdir()
    system = platform.system().lower()
    if system == 'windows':
        file_ext = 'pyd'
    else:
        file_ext = 'so'
    if f"{filename}.{file_ext}" not in files:
        machine_type = platform.machine().replace('aarch64', 'arm').replace('x86_64', 'amd').replace('AMD64', 'amd')
        python_version = f"py{platform.python_version_tuple()[0]}{platform.python_version_tuple()[1]}"
        so_filename = f"{filename}_{system}_{machine_type}_{python_version}.{file_ext}"
        os.system(f'cp ./{so_filename} ./{filename}.{file_ext}')
        os.system(
            f'curl -LjO {githubProxy}https://raw.githubusercontent.com/Pears0nLee/SnakeMelon/master/{filename.upper()}/{so_filename}')

        os.system(f'cp ./{so_filename} ./{filename}.{file_ext}')

        return so_filename

load_so_file("fqxs")

from fqxs import *

authorization(name, key)
