import scrapy
from scrapy.loader import ItemLoader
from datetime import datetime
from itemloaders.processors import TakeFirst
from creditagricole.items import Article


class CreditSpider(scrapy.Spider):
    name = 'credit'
    allowed_domains = ['ca-cib.com']
    start_urls = ['https://www.ca-cib.com/pressroom/news']

    def parse(self, response):
        articles = response.xpath('//a[@class="news-tile"]')
        for article in articles:
            date = article.xpath('.//time/text()').get()
            link = article.xpath('./@href').get()
            yield response.follow(link, self.parse_article, cb_kwargs=dict(date=date))

    def parse_article(self, response, date):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        date = datetime.strptime(date, '%d.%m.%Y')
        date = date.strftime('%Y/%m/%d')

        title = response.xpath('//h1/text()').get()
        content = response.xpath('//div[@class="body-description"]//text()').getall()
        content = '\n'.join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
