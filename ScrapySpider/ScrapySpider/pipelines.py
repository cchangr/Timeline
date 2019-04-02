# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import pymysql.cursors

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi


class ArticlePipeline(object):
    def process_item(self, item, spider):
        return item


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
       if 'front_image_url' in item:
           for ok, value in results:
              image_file_path = value["path"]
           item["front_image_path"] = image_file_path
       return item


class JsonWithEncodingPipeline(object):
    def __init__(self):
        self.file = codecs.open('article.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False) + '\n'
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


class JsonExporterPipeline(object):
    # 调用scrapy提供的josn export 导出json文件
    def __init__(self):
        self.file = open('articleexport.json', 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item


class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', password='', database='spider', port=3306,
                                    use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # MYSQL同步操作
        insert_sql = """
            insert into jobbole_article(title, create_date, url, fav_nums)
            VALUES (%s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'], item['create_date'], item['url'], item['fav_nums']))
        self.conn.commit()


# MYSQL 异步写入
class MysqlTwistedPipeline(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        db = dict(
            host=settings['MYSQL_HOST'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            database=settings['MYSQL_DBNAME'],
            port=settings['MYSQL_PORT'],
        )

        dbpool = adbapi.ConnectionPool("pymysql", **db)
        return cls(dbpool)

    def process_item(self, item, spider):
        # 使用twisted异步执行mysql
        query = self.dbpool.runInteraction(self.do_insert, item)
        # 异常处理
        query.addErrback(self.handle_error, item, spider)

    def handle_error(self, failure, item, spider):
        print(failure)


    def do_insert(self, cursor, item):
        # MYSQL同步操作
        insert_sql = """
                    insert into jobbole_article(title, create_date, url, fav_nums)
                    VALUES (%s, %s, %s, %s)
                """
        cursor.execute(insert_sql, (item['title'], item['create_date'], item['url'], item['fav_nums']))

