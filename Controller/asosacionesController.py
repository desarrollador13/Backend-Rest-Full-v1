from DAO.asociacionesDAO import AsociacionesDAO
from flask import Flask, jsonify, request, Response, make_response

class AsosacionesController:

	resursoContr= []
	asociacionesDAO = AsociacionesDAO()
	def __init__(self):
		pass

	def consultarAsosaciones(self):
		results= []
		try:
			self.resursoContr=  self.asociacionesDAO.consultarAsosaciones()
			
			if len(self.resursoContr) == 0:
				return  { 'code': 200, 'msg': 'no hay registros guardados', 'rows': [] }
			if self.resursoContr[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor', 'rows': []}
			for row_number, row in enumerate(self.resursoContr):
				results.append({})
				for column_number, value in enumerate(row):
					results[row_number][row.keys()[column_number]] = value
			return {'code': 200, 'msg': 'proceso exitoso', 'rows': results}
		except Exception as error:
			print('error->RecursosController->consultarAsosaciones()', error)	
			return { 'code': 500, 'msg': 'Error servidor', 'rows': [] }

	def registrarAsosaciones(self,paramsBody):
		results= []
		try:
			Title= paramsBody['Title']
			Number = paramsBody['Number']
			validarDatos=  self.asociacionesDAO.consultarAsosacion(Title,Number)
			
			if len(validarDatos) > 0:
				if validarDatos[0] == 500:
					return { 'code': 500, 'msg': 'Error servidor' }
				return  { 'code': 200, 'msg': 'el recurso ya existe' }
			

			self.resursoContr= self.asociacionesDAO.registrarAsosaciones(paramsBody)
			if self.resursoContr[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }
			return { 'code': 201, 'msg': 'recurso creado' }

		except Exception as error:
			print('error->AsosacionesController->registrarAsosaciones()', error)	
			return { 'code': 500, 'msg': 'Error servidor' }

	def eliminarAsosaciones(self,id):
		try:
			consultId= self.asociacionesDAO.consultarId(id)
			if len(consultId) == 0:
				return  { 'code': 200, 'msg': 'el dato a eliminar no existe' }
			if consultId[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }

			self.resursoContr=  self.asociacionesDAO.eliminarAsosaciones(id)
			if self.resursoContr[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }
			return { 'code': 200, 'msg': 'recurso eliminado' }

		except Exception as error:
			print('error->AsosacionesController->registrarAsosaciones()', error)	
			return { 'code': 500, 'msg': 'Error servidor' }

	def actualizarAsosaciones(self,id,paramsBody):
		try:
			Title= paramsBody['Title']
			Number = paramsBody['Number']
			validarDatos=  self.asociacionesDAO.consultarId(id)
			
			print(validarDatos,'kkk')
			if len(validarDatos) == 0:
				return  { 'code': 200, 'msg': 'el recurso no existe' }
			if validarDatos[0] == 500:
					return { 'code': 500, 'msg': 'Error servidor' }
			

			self.resursoContr= self.asociacionesDAO.actualizarAsosaciones(paramsBody,id)
			if self.resursoContr[0] == 500:
				return { 'code': 500, 'msg': 'Error servidor' }
			return { 'code': 200, 'msg': 'recurso actualizado' }

		except Exception as error:
			print('error->AsosacionesController->actualizarAsosaciones()', error)	
			return { 'code': 500, 'msg': 'Error servidor' }
