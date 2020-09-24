from flask import Flask, jsonify, request, Response
from flask_restful import Resource, Api
from ApiRest.index import Index
from ApiRest.asociaciones import Asosaciones
from ApiRest.asocAcciones import AsocAcciones
from Middelware.authJwt import tokenRequired
from functools import wraps
from flask_cors import CORS


#app.secret_key = 'myawesomesecretkey'
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.before_request
def before_request():
  print('-------*endpoint: %s, url: %s, path: %s' % (
  request.endpoint,
  request.url,
  request.path),'*------')

api.add_resource(Index, '/api/v1/usuario/')
api.add_resource(Asosaciones, '/api/v1/asosaciones/')
api.add_resource(AsocAcciones, '/api/v1/asosaciones/<id>/')

# @app.route('/index/', methods=['GET'])
# def index():
# 	jsonRes = jsonify({'id':1, 'name':'Jonathan Pinto'})
# 	return jsonRes

if __name__ == '__main__':
	app.run(debug=True)