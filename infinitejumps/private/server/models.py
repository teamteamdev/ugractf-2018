from peewee import *
import json


db = SqliteDatabase("gameserver.db")


class User(Model):
    nickname = CharField(max_length=30, primary_key=True)
    score = IntegerField(default=0)
    time = IntegerField(default=0)

    class Meta:
        database = db

        
class Coupon(Model):
    code = CharField(max_length=30, primary_key=True)
    limit = IntegerField(default=0)
    usages = IntegerField(default=0)

    class Meta:
        database = db
        

class Message(Model):
    nickname = CharField(max_length=40)
    timestamp = TimestampField(utc=True)
    message = TextField()
    
    class Meta:
        database = db
