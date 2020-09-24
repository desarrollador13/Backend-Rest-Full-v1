from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

class Singleton:
	"""A non-thread-safe helper class to ease implementing singletons. This should be used as a decorator -- not a metaclass
	 -- to the class that should be a singleton.
  The decorated class can define one `__init__` function that takes only the `self` argument. Other than that, there are
  no restrictions that apply to the decorated class.
  To get the singleton instance, use the `Instance` method. Trying to use `__call__` will result in a `TypeError` 
  being raised.
  Limitations: The decorated class cannot be inherited from."""

	def __init__(self, decorated):
		self._decorated = decorated
		
	def Instance(self):
		"""Returns the singleton instance. Upon its first call, it creates a
    new instance of the decorated class and calls its `__init__` method.
    On all subsequent calls, the already created instance is returned."""
		try:
			print('//****Primera unica Instancia****//')
			return self._instance
		except AttributeError as error:
			print('error instancia return instancia=====>>>',error)
			self._instance = self._decorated()
			return self._instance

	def __call__(self):
		raise TypeError('Se debe acceder a los singletons a  través de `Instance ()`.')

	def __instancecheck__(self, inst):
		print('instancia clase*** ',inst, 'clases***',self._decorated)
		return isinstance(inst, self._decorated)

@Singleton
class Connectiondb():
	"""docstring for ClassName"""
	connection= None
	session= None

	def __init__(self):
		pass

	def getConnectiondb(self):
		engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/prueba_app')
		self.connection = engine.connect()
	
		return self.connection

	def getConnectSession(self):
		
		Base = declarative_base()
		engine = create_engine('postgresql+psycopg2://postgres:admin@localhost/prueba_app', echo=True)
		Session = sessionmaker(bind=engine)
		# create db schema
		#Base.metadata.create_all(engine)
		session = Session()

		return session