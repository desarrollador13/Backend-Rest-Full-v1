import bcrypt
import jwt
from flask import Flask, jsonify, request, Response, make_response
from DAO.userDAO import UserDAO

class UserController:

	resultDao= []

	def __init__(self):
		pass

	def consultarUsuario(self,NombreApp=''):
		results= []
		userDAO= UserDAO()
		try:
			self.resultDao = []
			self.resultDao = userDAO.consultUsuarios(NombreApp)
			if len(self.resultDao) == 0:
				return  { 'code': 200, 'msg': 'contenido existente' }
			if self.resultDao[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }

			for row_number, row in enumerate(self.resultDao):
				results.append({})
				for column_number, value in enumerate(row):
					results[row_number][row.keys()[column_number]] = value
			return { 'code': 200, 'msg': 'Error servidor', 'rows': results }

		except Exception as error:
			print('error->UserController->consultarUsuario()', error)	
			return { 'code': 500, 'msg': 'Error servidor', 'rows': [] }

	def guardarUsuarios(self, paramsBody):
		userDAO= UserDAO()
		try:
			self.resultDao = []
			result= []
			resRegis= []
			results= []
			NombreApp= paramsBody['NombreApp']
			contrasena = paramsBody['Clave']

			result = userDAO.validarUsuarios(NombreApp)
			if len(result) > 0:
				if result[0] == 500:
					return { 'code': 500, 'msg': 'Error servidor' }
				else:
					return { 'code': 201, 'msg': 'El recurso ya existe' }
			nContrasena= self.encryptarContrasena(contrasena)

			resRegis= userDAO.registrarUsuarios(paramsBody,nContrasena)
			if isinstance(resRegis,list) > 0:
				if resRegis[0] == 500:
					return{ 'code': 500, 'msg': 'Verifique los datos vuelva intentar' }

			resUsuario= userDAO.consultUsuarios(NombreApp)
			for row_number, row in enumerate(resUsuario):
				results.append({})
				for column_number, value in enumerate(row):
					results[row_number][row.keys()[column_number]] = value
			compare= self.compareContrasena(contrasena,results[0]['Clave'])
			if compare == False:
				return { 'code': 200 , 'msg': 'Error de autenticación loguin' }

			token= jwt.encode(results[0],'rest-api-v1',algorithm='HS256')
			return {'code':'201', 'msg':'recurso creado', 'token':token.decode('utf-8')}

		except Exception as error:
			print('error->UserController->guardarUsuarios()*', error)	
			return { 'code': 500, 'msg': 'Error servidor', 'token': '' }	

	def loguinUsuario(self, paramsBody):
		userDAO= UserDAO()
		try:
			self.resultDao = []
			resUsuario= []
			results= []

			NombreApp= paramsBody['NombreApp']
			contrasena = paramsBody['Clave']
			resUsuario= userDAO.consultUsuarios(NombreApp)
			
			if len(resUsuario) == 0:
				return { 'code': 200, 'msg': 'el usuario no existe para ingresar registrar usuario' }
			if resUsuario[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }

			for row_number, row in enumerate(resUsuario):
				results.append({})
				for column_number, value in enumerate(row):
					results[row_number][row.keys()[column_number]] = value
			
			compare= self.compareContrasena(contrasena,results[0]['Clave'])
			if compare == False:
				return { 'code': 200 , 'msg': 'Error de autenticación loguin' }

			token= jwt.encode(results[0],'rest-api-v1',algorithm='HS256')
			return {'code':'200', 'msg':'proceso exitoso', 'token':token.decode('utf-8')}

		except Exception as error:
			print('error->UserController->loguinUsuario()', error)	
			return { 'code': 500, 'msg': 'Error servidor', 'token': '' }

	def encryptarContrasena(self, contrasena):

		hasContrasena = bcrypt.hashpw(contrasena.encode('utf-8'), bcrypt.gensalt(10))
		return hasContrasena.decode('utf-8')
		# hasContrasena= bcrypt.hashpw(contrasena.encode('utf8'), bcrypt.gensalt())
		# return hasContrasena

	def compareContrasena(self, password, hashedPassword):
		#bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))
		compare= bcrypt.checkpw(password.encode('utf-8'), hashedPassword.encode('utf-8'))
		#compare= bcrypt.checkpw(password.encode('utf8'), hashedPassword)
		return compare