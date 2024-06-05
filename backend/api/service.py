from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.service import Service, ServicesSchema

ruta_services = Blueprint("ruta_service", __name__)

service_schema = ServicesSchema()
services_schema = ServicesSchema(many=True)

@ruta_services.route('/services', methods=['GET'])
def service():
    resultall = Service.query.all() #Select * from service
    resultado_service= services_schema.dump(resultall)
    return jsonify(resultado_service)

@ruta_services.route('/saveservice', methods=['POST'])
def save():
    try:
        title = request.json['titulo']
        description = request.json['descripcion']
        imagen_url = request.json ['imagen_url']
        price = request.json ['price']
        new_service = Service(title,description,imagen_url,price)

        db.session.add(new_service)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}),500

@ruta_services.route('/updateservice', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        title = request.json['title']
        description = request.json['description']
        imagen_url = request.json ['imagen_url']
        price = request.json['price']
        service = Service.query.get(id)
        if service :
            print(service)
            service.title = title
            service.description = description
            service.imagen_url = imagen_url
            service.price = price
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró la service con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_services.route('/deleteservice/<id>', methods=['DELETE'])
def eliminar(id):
    service = Service.query.get(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify(service_schema.dump(service))