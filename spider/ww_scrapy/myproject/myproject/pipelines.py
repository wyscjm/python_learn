# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from myproject.items import UstcItem

import os
import shutil

from scrapy.contrib.pipeline.files import FilesPipeline

class MyprojectPipeline(object):
    def process_item(self, item, spider):
        return item

class UstcPipeline(FilesPipeline):

    """
    def file_path(self, request, response=None, info=None):  
        image_guidj
        
    def file_path(self, request, response=None, info=None):  
        image_guid = request.url.split('/')[-1]  
        print "ustc1"
        return 'full/%s' % (image_guid)  

    def get_media_requests(self, item, info):
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

    def close_spider(self, spider):
        print "close_spider"


    def process_item(self, item, spider):
        if spider.name == "ustc":
            print "ustc:",item
            self.ustc_name = item["title"]
            dir = "/tmp/scrapy/"
            src_name = dir + item["files"][0]["path"]
            file_type = os.path.splitext(src_name)[1]
            dest_dir = dir + "ustc/"
            if not os.path.exists(dest_dir):
                os.mkdir(dest_dir)
            dest_name = dest_dir + item["title"][0] + file_type
            #os.rename(src_name,dest_name)
            shutil.copy(src_name,dest_name)
            print "ustc:",item["title"][0]
            print "ustc2:",item["files"]
            #print "ustc:",dest_name
        return item
    
    """

    def file_path(self, request, response=None, info=None):  
        image_guid = request.url.split('/')[-1]  
        return 'full/%s' % (image_guid)  

    def item_completed(self, results, item, info):
        return item
