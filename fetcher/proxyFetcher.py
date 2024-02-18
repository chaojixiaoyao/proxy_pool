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
    def free_proxy1():
        """https://github.com/hookzof/socks5_list"""
        url_pattern = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy2():
        """https://github.com/sunny9577/proxy-scraper"""
        url_pattern = "https://sunny9577.github.io/proxy-scraper/generated/http_proxies.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy3():
        """https://github.com/proxy4parsing/proxy-list"""
        url_pattern = "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy4():
        """https://github.com/roosterkid/openproxylist"""
        url_pattern = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy5():
        """https://github.com/mmpx12/proxy-list"""
        url_pattern = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy6():
        """https://github.com/monosans/proxy-list/tree/main"""
        url_pattern = "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy7():
        """https://github.com/TheSpeedX/PROXY-List"""
        url_pattern = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy8():
        # have protocol
        """https://github.com/ObcbO/getproxy"""
        url_pattern = "https://cdn.jsdelivr.net/gh/ObcbO/getproxy/file/https.txt"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy9():
        # have protocol
        """https://proxyscrape.com/free-proxy-list"""
        url_pattern = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=yes&anonymity=all"

        ips = WebRequest().get(url_pattern).text.split('\n')
        for ip in ips:
            if ip:
                yield ip.strip().replace('\r', '')

    @staticmethod
    def free_proxy10(page_count=1):
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


if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy06():
        print(_)