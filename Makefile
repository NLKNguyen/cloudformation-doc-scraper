all: resources parameters

resources:
	rm -f resources.json
	scrapy runspider resources_spider.py -o resources.json

parameters:
	rm -f parameters.json
	scrapy runspider parameters_spider.py -o parameters.json
