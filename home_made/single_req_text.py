import requests
from util.webRequest import WebRequest

def req1():
    url_pattern = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"

    ips = WebRequest().get(url_pattern).text.split('\n')
    for ip in ips:
        if ip:
            yield ip.strip().replace('\r', '')

req1()
