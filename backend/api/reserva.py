from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.reserva import Reserva, ReservasSchema

ruta_reservas = Blueprint("ruta_reserva", __name__)

reserva_schema = ReservasSchema()
reservas_schema = ReservasSchema(many=True)

@ruta_reservas.route('/reservas', methods=['GET'])
def reserva():
    resultall = Reserva.query.all() #Select * from reserva
    resultado_reserva= reservas_schema.dump(resultall)
    return jsonify(resultado_reserva)       

@ruta_reservas.route('/savereserva', methods=['POST'])
def save():
    try:
        email = request.json['email']
        pService = request.json['pService']
        fecha = request.json['fecha']
        hora = request.json['hora']
        nombre = request.json['nombre']
        phone = request.json['phone']
        mPago = request.json['mPago']
        reservabath = request.json['reservabath']
        reservaservice = request.json['reservaservice']
        new_reserva = Reserva(email,pService,fecha,hora,nombre,phone,mPago,reservabath,reservaservice)
        db.session.add(new_reserva)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}),500

@ruta_reservas.route('/updatereserva', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        email = request.json['email']
        pService = request.json['pService']
        fecha = request.json['fecha']
        hora = request.json['hora']
        nombre = request.json['nombre']
        phone = request.json['phone']
        mPago = request.json['mPago']
        reservabath = request.json['reservabath']
        reservaservice = request.json['reservaservice']
        reserva = Reserva.query.get(id)
        if reserva :
            print(reserva)
            reserva.email = email
            reserva.pService = pService
            reserva.fecha = fecha
            reserva.hora = hora
            reserva.nombre = nombre
            reserva.phone = phone
            reserva.mPago = mPago
            reserva.reservabath = reservabath
            reserva.reservaservice = reservaservice
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró el reserva con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_reservas.route('/deletereserva/<id>', methods=['DELETE'])
def eliminar(id):
    reserva = Reserva.query.get(id)
    db.session.delete(reserva)
    db.session.commit()
    return jsonify(reserva_schema.dump(reserva))