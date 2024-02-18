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


if __name__ == '__main__':
    p = ProxyFetcher()
    for _ in p.freeProxy06():
        print(_)