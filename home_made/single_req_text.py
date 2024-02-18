import requests
from util.webRequest import WebRequest
import re
from time import sleep


def req1(page_count=1):
    print(111111111111)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    r = requests.get("https://www.docip.net/data/free.json", headers=headers, timeout=10)
    try:
        for each in r.json['data']:
            print(each)
            yield each['ip']
    except Exception as e:
        print(e)


print(1111)
req1()
print(2222)