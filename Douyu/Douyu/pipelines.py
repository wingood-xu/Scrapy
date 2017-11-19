# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import scrapy, os


class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipeline(ImagesPipeline):
    IMAGE_STORE = get_project_settings().get('IMAGES_STORE')
    print(IMAGE_STORE)

    def get_media_requests(self, item, info):
        # print(item)
        # print(item['image_link'])
        yield scrapy.Request(item['image_link'])

    def item_completed(self, results, item, info):
        # print(results)
        file_paths = [x['path'] for ok, x in results if ok]
        old_name = self.IMAGE_STORE + os.sep + file_paths[0].replace('/', os.sep)

        new_name = self.IMAGE_STORE + os.sep + file_paths[0].split('/')[0] + os.sep + item['nick_name'] + '.jpg'
        os.rename(old_name, new_name)
        item['image_path'] = new_name
        print(old_name)
        print(new_name)
        return item
