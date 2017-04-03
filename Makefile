all:
	rm -f resources.json
	scrapy runspider cloudformation_spider.py -o resources.json
