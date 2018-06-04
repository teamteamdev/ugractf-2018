from peewee import *

db = PostgresqlDatabase("postgres", user="postgres", host="postgres", port=5432)


class User(Model):
    id = IntegerField(primary_key=True)
    highscore = IntegerField(default=0)
    
    class Meta:
        database = db
