import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()


def title():
    print("""
                                  检测fastjson脚本
                      use: python3 检测fastjson脚本.py
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
            # 'Cookie': '',
            'Content-Type': 'application/json'
        }
        proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        test = '{"@type":"java.lang.AutoCloseable"'
        url = self.url + "/fastjson/deserialize"
        try:
            requests.packages.urllib3.disable_warnings()
            etc_passwd = requests.post(url, data=test, headers=headers, proxies=proxies, verify=False, timeout=2)
            rt = etc_passwd.text
            if 'version' in rt and etc_passwd.status_code == 200:
                print("\033[32m[o]" + self.url + "检测出fastjson结果：" + rt + "\033[0m")
                with open("fastjson版本检测结果.txt", mode="a") as rp:
                    rp.write(self.url + " 版本信息：" + rt + "\n")
            elif etc_passwd.status_code == 404:
                print(self.url + ' 未检测出版本信息！')
            else:
                print(self.url + ' 未检测出版本信息！')
                pass

        except:
            print(self.url + ' 未检测出版本信息！')
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
    parser = argparse.ArgumentParser(description="检测fastjson脚本")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 检测fastjson脚本.py -u http://127.0.0.1\neg2:>>>python3 检测fastjson脚本.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
