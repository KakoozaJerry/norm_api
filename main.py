from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast
import sys
import date, ranges, lugandatime, currency, phonenumber, measurement, abbreviations, ordinals, cardinals, cardinals_orig, detection


app = Flask(__name__)
api = Api(app)


class Users(Resource):
    # methods go here
    def get(self):
        data = pd.read_csv('abbreviations.csv')  # read CSV
        data = data.to_dict()  # convert dataframe to dictionary
        return {'data': data}, 200  # return data and 200 OK code
    
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('sentence', required=True)  # add args
        
        args = parser.parse_args()  # parse arguments to dictionary
        text = args['sentence']
        norm_word = detection.start(isFile=False,g=text)
        
        return {'text': norm_word }, 200  # return data with 200 OK

class Locations(Resource):
    # methods go here
    pass

api.add_resource(Users, '/luganda')  # '/luganda' is our entry point
api.add_resource(Locations, '/locations')  # and '/locations' is our entry point for Locations


if __name__ == "__main__":
  app.run()
