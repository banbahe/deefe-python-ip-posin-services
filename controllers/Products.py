from flask_restful import Resource, Api, reqparse

class Products(Resource):
#class Item(Resource):
    # parser = reqparse.RequestParser()
    # parser.add_argument('price',
    #                     type=float,
    #                     required=True,
    #                     help='this field cannot be left blank!')
    def get(self, name):
        return name
