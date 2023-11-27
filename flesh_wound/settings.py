# settings.py

BOT_NAME = 'FleshWound'
SPIDER_MODULES = ['FleshWound.spiders']
NEWSPIDER_MODULE = 'FleshWound.spiders'

ROBOTSTXT_OBEY = True

# Configure the ImagesPipeline
ITEM_PIPELINES = {
    'scrapy.pipelines.images.ImagesPipeline': 1,
    'scrapy.pipelines.files.FilesPipeline': 2,
}

IMAGES_STORE = 'media'  # This should be the name of your media folder
FILES_STORE = 'media'  # This should be the name of your media folder
