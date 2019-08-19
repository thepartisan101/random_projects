from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask.ext.jsonpify import jsonify

db_connect = create_engine('sqlite:///chinnok.db')
app = Flask(__name__)
api = Api(app)

class Employees(Resource):
    def get(self):
        conn = db_connect.connect() #Connect to database
        query = conn.execute("select * from employees") # Perfroms a query and return json results
        return {'employees': [i[0] for i in query.cursor.fetchall()]} # Fetches 1st collumn, the Employee ID

class Tracks(Resource):
    def get(self):
        conn = db_connnect.connect()
        query = conn.execute("select trackid, name composer, unitprice from tracks;")
        result = {'data': [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return jsonify(result)
