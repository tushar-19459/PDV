# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class Work3Pipeline:
    def __init__(self):
        self.create_Connection()
        self.CreateTable()

    def create_Connection(self):
        self.connection = sqlite3.connect('Work3.db')
        self.current = self.connection.cursor()
        pass

    def CreateTable(self):
        self.current.execute(""" drop table if exists work3 """)
        self.current.execute(""" create table work3(job_Title text,location text,date text,category text,skills text)""")
        pass

    def Insert(self,item):
        self.current.execute(""" insert into work3(job_Title ,location ,date ,category ,skills ) values (?,?,?,?,?)""",(item['job_Title'],item['location'],item['date'],item['category'],item['skills']))
        self.connection.commit()
        pass

    def process_item(self, item, spider):
        self.Insert(item)
        return item