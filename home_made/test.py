import redis
import json
import requests
from lxml import etree


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
]

# proxies = list(filter(lambda x: json.loads(x).get("https"), item_dict.values()))
# for item in proxies:
#     print(item)

# 转换item为Python字典
for num, item in enumerate(item_dict.values(), start=1):
    item_dict = json.loads(item)
    if not item_dict.get("https"):
        continue
    print("proxy", item_dict)

    proxy = item_dict['proxy']
    proxies = {
        'http': f'http://{proxy}',
        'https': f'https://{proxy}'
    }

    url = urls.pop()
    response = requests.get(url, headers=headers, proxies=proxies)
    http_code = response.status_code
    xp = etree.HTML(response.text)
    print('title', xp.xpath('//title/text()'))
    print('http_code', http_code)

    if num == 10:
        break