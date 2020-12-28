#!/usr/bin/python3

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class WebAPI(Resource):
    def get(self):
        return {
                'Bill': {
                    'quote': ['Love and Basketball']
        },
                'Linus': {
                    'quote': ['Talk is cheap']
                    }
        }


api.add_resource(WebAPI, '/')

if __name__ == '__main__':
    app.run(debug=True)
