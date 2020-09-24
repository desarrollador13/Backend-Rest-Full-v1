from flask_restful import Resource, Api
from flask import Flask, jsonify, request, Response, make_response
import jwt
from DAO.userDAO import UserDAO
from Middelware.authJwt import tokenRequired
from Controller.asosacionesController import AsosacionesController

class  Asosaciones(Resource):
	
	def __init__(self):
		pass

	@tokenRequired
	def get(self,current_user):
		asosacionesControl= AsosacionesController()
		bearerHeader = request.headers.get('authorization')
		resControl= asosacionesControl.consultarAsosaciones()
		return make_response(jsonify(resControl),resControl['code'])

	@tokenRequired
	def post(self,current_user):
		asosacionesControl= AsosacionesController()
		bearerHeader = request.headers.get('authorization')
		jsonBody= request.get_json()
		resControl= asosacionesControl.registrarAsosaciones(jsonBody)
		return make_response(jsonify(resControl),resControl['code'])
