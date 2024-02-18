# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     proxyFetcher
   Description :
   Author :        JHao
   date：          2016/11/25
-------------------------------------------------
   Change Activity:
                   2016/11/25: proxyFetcher
-------------------------------------------------
"""
__author__ = 'JHao'

import re
import json
from time import sleep

from util.webRequest import WebRequest


class ProxyFetcher(object):
    """
    proxy getter
    """

    @staticmethod
    def freeProxy05(page_count=1):
        """ 快代理 https://www.kuaidaili.com """
        url_pattern = [
            'https://www.kuaidaili.com/free/fps/{}/',
        ]
        url_list = []
        for page_index in range(1, page_count + 1):
            for pattern in url_pattern:
                url_list.append(pattern.format(page_index))

        for url in url_list:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            sleep(1)  # 必须sleep 不然第二条请求不到数据
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])

    @staticmethod
    def freeProxy06():
        """ 冰凌代理 https://www.binglx.cn """
        url = "https://www.binglx.cn/?page=1"
        try:
            tree = WebRequest().get(url).tree
            proxy_list = tree.xpath('.//table//tr')
            for tr in proxy_list[1:]:
                yield ':'.join(tr.xpath('./td/text()')[0:2])
        except Exception as e:
            print(e)

    @staticmethod
    def freeProxy07():
        """ 云代理 """
        urls = ['http://www.ip3366.net/free/?stype=1', "http://www.ip3366.net/free/?stype=2"]
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td>[\s\S]*?<td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy08():
        """ 小幻代理 """
        urls = ['https://ip.ihuan.me/address/5Lit5Zu9.html']
        for url in urls:
            r = WebRequest().get(url, timeout=10)
            proxies = re.findall(r'>\s*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s*?</a></td><td>(\d+)</td>', r.text)
            for proxy in proxies:
                yield ":".join(proxy)

    @staticmethod
    def freeProxy09(page_count=1):
        """ 免费代理库 """
        for i in range(1, page_count + 1):
            url = 'http://ip.jiangxianli.com/?country=中国&page={}'.format(i)
            html_tree = WebRequest().get(url, verify=False).tree
            for index, tr in enumerate(html_tree.xpath("//table//tr")):
                if index == 0:
                    continue
                yield ":".join(tr.xpath("./td/text()")[0:2]).strip()

    @staticmethod
    def freeProxy10():
        """ 89免费代理 """
        r = WebRequest().get("https://www.89ip.cn/index_1.html", timeout=10)
        proxies = re.findall(
            r'<td.*?>[\s\S]*?(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})[\s\S]*?</td>[\s\S]*?<td.*?>[\s\S]*?(\d+)[\s\S]*?</td>',
            r.text)
        for proxy in proxies:
            yield ':'.join(proxy)

    @staticmethod
    def freeProxy11():
        """ 稻壳代理 https://www.docip.net/ """
        r = WebRequest().get("https://www.docip.net/data/free.json", timeout=10)
        try:
            for each in r.json['data']:
                yield each['ip']
        except Exception as e:
            print(e)

if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy06():
        print(_)