import sqlite3
from combined.items import Work1Item, Work2Item, Work3Item

class Work1Pipeline:
    def __init__(self):
        self.create_Connection()
        self.CreateTable()

    def create_Connection(self):
        self.connection = sqlite3.connect('testingOne.db')
        self.current = self.connection.cursor()

    def CreateTable(self):
        self.current.execute(""" drop table if exists One """)
        self.current.execute(""" create table One(job_title text,location text,Skills text,date text,category text)""")

    def Insert(self,item):
        self.current.execute(""" insert into One(job_title ,location ,Skills ,date ,category ) values (?,?,?,?,?)""",(item['job_title'],item['location'],item['Skills'],item['date'],item['category']))
        self.connection.commit()

    def process_item(self, item, spider):
        if isinstance(item, Work1Item):
            self.Insert(item)
        return item

    
    def close_spider(self, spider):
        self.connection.close()

class Work2Pipeline:
    def __init__(self):
        self.create_Connection()
        self.CreateTable()

    def create_Connection(self):
        self.connection = sqlite3.connect('testingTwo.db')
        self.current = self.connection.cursor()

    def CreateTable(self):
        self.current.execute(""" drop table if exists Two """)
        self.current.execute(""" create table Two(job_role text,company text,posted_on text,salary text,location text)""")

    def Insert(self,item):
        self.current.execute(""" insert into Two(job_role ,company ,posted_on ,salary ,location ) values (?,?,?,?,?)""",(item['job_role'],item['company'],item['posted_on'],item['salary'],item['location']))
        self.connection.commit()

    def process_item(self, item, spider):
        if isinstance(item, Work2Item):
            self.Insert(item)
        return item
    
    
    def close_spider(self, spider):
        self.connection.close()

class Work3Pipeline:
    def __init__(self):
        self.create_Connection()
        self.CreateTable()

    def create_Connection(self):
        self.connection = sqlite3.connect('testingThree.db')
        self.current = self.connection.cursor()

    def CreateTable(self):
        self.current.execute(""" drop table if exists Three """)
        self.current.execute(""" create table Three(job_Title text,location text,date text,category text,skills text)""")

    def Insert(self,item):
        self.current.execute(""" insert into Three(job_Title ,location ,date ,category ,skills ) values (?,?,?,?,?)""",(item['job_Title'],item['location'],item['date'],item['category'],item['skills']))
        self.connection.commit()

    def process_item(self, item, spider):
        if isinstance(item, Work3Item):
            self.Insert(item)
        return item
    
    
    def close_spider(self, spider):
        self.connection.close()
