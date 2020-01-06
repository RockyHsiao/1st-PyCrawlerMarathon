import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings


def main():
    target_urls = [
        'https://www.ptt.cc/bbs/Gossiping/M.1119417269.A.9CB.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1578286948.A.713.html',
        'https://www.ptt.cc/bbs/Gossiping/M.1578287221.A.4CE.html'
    ]
    process = CrawlerProcess(get_project_settings())
    process.crawl('PTTCrawler', start_urls=target_urls, filename='hw.json')
    process.start()

if __name__ == '__main__':
    main()
