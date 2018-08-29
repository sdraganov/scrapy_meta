
BOT_NAME = 'meta_test'

SPIDER_MODULES = ['meta_test.spiders']
NEWSPIDER_MODULE = 'meta_test.spiders'


DOWNLOADER_MIDDLEWARES = {
   'meta_test.middlewares.DownloaderMiddleware': 543,
}

