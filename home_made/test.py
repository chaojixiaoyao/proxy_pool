import redis
import json
import requests
from lxml import etree
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


# Redis连接参数
redis_config = {"host": "127.0.0.1", "port": 6379, "password": "", "db": 0}

# 连接到Redis
r = redis.Redis(**redis_config)

# 获取哈希表中键值对的数量
item_dict = r.hgetall("use_proxy")


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'}
urls = [
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.persiantv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.ruradio',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.latintv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.ngradio',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.sradio',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.radio',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.bihradio',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.bulgariantv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.latviantv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.ukrainiantv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.burmesetv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.greektv',
    'https://webcache.googleusercontent.com/search?q=cache:https://play.google.com/store/apps/details?id=com.antonio.congotvk',
]

# proxies = list(filter(lambda x: json.loads(x).get("https"), item_dict.values()))
# for item in proxies:
#     print(item)

# 转换item为Python字典
for num, item in enumerate(item_dict.values(), start=1):
    item_dict = json.loads(item)
    if not item_dict.get("https"):
        continue
    elif '中国' in item_dict.get("region") and '香港' not in item_dict.get("region"):
        continue
    elif '中国' in item_dict.get("region") and '台湾' not in item_dict.get("region"):
        continue
    print("proxy", item_dict)

    proxy = item_dict['proxy']
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    url = urls.pop()
    try:
        response = requests.get(url, headers=headers, proxies=proxies, verify=False, timeout=10)
        http_code = response.status_code
        xp = etree.HTML(response.text)
        title = xp.xpath('//title/text()')
        print('title', xp.xpath('//title/text()'))
        print('http_code', http_code)
        if not title or http_code != 200:
            print('text@@@', response.text)
    except (requests.exceptions.ProxyError, requests.exceptions.ConnectTimeout) as pe:
        print(pe)

    if num == 10:
        break