import pymongo
from flask import current_app, g
from flask.cli import with_appcontext
from .schema import instructions

CONNECTION_STRING = 'mongodb+srv://noobmaster69:a1e2i3o4u5@cluster0.pd5jd.gcp.mongodb.net/fooddb?retryWrites=true&w=majority'

def get_db():
    if 'db' not in g:
        g.db = pymongo.MongoClient(current_app.config['DATABASE_HOST'])
    return g.db

def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()




myclient = pymongo.MongoClient(CONNECTION_STRING)

mydb = myclient["fooddb"]

mycol = mydb['test']

for x in mycol.find():
  print(x)















    

# work 
# import pymongo

# CONNECTION_STRING = 'mongodb+srv://noobmaster69:a1e2i3o4u5@cluster0.pd5jd.gcp.mongodb.net/fooddb?retryWrites=true&w=majority'

# myclient = pymongo.MongoClient(CONNECTION_STRING)

# mydb = myclient["fooddb"]

# mycol = mydb['test']

# for x in mycol.find():
#   print(x)

