from Loaders.connectiondb import Connectiondb
from Model.usuariosAppModel import UsuariosAppModel
from Model.rolesModel import RolesModel
class UserDAO:
	"""docstring for ClassName"""
	resModel = []
	def __init__(self):
		pass

	def consultUsuarios(self, NombreApp=''):
		if NombreApp=='':
		 	params= 'Applicacion1'
		else:
			params= NombreApp
		results= []
		try:
			#connectiondb = Connectiondb()
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			#db = connectiondb.getConnectiondb()

			sql_query='''SELECT "NombreApp", "IdRoles", "Clave", "nombreRoll" 
									 FROM public."UsuariosApp" us
									 INNER JOIN public."Roles" rl ON us."IdRoles" = rl."Id" 
									 WHERE "NombreApp"='{0}' '''.format(params)
			result=db.execute(sql_query).fetchall()
			return result

		except Exception as error:
			print('error->UserDao->consultUsuarios()', error)	
			results= [500]
			return results		

	def validarUsuarios(self, paramsValidar=''):
		params= ''
		if paramsValidar=='':
		 	params= 'Applicacion2'
		else:
			params= paramsValidar
		try:
			instan= Connectiondb.Instance()
			db= instan.getConnectiondb()
			sql_query='''SELECT "NombreApp", "IdRoles", "Clave", "nombreRoll" 
									 FROM public."UsuariosApp" us
									 INNER JOIN public."Roles" rl ON us."IdRoles" = rl."Id" 
									 WHERE "NombreApp"='{0}' '''.format(params)
			result=db.execute(sql_query).fetchall()
			return result
		except Exception  as error:

			print('error->UserDao->validarUsuarios()', error)	
			results= [500]
			return results		
	
	def consUsuariosOrm(self, parametroUsuario):
		try:
			kwargs = {'NombreApp': parametroUsuario}
			print('parametroUsuario',kwargs)
			self.resModel= []
			instan= Connectiondb.Instance()
			session= instan.getConnectSession()
			self.resModel= session.query(UsuariosAppModel.NombreApp, UsuariosAppModel.Correo,\
			UsuariosAppModel.IdRoles, UsuariosAppModel.Clave, RolesModel.nombreRoll).\
			join(UsuariosAppModel, UsuariosAppModel.IdRoles == RolesModel.Id)
			# .\
			# filter_by(UsuariosAppModel.NombreApp =)
			return self.resModel

		except Exception as error:
			print('error->UserDao->consUsuariosOrm', error)	
			self.resModel= [500]
			return self.resModel

	def registrarUsuarios(self, paramsGuardar, claveusuario):
		try:
			self.resModel= []
			instan= Connectiondb.Instance()
			session= instan.getConnectSession()
			usuario = UsuariosAppModel(NombreApp=paramsGuardar['NombreApp'],
																 Correo=paramsGuardar['Correo'],
																 IdRoles=paramsGuardar['IdRoles'],
																 Clave=claveusuario)
			session.add(usuario)
			self.resModel = session.commit()
			return self.resModel

		except Exception as error:
			print('error->UserDao->registrarUsuarios', error)	
			self.resModel= [500]
			return self.resModel
