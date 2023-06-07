"""
抖音自用版
by Pearson
开宝箱,宝箱广告,视频广告
6.2 修复签到
增加走路
暂时未写异常处理,bug提交https://t.me/+T8ozejX9rnkwZDE1
"""
import os
import time
import random
import base64
import requests
import json
import threading

# cookies = "_request_from=web&in_sp_time=1&version_code=14.9.0&js_sdk_version=1.95.0.29&tma_jssdk_version=1.95.0.29&app_name=douyin_lite&app_version=14.9.0&vid=E7A9576D-B604-4011-9EF1-828A7747BC85&device_id=2676642195441342&channel=App%20Store&mcc_mnc=313110&aid=2329&screen_width=1284&openudid=b8b3b19e728856a3939f772485c5e6a8f478e139&cdid=BC982C17-E984-4A2B-B8E1-74345D1143ED&os_api=18&ac=WIFI&os_version=16.6&device_platform=iphone&build_number=149005&iid=2764618364881651&device_type=iPhone15,3&idfa=00000000-0000-0000-0000-000000000000#excgd=20230531; passport_csrf_token=d76004c80f3e9671189b2fc6b4c76bea; passport_csrf_token_default=d76004c80f3e9671189b2fc6b4c76bea; d_ticket=e577956cc768c01e0a3e5adebbef9167dc2ef; n_mh=MM6CxTALSDIp_mTzNk8J_5OpevFOoHkgj7l0l5Tb340; odin_tt=7c051c47f2919301eff87d5ff88b9576e716e8a204cf58fc9f054b784edee7143689e6296755a82ef243c69309ab079e8541c42aa308e0569750f5598e4082d76b1537dc49f1229de6cff212bcc76a84; passport_assist_user=Cjz47-uOOejE3faOzK7uT7R_85IxX_K9H0KaoaDhOYDNPWRdLleuPdyd0EKJyT9mnjGNg4bo6UG63pH8ltoaSAo8YEivoW_2A8-QW1bBsWdzqz9Ks7e1-TeFHTx4VepSwneHiwA3y9n4xgfZgEQ231vUwaHSGtbw0kmrg5pkELSGsg0Yia_WVCIBAzlB54A%3D; sessionid=f29527bac2b9230f3916e0237b07dc50; sessionid_ss=f29527bac2b9230f3916e0237b07dc50; sid_guard=f29527bac2b9230f3916e0237b07dc50%7C1684983357%7C5184000%7CMon%2C+24-Jul-2023+02%3A55%3A57+GMT; sid_tt=f29527bac2b9230f3916e0237b07dc50; uid_tt=a232553ca7c7f41e7275e2376a4708d4; uid_tt_ss=a232553ca7c7f41e7275e2376a4708d4; msToken=IeyWiDGAtQRKWg4IfwIXSRsHDbyabSpLKaZrLooXtwoI1AGJWKC-0z2_OhpE9HObv5sPIzR_JTnSQ9OV-s6tXBLM; MONITOR_WEB_ID=2676642195441342; install_id=2764618364881651; ttreq=1$5cf1c5fcc8495b0c3064d5f60f6426c2ea27630d; store-region=cn-fj; store-region-src=uid#1eekX0hyiHDxbbbpYgWi1d9nfE9cuDFnTGxILxzOVA0Wrdil9+Ui2ioxGAtzE+utNK0Jzpmv32i9utNpQa1Xs4kZci7iUvVmeMy/suxzoNk6Wzzc0CcDCFDg2yKiV2fBCVChRKAktHJ01SOMdnU+DVfUVINo/ohBKaknfzzGtQsJ5gWSkAV8lN5lXO2ATpH6XWBf1uR+JEL9oNmYi9gMBkVq3ogD2Z8CBPtAv5TF5kBnfpKa8mmx8EIjpK4iV2A9MME#dlAiWrGVhexpAnA9pnmJ+5QqkoSv0bCQnLlZ2/sfL5XUghad"
# cookies = os.getenv("dyjsb")
cookies = "_request_from=web&in_sp_time=0&version_code=14.9.0&js_sdk_version=1.95.0.29&tma_jssdk_version=1.95.0.29&app_name=douyin_lite&app_version=14.9.0&vid=BB526F35-F75A-4A7F-9789-D2DFD39B153C&device_id=1394618304577160&channel=App%20Store&mcc_mnc=46001&aid=2329&screen_width=1125&openudid=8d793bf200e2a07aae6c9e3e1c9a2dc5bb38ffb3&cdid=AAE20121-B06C-4239-AFBA-02BEC9C643AD&os_api=18&ac=WIFI&os_version=15.6&device_platform=iphone&build_number=149005&iid=4453451106360782&device_type=iPhone11,2&idfa=57ADC867-91F8-4CE9-B9CD-230B4B2F7CC6#excgd=20230516; passport_csrf_token=b38184b8b409e1a1729bd8235c2d8a82; passport_csrf_token_default=b38184b8b409e1a1729bd8235c2d8a82; d_ticket=b41867579a7f2c7b51119d147e8b60976d3d0; n_mh=ngx4nTLueyUCiZv_idyOERZ5MXExBFl1qO_3KQQd_eI; odin_tt=2046295b7b5f02c6e9c650af660554122cc83a8024bb105110060c543efcf7b3a8b4588226462d4fa9c8e6b499a9606292c64ddd8a22409aef0b92152f9c2c14d433039f47860e7893142a6e4d05b731; passport_assist_user=CkHj-OZpZnQ-j5YPyzeHNJbzxLXi6SfkotO8bdJg-w3BftvR_-Golpd9yCvoBEdNRUUD-zczJ1S82uthzNwRr0C5eRpICjysQPH6WP3e31wueAGFYvDff9iqt6of_cJoSohVMpfdm84Dtok-aEj38jq7fWvgGuYyYCUx4ViHqH26ZiIQ6uOuDRiJr9ZUIgEDyktR4A%3D%3D; sessionid=5689d1a50dccd312dea544e1b321b130; sessionid_ss=5689d1a50dccd312dea544e1b321b130; sid_guard=5689d1a50dccd312dea544e1b321b130%7C1684027093%7C5184000%7CThu%2C+13-Jul-2023+01%3A18%3A13+GMT; sid_tt=5689d1a50dccd312dea544e1b321b130; uid_tt=2a3ed22ca3f286e041ca383144886ac9; uid_tt_ss=2a3ed22ca3f286e041ca383144886ac9; msToken=yAuImv7EBmqD7YZ5nZJIvpqVaTbMxICiDzh7N2e46R_QL08zi5mdavVT0C-PKMKW379d6D4XPr5GvG7BTwhEzSHP; MONITOR_WEB_ID=1394618304577160; store-region=cn-sd; store-region-src=uid; install_id=4453451106360782; ttreq=1$db6e2e289f06251f5da9b3dcad18d00a00d6f4e2#8aKZqshN/vbDzeI+IrVDDWG2guVsyNzmmfgMaReNGUXSnQ2dyM9FQe+Njcr4zurKyYxvPEl8H56H5gXFdMOCIAMa4ydUnRpspDFG4oQOqoSQ8p+euCp/infcslKBpSOZtDxJhj2Ph7bbi8ZU+dW3NqHxBKMFE+ydruM2slqW4l65c60j/GhPPcZAIaJ0A5mk7rj/1YAzCnzYCntMwUopFXo2Vs4MiIxBnkYtUEzK3on4h3FYJOWLYSpNsB8Y4YRdhTdEBFnAvxtmwpQA/ZbQzpZd#AssWMGmtwKvoyCAqwWvFqPWm8tVMVrbKmoBmFMCyMyXAd9L1" \
          "@_request_from=web&in_sp_time=0&version_code=14.9.0&js_sdk_version=1.95.0.29&tma_jssdk_version=1.95.0.29&app_name=douyin_lite&app_version=14.9.0&vid=CC7693D3-B89A-42F7-A41E-4823AB6F44A2&device_id=594213450290318&channel=App%20Store&mcc_mnc=46011&aid=2329&screen_width=1125&openudid=0eab48a3dac679248e1007fad26c020d2a4c0739&cdid=BD280BEE-F506-439A-A46C-13D343C51101&os_api=18&ac=WIFI&os_version=16.2&device_platform=iphone&build_number=149005&iid=2148874146810872&device_type=iPhone11,2&idfa=00000000-0000-0000-0000-000000000000#excgd=20230416; d_ticket=636dcba343b7ea06ebdee81744639e4bba879; passport_csrf_token=950977397d4f4e8dd04e75d538628700; passport_csrf_token_default=950977397d4f4e8dd04e75d538628700; n_mh=R-rKNuq_ls3QhUZbr_b03tEtgNaaBwoFBR4EpU3LwXw; sessionid=c26ca4501567b808c37f4e222ec95133; sessionid_ss=c26ca4501567b808c37f4e222ec95133; sid_guard=c26ca4501567b808c37f4e222ec95133%7C1680964546%7C5183999%7CWed%2C+07-Jun-2023+14%3A35%3A45+GMT; sid_tt=c26ca4501567b808c37f4e222ec95133; uid_tt=28fd289f749735aa76fdafd76469198b; uid_tt_ss=28fd289f749735aa76fdafd76469198b; MONITOR_WEB_ID=594213450290318; passport_assist_user=CkGl-WI7faihYz9kExcDZIj8-NbQ5Hi5lackias_BzQRl1kLndxEZNQIVLwLz2nT8C5OrSA1r8GPQSCYDwz_tiwwoBpICjywiPhl60KTnWoVnYye17QTTDW7y6tzaBT6o1G8UoKEE_AGfW1AATQaWJ8LH2kW25bMh_gk7jTA3B4C8rcQ2tSuDRiJr9ZUIgEDLlb58w%3D%3D; odin_tt=38213bcacee5529b5537b5ab7b67a6c10a41b80275c98113e5b67fe83279bcf58d3e9b11d496a743b72c1d2f554a759567446adb025efa1eb8feb0ccc02ffab883e0537600f6a0f43c983d50b9a5f64a; msToken=E7VXrqGau-iMXqSJ64i4uxrTipF4YU_jA8jgWYHtsauEAx2wiRsczMahY3Tryr1DOkzkRLXTMHf02MHiNqyXo3kK2A==; install_id=2148874146810872; ttreq=1$8fb8081418b073714201027ca7a05650a7031b83; store-region=cn-sc; store-region-src=uid#gWCErCpsPJeslOY/mIcmkzB14GNiv3DcjbzYujAufoNwnUh0S2moSHzjD9GAVlUenRXfBf4/ljFZuLm1hxhTBjD1R35jCLgFVRzoY5QmOG4KNN1YXfmoTsQ/2RoBBZMUoki3qwvrj+syP/WoaCbwM04OR3Q5SNnaCFwYvlO8zVl/kuFGA9vv4at9f5r8Zgh3gi3pRFFClm7ps6qGD/S8M//ZpuG1uu/zJvWYncYW3+LssqH3gA2aAu2/bGR+CtBb0NtnXGhQvBWP2953OByMC7gp#3QpIaDOX+TrVQVN0WZxmcJ3snlGkitOhlvszEjxknJTnfN7s"
ua = "AwemeLite 14.9.0 rv:149005 (iPhone; iOS 16.4.1; zh_CN) Cronet"


class DY:
    def __init__(self, cookie):
        self.url = cookie.split("#")[0]
        self.cookie = cookie.split("#")[1]
        self.argus = cookie.split("#")[2]
        self.ladon = cookie.split("#")[3]
        self.nickname = self.get_nickname()

    def run(self):
        self.get_info()

        self.sign_in()
        time.sleep(1.5)
        self.read()
        time.sleep(1.5)
        self.open_box()
        print(f"准备看广告,假装看15s")
        time.sleep(random.randint(20, 30))
        self.box_ad()
        self.detail_info()
        time.sleep(random.randint(20, 30))
        self.detail_ad()
        step = self.get_step()
        time.sleep(0.5)
        self.read()
        time.sleep(1.5)
        self.upload_step(step)
        self.step_reward()

    def sign_in(self):
        try:
            url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/sign_in?{self.url}"
            headers = {
                'Host': 'api5-normal-c-lf.amemv.com',
                'Connection': 'keep-alive',
                'Content-Length': '22',
                'Accept': 'application/json',
                'Cookie': self.cookie,
                'User-Agent': ua,
                'passport-sdk-version': '5.12.1',
                'X-Argus': self.argus,
                'X-Ladon': self.ladon,
                'Content-Type': 'text/plain'}
            payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
            response = requests.request("POST", url=url, headers=headers, data=payload)
            print(f"[{self.nickname}]签到成功,获取音符{response.json().get('data').get('amount')}")
        except:
            print("签到失败,可能今日已签到")

    def get_info(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/page?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Accept': 'application/json',
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        response = requests.request("GET", url=url, headers=headers)
        if response.json().get("data").get("is_login"):
            print(f"[{self.nickname}]登录成功\n"
                  f"[{self.nickname}]今日金币{response.json().get('data').get('income_data').get('amount1')}")

    def get_nickname(self):
        now = str(time.time()).replace(".", "")[:10]
        url = f"https://api5-core-c-lf.amemv.com/aweme/v1/user/profile/self/?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Content-Type': 'application/json; encoding=utf-8',
                   'Accept': 'application/json',
                   'tt-request-time': now,
                   'X-Argus': self.argus,
                   'X-Ladon': self.ladon,
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        payload = None
        try:
            response = requests.request("GET", url=url, headers=headers, data=payload)
            nickname = response.json().get("user").get("nickname")
            return nickname
        except:
            print("获取用户名失败")

    def read(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/read?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon,
            'Content-Type': 'text/plain'}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAsCiAgInRhc2tfa2V5IiA6ICJyZWFkIgp9")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]刷视频奖励--{response.json().get('data').get('score_amount')}")

    def open_box(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/treasure_task?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Content-Length': '22',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon,
            'Content-Type': 'text/plain'}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]开宝箱奖励音符--{response.json().get('data').get('amount')}")

    def box_ad(self):
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/excitation_ad_treasure_box?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("POST", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]看宝箱广告--{response.json().get('data').get('amount')}")

    def detail_info(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/sign_in/detail?{self.url}"
        headers = {'Host': 'api5-normal-c-lq.amemv.com',
                   'Content-Type': 'application/json; encoding=utf-8',
                   'Accept': 'application/json',
                   'tt-request-time': now,
                   'X-Argus': self.argus,
                   'X-Ladon': self.ladon,
                   'Cookie': self.cookie,
                   'User-Agent': ua}
        response = requests.request("GET", url=url, headers=headers)
        req_i = response.json().get("data").get("excitation_ad_info").get("req_id")
        ad_id = response.json().get("data").get("excitation_ad_info").get("ad_id")
        score_amount = response.json().get("data").get("excitation_ad_info").get("score_amount")
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]获取广告视频成功,预计获得{score_amount},假装看15秒")

    def detail_ad(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/done/excitation_ad?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("POST", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]看视频奖励音符成功--{response.json().get('data').get('amount')}")

    def get_step(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/page?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        response = requests.request("GET", url=url, headers=headers)
        if response.json().get("err_tips") == "成功":
            step = response.json().get("data").get("today_step")
            print(f"[{self.nickname}]当前步数{step}")
            return step
        else:
            print("走路出错")

    def upload_step(self, steps):
        now = str(time.time()).replace(".", "")[:10]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/step_submit?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        step = random.randint(steps, steps + 1200)
        payload = {"step": step,
                   "submit_time": int(now),
                   "in_sp_time": 0}
        payload = json.dumps(payload)
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]上传步数成功,当前步数--{response.json().get('data').get('today_step')}")

    def step_reward(self):
        now = str(time.time()).replace(".", "")[:13]
        url = f"https://api5-normal-c-lf.amemv.com/luckycat/aweme/v1/task/walk/receive_step_reward?{self.url}"
        headers = {
            'Host': 'api5-normal-c-lf.amemv.com',
            'Connection': 'keep-alive',
            'Accept': 'application/json',
            'Cookie': self.cookie,
            'User-Agent': ua,
            'passport-sdk-version': '5.12.1',
            'X-Argus': self.argus,
            'X-Ladon': self.ladon}
        payload = base64.b64decode("ewogICJpbl9zcF90aW1lIiA6IDAKfQ==")
        response = requests.request("POST", url=url, headers=headers, data=payload)
        if response.json().get("err_tips") == "成功":
            print(f"[{self.nickname}]领取步数奖励成功--{response.json().get('data').get('reward_amount')}")


if __name__ == "__main__":
    cookies = cookies.split("@")
    print(f"抖音激素版共获取到{len(cookies)}个账号by Pearson")
    print("bug提交https://t.me/+T8ozejX9rnkwZDE1")
    print("R18黄群不是我的,是内鬼外传改的")
    i = 1
    for cookie in cookies:
        print(f"---开始第{i}个账号---")
        i += 1
        DY(cookie).run()
        time.sleep(random.randint(60, 200))
