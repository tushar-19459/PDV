# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class OnePipeline:
    def __init__(self):
        self.create_connection()
        self.create_table()

    def create_connection(self):
        self.connection = sqlite3.connect('tushar.db')
        self.current = self.connection.cursor()
        

    def create_table(self):
        self.current.execute('drop table if exists new_Quotes')
        self.current.execute(""" 
        create table new_Quotes (quotes text , author text ,tag text)    
        """)
        

    def insert_data(self,item,spider):
        self.current.execute("""
            insert into new_Quotes(quotes,author,tag) values (?,?,?)
        """,(item['quote'],item['author'],item['tags']))
        self.connection.commit()
        # spider.logger.info
        

    def process_item(self, item, spider):
        self.insert_data(item,spider)
        return item
