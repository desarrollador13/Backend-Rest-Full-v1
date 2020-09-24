from Model.asociacionesModel import AsociacionesModel
from Loaders.connectiondb import Connectiondb

class AsociacionesDAO:

	asociacionesDao= []
	#recursosModel = RecursosModel()
	def __init__(self):
		pass

	def consultarAsosaciones(self):
		self.asociacionesDao= []
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query='''SELECT "Id", "State", "Number", "Title", "Created"
									 FROM public."Tabla1" '''
			self.asociacionesDao=db.execute(sql_query).fetchall()
			return self.asociacionesDao
	
		except Exception as error:
			print('error->AsociacionesDAO->consultarAsosaciones', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao

	def consultarAsosacion(self,params1,params2):
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query='''SELECT "Id", "State", "Number", "Title", "Created"
									 FROM public."Tabla1"
									 WHERE "Title"='{0}' AND "Number"= '{1}' '''.format(params1,params2)
			result=db.execute(sql_query).fetchall()
			return result

		except Exception as error:
			print('error->AsociacionesDAO->consultarAsosacion', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao

	def registrarAsosaciones(self,colums):
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb() #"Created", 
			sql_query='''INSERT INTO public."Tabla1" 
									("State", "Number", "Title") VALUES
									('{0}','{1}','{2}') '''.\
									format(colums['State'],colums['Number'],\
									colums['Title'])
			result=db.execute(sql_query)
			self.asociacionesDao= [200]
			return self.asociacionesDao

		except Exception as error:
			print('error->AsociacionesDAO->registrarAsosaciones', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao

	def eliminarAsosaciones(self,id):
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query='''DELETE FROM public."Tabla1" WHERE "Id"='{0}' '''.format(id)
			result=db.execute(sql_query)
			self.asociacionesDao= [200]
			return self.asociacionesDao

		except Exception as error:
			print('error->AsociacionesDAO->registrarAsosaciones', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao

	def actualizarAsosaciones(self,colums,id):
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query= '''UPDATE public."Tabla1" SET "State"='{0}', "Number"='{1}', "Title"='{2}' WHERE "Id"='{3}' '''.\
			format(colums['State'],colums['Number'],colums['Title'],id)
			result=db.execute(sql_query)
			self.asociacionesDao= [200]
			return self.asociacionesDao

		except Exception as error:
			print('error->AsociacionesDAO->actualizarAsosacionesooo', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao

	def consultarId(self,id):
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query='''SELECT "Id", "State", "Number", "Title", "Created"
									 FROM public."Tabla1"
									 WHERE "Id"='{0}' '''.format(id)
			result=db.execute(sql_query).fetchall()
			return result

		except Exception as error:
			print('error->AsociacionesDAO->consultarId', error)	
			self.asociacionesDao= [500]
			return self.asociacionesDao


