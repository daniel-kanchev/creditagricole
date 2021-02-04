BOT_NAME = 'creditagricole'
SPIDER_MODULES = ['creditagricole.spiders']
NEWSPIDER_MODULE = 'creditagricole.spiders'
ROBOTSTXT_OBEY = True
LOG_LEVEL = 'WARNING'
ITEM_PIPELINES = {
    'creditagricole.pipelines.DatabasePipeline': 300,
}
