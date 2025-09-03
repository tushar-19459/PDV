# Scrapy settings for work_2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "work_2"

SPIDER_MODULES = ["work_2.spiders"]
NEWSPIDER_MODULE = "work_2.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "work_2 (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Connection': 'keep-alive',
    # 'Cookie': 'x-georegion=104,IN,KA,UDIPI,,,,,,13.35,74.75,GMT+5.50,,AS,,,45769,vhigh,5000; visitor_layeruid=c9467602-014c-46eb-b884-1e71a2ee1b17_1_rmc_GENRIC; ew_exp=eed16e85-6b2a-419d-8c13-474003f67c36_4_1_0_rmc_030925; ak_bmsc=877721042E11B9CAB910DDFB12FF260F~000000000000000000000000000000~YAAQ3wFAF/OvdfCYAQAAhYfhDhx8R3o7czV5zxfrwpj/UgDiCKDiq6ZF9zY5o9d1v175B8vRAO1fVHIElyo8d82GlNKu1iO8ntbJEk0JXVFDqtWogLNPIm1vT0/+wUVIorR3Lrz6IRRP5cdZFwnFpVXEuwth07NQjveWRn+UpAOQPtObV+O+8VIOkcyqZ6/B2ycS5KgBCkQvQpdJzvaqw61rN5VFfl0kWdmW9VrN7vGdtWlyxVKagYpTXzE+VKIzDUsU1apzrWsKx/2sYDKm5ZsG/kEPiZpmIFYNiuB5YKh8zjQf6LiabUhkGeXXvF5CVXRWVYcpxUtBxnWmajVazJvXWpmKma1evtFH9Xq/PMds9nB30E6R2fm6DjpeIikys6AP65oaMZ+lzTZB6Z1iPu4J5fGMAShL7WL6PAcohnzYHJxM0XyGr7lovAcMPdEPfj9AfASp/4gr8AdeLt5y; vssessionuid=75421570-6cdb-4970-b759-4bc117cd7c71; bm_sv=471A21A2C1A4896995D49818CBD47CAD~YAAQ3wFAF/ewdfCYAQAAZcfhDhzN8WZplINKAg4Yg8UZj7fKk0Ohn03TKznK1gZoaJmH1Sc8fGMgvsapxh5nefx03j3xme3/c2qcSM5l30fJmcNiRTegmdt1AHM5S/cuKflnhjzibtrQPL3iJPcg7j42ooIMI6VCdKx3Vgg3YYJXH0HhRWQFhwxnCeJJV6OWO6V2T7pCOl9yK4IiCXA5+JhOvLIVOvjfZ9AeZmCYUawFT4nCiyMogqLgHNB/pwc=~1; vstr=3ed9fbaf-c85c-4f25-8b5b-28b2de025183; vsuid=ce9c0c93-d629-4d91-a6d2-d1d35458b9f1; ref=3; visitinfo=[City,Udupi]&[State,KA]&[Country,IN]&[PostalCode,576101]; vsutms=468ca54b-b19f-489f-987c-e3f5c40cfb2e#3ed9fbaf-c85c-4f25-8b5b-28b2de025183#ce9c0c93-d629-4d91-a6d2-d1d35458b9f1#1756891285##||||; COOKIE_CONSENT={"key":"eyJuZWNlc3NhcnkiOnRydWUsImFuYWx5dGljcyI6dHJ1ZSwiYWR2ZXJ0aXNpbmciOnRydWUsInBlcnNvbmFsaXphdGlvbiI6dHJ1ZX0=","consent":{"necessary":true,"analytics":true,"advertising":true,"personalization":true},"accepted":true}; fs_user=0; vstrType=1; _ga_DJ23BNLRSH=GS2.1.s1756871485$o1$g1$t1756871500$j45$l0$h0; _ga=GA1.1.78465561.1756871485; ajs_anonymous_id=74ec07bd-f389-4045-95bb-6a9195ed14c7',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Priority': 'u=0, i',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "work_2.middlewares.Work2SpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    "work_2.middlewares.Work2DownloaderMiddleware": 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "work_2.pipelines.Work2Pipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"
