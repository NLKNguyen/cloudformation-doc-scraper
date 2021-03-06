import scrapy
from scrapy.http import Request

class ResourcesSpider(scrapy.Spider):
    name = "Resources Spider"
    start_urls = ['http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html']

    def parse(self, response):
        aws_resource_ahrefs = response.xpath('//div[@id="main-col-body"]//div[@class="highlights"]/ul/li/a')
        aws_resource_pages = aws_resource_ahrefs.xpath('@href').extract()

        for page in aws_resource_pages:
            url = 'http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/' + page
            request = Request(url, callback=self.parse_single_resource_ref)
            yield request

    def parse_single_resource_ref(self, response):
        obj = {}
        # obj['url'] = response.url
        obj['resource'] = response.xpath('//h1[@class="topictitle"]/text()').extract_first()
        obj['properties'] = response.xpath('//div[@class="variablelist"]//dt//code/text()').extract()
        yield obj


