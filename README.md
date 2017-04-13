CloudFormation Doc Scraper
====

Written in Python 3, used [Scrapy](https://scrapy.org/)

__Project files__:

+ `*_spider.py` : scraper scripts to be executed with Scrapy

+ `*.json` : output file using the corresponding `*_spider.py` from the last script execution. Ready to be consumed.

+ `Makefile` : run commands

Run instruction using Makefile:

```shell
$ make all

```

or separately:

```shell
$ make resources

$ make parameters
```

# References

Web pages that are scrapped:

+ AWS Resources: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html

+ Parameter Properties: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/parameters-section-structure.html

# Dev notes

Use XPath API to extract data from the pages.

Use Scrapy shell ([doc](https://doc.scrapy.org/en/latest/topics/shell.html)) to easily test XPath queries before putting those in Python script.

Each Python script is responsible for scrapping only one type of data to make things short and easy to manage.

