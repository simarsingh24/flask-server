from flask import request, redirect, url_for,jsonify
from app import app, db
from app.models import Model
from app.schemas import *

@app.route('/')
def home():
	return "home"

@app.route('/model' , methods=['POST', 'GET'])
def model():
	if request.method == 'POST':
		name = request.json["name"]
		new_model = Model(name)
		db.session.add(new_model)
		db.session.commit()
		return model_schema.jsonify(new_model)	
	if request.method == 'GET' :
		all_model = Model.query.all()
		result = models_schema.dump(all_model)
		return jsonify(result.data)

@app.route('/model/<id>')
def model_detail(id):
    model = Model.query.get(id)
    return model_schema.jsonify(model)

   