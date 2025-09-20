# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class Work1Pipeline:
    def __init__(self):
        self.create_Connection()
        self.CreateTable()

    def create_Connection(self):
        self.connection = sqlite3.connect('Work1.db')
        self.current = self.connection.cursor()
        pass

    def CreateTable(self):
        self.current.execute(""" drop table if exists work1 """)
        self.current.execute(""" create table work1(job_title text,location text,Skills text,date text,category text)""")
        pass

    def Insert(self,item):
        self.current.execute(""" insert into work1(job_title ,location ,Skills ,date ,category ) values (?,?,?,?,?)""",(item['job_title'],item['location'],item['Skills'],item['date'],item['category']))
        self.connection.commit()
        pass

    def process_item(self, item, spider):
        self.Insert(item)
        return item

