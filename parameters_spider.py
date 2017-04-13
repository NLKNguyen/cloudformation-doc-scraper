import scrapy

class ParametersSpider(scrapy.Spider):
    name = "Parameters Spider"
    start_urls = ['http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html']

    def parse(self, response):
        properties = response.xpath('//div[@class="variablelist"][1][not(ancestor::dd)]/dl/dt//code/text()').extract()
        for property in properties:
            obj = {'property': property}
            yield obj
