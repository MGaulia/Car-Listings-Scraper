# -*- coding: utf-8 -*-

# Scrapy settings for carlistings project

BOT_NAME = 'carlistings'

SPIDER_MODULES = ['carlistings.spiders']
NEWSPIDER_MODULE = 'carlistings.spiders'

USER_AGENT='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

LOG_LEVEL='DEBUG'
# Obey robots.txt rules
ROBOTSTXT_OBEY = True

REACTOR_THREADPOOL_MAXSIZE = 128
CONCURRENT_REQUESTS = 256
CONCURRENT_REQUESTS_PER_DOMAIN = 256
CONCURRENT_REQUESTS_PER_IP = 256

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 3
AUTOTHROTTLE_MAX_DELAY = 5
AUTOTHROTTLE_TARGET_CONCURRENCY = 128
AUTOTHROTTLE_DEBUG = True