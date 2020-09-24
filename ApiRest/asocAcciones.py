from flask_restful import Resource, Api
from flask import Flask, jsonify, request, Response, make_response
import jwt
from DAO.userDAO import UserDAO
from Middelware.authJwt import tokenRequired
from Controller.asosacionesController import AsosacionesController

class AsocAcciones(Resource):

	def __init__(self):
		pass
	
	@tokenRequired
	def delete(self,current_user,id):
		asosacionesControl= AsosacionesController()
		bearerHeader = request.headers.get('authorization')
		resControl= asosacionesControl.eliminarAsosaciones(id)
		return make_response(jsonify(resControl),resControl['code'])

	@tokenRequired
	def put(self, current_user, id):
		asosacionesControl= AsosacionesController()
		bearerHeader = request.headers.get('authorization')
		jsonBody= request.get_json()
		resControl= asosacionesControl.actualizarAsosaciones(id,jsonBody)
		return make_response(jsonify(resControl),resControl['code'])
