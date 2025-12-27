# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class TwoPipeline:

    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('test.db')
        self.current = self.connection.cursor()

    def create_table(self):
        self.current.execute(""" drop table if exists joblist  """)
        self.current.execute(""" create table joblist(title text)  """)

    def insert(self,item):
        self.current.execute(""" insert into joblist(title) values (?) """,(item['title'],))        
        self.connection.commit()

    def process_item(self, item, spider):
        self.insert(item)
        return item
