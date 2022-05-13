import pymongo
from flask import current_app, g
# from flask.cli import with_appcontext


CONNECTION_STRING = 'mongodb+srv://noobmaster69:a1e2i3o4u5@cluster0.pd5jd.gcp.mongodb.net/fooddb?retryWrites=true&w=majority'

def create_app():
    app = Flask(__name__)

    with app.app_context():
        init_db()

    return app

def get_db():
    if 'db' not in g:
        #g.db = connect_to_database()
        g.db = pymongo.MongoClient(current_app.config[CONNECTION_STRING])


    return g.db


def dummy() -> str:
    print('test')
    return ""


def get_db1():
    try:
        if 'db' not in g:
            #print(dir(g))
            print('\n\n\n\n')
            # g.db = pymongo.MongoClient(current_app.config['DATABASE_HOST'])
            g.db = "save any data"
    except Exception as ex:
        print(ex)
    else:
        print(g)
    #return g.db


def close_db(e=None):
    db = g.pop('db',None)
    if db is not None:
        db.close()

# dummy()
get_db()
# print(dir(g))

#get_db()
#print(g.db)




# myclient = pymongo.MongoClient(CONNECTION_STRING)

# mydb = myclient["fooddb"]

# mycol = mydb['test']

# for x in mycol.find():
#   print(x)















    

# work 
# import pymongo

# CONNECTION_STRING = 'mongodb+srv://noobmaster69:a1e2i3o4u5@cluster0.pd5jd.gcp.mongodb.net/fooddb?retryWrites=true&w=majority'

# myclient = pymongo.MongoClient(CONNECTION_STRING)

# mydb = myclient["fooddb"]

# mycol = mydb['test']

# for x in mycol.find():
#   print(x)

