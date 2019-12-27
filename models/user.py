from peewee import *


DATABASE    =   SqliteDatabase("example.db")


class BaseModel(Model):
    class Meta:
        database    =  DATABASE 

class Users(BaseModel):
    username    =   TextField()
    passwd      =   TextField()
    email       =   TextField()


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([Users],safe=True)
    DATABASE.close()