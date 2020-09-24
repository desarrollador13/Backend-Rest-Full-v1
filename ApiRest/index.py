from flask import Flask, jsonify, request, Response, make_response
from flask_restful import Resource, Api
from Loaders.connectiondb import Connectiondb
from Controller.userController import UserController

class Index(Resource):

	resultController= None

	def __init__(self):
		pass

	def get(self):
		userController= UserController()

		self.resultController= userController.consultarUsuario()
		return make_response(jsonify(self.resultController),self.resultController['code'])

	def post(self):
		userController= UserController()
		jsonBody= request.get_json()
		NombreApp= jsonBody['NombreApp']
		Loguin= jsonBody['Loguin']
		if Loguin == 0:
			self.resultController= userController.guardarUsuarios(jsonBody)
			return make_response(jsonify(self.resultController),self.resultController['code'])
		else:
			self.resultController= userController.loguinUsuario(jsonBody)
			return make_response(jsonify(self.resultController),self.resultController['code'])



#SELECT to_json(result)
#FROM 
#(
#SELECT "NombreApp", "IdRoles", "Clave", "nombreRoll" 
#FROM public."UsuariosApp" us
#INNER JOIN public."Roles" rl ON us."IdRoles" = rl."Id" 
#WHERE "NombreApp"='{0}' 
#) result 
    