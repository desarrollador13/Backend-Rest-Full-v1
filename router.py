from app import *


@app.route('/index/', methods=['GET'])
def index():

	data = []
	jsonRes = jsonify({'id':1, 'name':'Jonathan Pinto'})
	jsonRes.status_code = 201
	data.append(jsonRes)
	return data