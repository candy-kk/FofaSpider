#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import time
import base64
import random
import optparse
import requests

from urllib.parse import quote
from lxml import etree
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor


def cmd():
    parser = optparse.OptionParser()
    parser.add_option('-p', '--page', dest='page', type='int', default=5, help='write the page you want crawel')
    parser.add_option('-q', '--query', dest='query', help='write the query you want')
    parser.add_option('-c', '--cookie', dest='cookie', help='write your cookie')
    (options, args) = parser.parse_args()
    if options.query is None or options.cookie is None:
        parser.print_help()
        sys.exit(0)
    else:
        return options,args

class FofaSpider(object):

    def __init__(self,page,Cookie,q,qbase64):
        self.q = q
        self.qbase64 = qbase64
        self.page = page
        self.s = requests.Session()
        self.ua = UserAgent()
        # 这里的cookie 后面改成input 用户自己输入
        self.header = {"User-Agent": self.ua.random,"Cookie": Cookie}
        self.domains = set()

    def spider(self,page):
        try:
            # time.sleep(random.randint(3, 7))
            target = 'https://fofa.so/result?page={}&q={}&qbase64={}'.format(page,self.q, self.qbase64)
            res = self.s.get(url=target, headers=self.header).text
            # time.sleep(random.randint(3,7))
            selector = etree.HTML(res)
            domain = selector.xpath('//*[@id="ajax_content"]/div/div/div/a/text()')
            for value in domain:
                # print(value)
                value.strip(' ')
                self.domains.add(value)
                print(value)
            time.sleep(random.randint(3,7))
        except Exception as e:
            print(e)

    def run(self):
        pool = ThreadPoolExecutor(2)
        [pool.submit(self.spider,i) for i in range(1,self.page)]

if __name__ == '__main__':
    options,args = cmd()
    page = options.page + 1
    q = quote(options.query)
    qbase64 = quote(str(base64.b64encode(options.query.encode()),encoding='utf-8'))
    target = 'https://fofa.so/result?page={}&q={}&qbase64={}'.format(page, q, qbase64)
    cookie = options.cookie
    test = FofaSpider(page,cookie,q,qbase64)
    test.run()
