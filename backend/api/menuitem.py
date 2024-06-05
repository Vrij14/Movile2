from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.menuitem import MenuItem, MenuItemsSchema

ruta_menuitems = Blueprint("ruta_menuitem", __name__)

menuitem_schema = MenuItemsSchema()
menuitems_schema = MenuItemsSchema(many=True)

@ruta_menuitems.route('/menuitems', methods=['GET'])
def menuitem():
    resultall = MenuItem.query.all() #Select * from MenuItems
    resultado_menuitem= menuitems_schema.dump(resultall)
    return jsonify(resultado_menuitem)

@ruta_menuitems.route('/savemenuitem', methods=['POST'])
def save():
    try:
        title = request.json['title']
        icon_url = request.json['icon_url']
        new_menuitem = MenuItem(title=title, icon_url=icon_url)
        db.session.add(new_menuitem)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}),500

@ruta_menuitems.route('/updatemenuitem', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        title = request.json['title']
        icon_url = request.json['icon_url']
        menuitem = MenuItem.query.get(id)
        if menuitem :
            print(menuitem)
            menuitem.title = title
            menuitem.icon_url = icon_url
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró la categoría con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_menuitems.route('/deletemenuitem/<id>', methods=['DELETE'])
def eliminar(id):
    menuitem = MenuItem.query.get(id)
    db.session.delete(menuitem)
    db.session.commit()
    return {'message': 'Categoría eliminada con éxito'}, 200