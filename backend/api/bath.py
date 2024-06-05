from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.bath import Bath, BathsSchema

ruta_baths = Blueprint("ruta_bath", __name__)

bath_schema = BathsSchema()
baths_schema = BathsSchema(many=True)

@ruta_baths.route('/baths', methods=['GET'])
def bath():
    resultall = Bath.query.all() #Select * from bath
    resultado_bath= baths_schema.dump(resultall)
    return jsonify(resultado_bath)       

@ruta_baths.route('/savebath', methods=['POST'])
def save():
    try:
        title = request.json['title']
        adress = request.json['adress']
        city = request.json['city']
        imagen_url = request.json['imagen_url']
        description = request.json['description']
        rating = request.json['rating']
        bathreview = request.json['bathreview']
        new_bath = Bath(title,adress,city,imagen_url,description,rating,bathreview)
        db.session.add(new_bath)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}),500

@ruta_baths.route('/updatebath', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        title = request.json['title']
        adress = request.json['adress']
        city = request.json['city']
        imagen_url = request.json['imagen_url']
        description = request.json['description']
        rating = request.json['rating']
        bathreview = request.json['bathreview']
        bath = Bath.query.get(id)
        if bath :
            print(bath)
            bath.title = title
            bath.adress = adress
            bath.city = city
            bath.imagen_url = imagen_url
            bath.description = description
            bath.rating = rating
            bath.bathreview = bathreview
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró el bath con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_baths.route('/deletebath/<id>', methods=['DELETE'])
def eliminar(id):
    bath = Bath.query.get(id)
    db.session.delete(bath)
    db.session.commit()
    return jsonify(bath_schema.dump(bath))