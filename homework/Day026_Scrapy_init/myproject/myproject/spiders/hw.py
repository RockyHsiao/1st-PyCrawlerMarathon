# -*- coding: utf-8 -*-
import scrapy
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pprint import pprint


class HwSpider(scrapy.Spider):
    name = 'hw'
    allowed_domains = ['https://www.ptt.cc/bbs/Lifeismoney/M.1577848601.A.99A.html']
    start_urls = ['http://https://www.ptt.cc/bbs/Lifeismoney/M.1577848601.A.99A.html/']

    def parse(self, response):
        pass
    
        
