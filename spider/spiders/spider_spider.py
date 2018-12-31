# -*- coding: utf-8 -*-
import scrapy
from spider.items import SpiderItem

class SpiderSpiderSpider(scrapy.Spider):
    #爬虫名
    name = 'spider_spider'
    #允许的域名
    allowed_domains = ['movie.douban.com']
    #入口URL，扔到调度器
    start_urls = ['https://movie.douban.com/top250']


    #默认的解析方法

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']//li")

        #循环电影的条目

        for i_item in movie_list:
            #item文件导进来
            spider_item = SpiderItem()
            #写详细的xpath，进行数据解析
            spider_item['serial_number'] = i_item.xpath(".//div[@class='item']//em/text()").extract_first()

            spider_item['movie_name'] = i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            content = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            #数据的处理
            for i_content in content:
                content_s = "".join(i_content.split())
                spider_item['introduce'] = content_s


            # print(spider_item['introduce'])
            spider_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()
            spider_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first()
            spider_item['describe'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()
            #你需要将数据yield到pipelines里面去
        #
            yield spider_item
        #解析下一页,取后页的xpath
        next_link = response.xpath("//span[@class='next']/a/@href").extract()
        #判断是否有下一页按钮
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link,callback=self.parse) #回调函数
