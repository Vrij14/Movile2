from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.user import User, UsersSchema

ruta_users = Blueprint("ruta_user", __name__)

user_schema = UsersSchema()
users_schema = UsersSchema(many=True)

@ruta_users.route('/users', methods=['GET'])
def user():
    resultall = User.query.all() #Select * from user
    resultado_user= users_schema.dump(resultall)
    return jsonify(resultado_user)

@ruta_users.route('/saveuser', methods=['POST'])
def save():
    try:
        name = request.json['name']
        email = request.json['email']
        phone = request.json ['phone']
        passw = request.json ['passw']

        new_user = User(name, email, phone,passw)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}), 500

@ruta_users.route('/verificaruser', methods=['POST'])
def verifica():
    try:
        datos = request.json

        if 'nombreuser' not in datos or 'contrasena' not in datos:
            return jsonify({'status': 'Error', 'message': 'Datos incompletos'})

        name = datos['name']
        passw = datos['passw']

        existe = User.query.filter_by(name=name, passw=passw).first()

        if existe:
            return jsonify({'status': 'OK', 'message': 'El user existe en la base de datos'})
        else:
            return jsonify({'status': 'Error', 'message': 'El user no existe en la base de datos'})

    except Exception as e:
        print(f"Error en la verificación: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error en la verificación'})


@ruta_users.route('/updateuser', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        name = request.json['name']
        email = request.json['email']
        phone = request.json ['phone']
        passw = request.json ['passw']

        user = User.query.get(id)
        if user :
            print(user)
            user.name = name
            user.email = email
            user.phone = phone
            user.passw = passw
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró el user con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_users.route('/deleteuser/<id>', methods=['DELETE'])
def eliminar(id):
    user = User.query.get(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify(user_schema.dump(user))