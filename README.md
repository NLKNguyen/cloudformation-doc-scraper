CloudFormation Doc Scraper
====

Written in Python 3, used [Scrapy](https://scrapy.org/)

__Project files__:

+ `cloudformation_spider.py` : scraper script to be executed with Scrapy

+ `resources.json` : output file from the last script execution. Ready to be consumed.

+ `Makefile` : run commands

Run instruction using Makefile:
```
$ make
```

or manually:

```shell
$ scrapy runspider cloudformation_spider.py -o resources.json
```

`resources.json` file should be deleted prior script execution.