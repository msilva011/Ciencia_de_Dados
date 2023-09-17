BOT_NAME = 'pokespider'
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
ROBOTSTXT_OBEY = True
FEED_FORMAT = 'jsonlines'
FEED_URI = 'pokemons.json'
EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 1,
}
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 4
CONCURRENT_REQUESTS_PER_IP = 2
DEPTH_LIMIT = 3
COOKIES_ENABLED = False
LOG_LEVEL = 'INFO'
