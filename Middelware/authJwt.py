from flask_restful import Resource, Api
from flask import Flask, jsonify, request, Response, make_response
import jwt
from DAO.userDAO import UserDAO
from functools import wraps

def tokenRequired(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		res= validarToken()
		if not res.get('user'):
			return make_response(jsonify({'code':res.get('code'), 'msg':res.get('msg')}), res.get('code')) 
		return f(res.get('user'),*args, **kwargs)
	return decorated

def validarToken():
	try:
		userDAO= UserDAO()
		results= []
		bearerHeader = request.headers.get('authorization')
		if not bearerHeader or 'Bearer ' not in bearerHeader:
			return {'code':400, 'msg':'requiere authorization headers'}
		split= bearerHeader.split(' ')

		if not len(split) == 2:
			return {'code':400, 'msg':'requiere authorization headers'}

		decodeData= jwt.decode(split[1],'rest-api-v1')
		resUsuario= userDAO.consultUsuarios(decodeData['NombreApp'])

		if len(resUsuario) == 0:
			return {'code':200, 'msg': 'token invalido usuario' }
		if resUsuario[0] == 500:
			return {'code':500, 'msg': 'token invalido' }
		
		for row_number, row in enumerate(resUsuario):
			results.append({})
			for column_number, value in enumerate(row):
				results[row_number][row.keys()[column_number]] = value

		return {'user':results}

	except Exception as error:
		print('error->Procesos->get()', error)	
		return {'code':500, 'msg': 'Error token invalido', 'token': 'token invalido'}