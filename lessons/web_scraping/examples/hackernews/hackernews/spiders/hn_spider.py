from scrapy import Spider 
from scrapy.selector import Selector

from hackernews.items import HackerNewsItem


class HNSpider(Spider):
    name = 'hnspider'
    allowed_domains = ["https://news.ycombinator.com/"]
    start_urls = ["https://news.ycombinator.com/"]

    def parse(self, response):
        posts = Selector(response).xpath("//tr")

        for post in posts:
            item = HackerNewsItem()
            item['title'] = post.xpath("td[@class='title']/a/text()").extract()
            yield item 

#("//tr/td[@class='title']/a/text()")