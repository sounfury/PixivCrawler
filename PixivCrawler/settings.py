# Scrapy 项目的配置文件

# 为了简单起见，这个文件只包含了一些重要或常用的设置。
# 更多设置请参考文档：
# https://docs.scrapy.org/en/latest/topics/settings.html
# https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# 爬虫的名称
BOT_NAME = "PixivCrawler"

# 爬虫模块和新建爬虫模块的位置
SPIDER_MODULES = ["PixivCrawler.spiders"]
NEWSPIDER_MODULE = "PixivCrawler.spiders"

# 在请求时声明自己的身份（可以设置为你的域名）
# USER_AGENT = "TestSpider (+http://www.yourdomain.com)"

# 遵守 robots.txt 规则
# 取消遵守 robots 协议
ROBOTSTXT_OBEY = False

# 设置 User-Agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

# 输出文件格式
FEED_FORMAT = 'json'
FEED_URI = 'output.json'

DOWNLOAD_DELAY = 0.25  # 设置为1秒延迟

# 启用或禁用下载器中间件
# 参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "PixivCrawler.middlewares.PixivcrawlerDownloaderMiddleware": 543,
}

# 设置图片保存的主目录
IMAGES_STORE = 'E:/图片/test/'


LOG_LEVEL = 'DEBUG'  # 设置日志级别，DEBUG 会输出所有信息

# 配置 Scrapy 执行的最大并发请求数（默认是 16）
CONCURRENT_REQUESTS = 24

# 为同一网站配置请求延迟（默认是 0）
# 参考 https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# 也可以参考 AutoThrottle 设置和文档
# DOWNLOAD_DELAY = 3
# 下载延迟设置只会影响以下其中之一：
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# 禁用 Cookies（默认启用）
# COOKIES_ENABLED = False

# 禁用 Telnet Console（默认启用）
# TELNETCONSOLE_ENABLED = False

# 默认请求头：


DEFAULT_REQUEST_HEADERS = {
    'referer': 'https://www.pixiv.net/',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.41',
    "Accept-Language": "en",
}

# 图片管道
ITEM_PIPELINES = {
    'PixivCrawler.pipelines.CustomImagesPipeline': 1,
}

# 启用或禁用爬虫中间件
# 参考 https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "TestSpider.middlewares.SpiderSpiderMiddleware": 543,
# }


# 启用或禁用扩展
# 参考 https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
# }


# 启用并配置 AutoThrottle 扩展（默认禁用）
# 参考 https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# 在高延迟情况下设置的最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# Scrapy 应该并行发送到每个远程服务器的平均请求数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# 启用显示每个响应接收到的 AutoThrottle 调节状态：
# AUTOTHROTTLE_DEBUG = False

# 启用并配置 HTTP 缓存（默认禁用）
# 参考 https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTP 缓存的过期时间（以秒为单位）
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTP 缓存存储位置
# HTTPCACHE_DIR = "httpcache"
# 忽略哪些 HTTP 状态码的缓存
# HTTPCACHE_IGNORE_HTTP_CODES = []
# 使用的缓存存储机制
# HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# 设置将默认值设置为向后兼容的值
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
