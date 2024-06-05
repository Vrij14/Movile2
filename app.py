from flask import Flask
from backend.api.menuitem import CategoriaResource
from flask_restful import Api
from backend.config.db import db, ma, app

api = Api(app)

from backend.api.user import User, ruta_users
from backend.api.menuitem import MenuItem, ruta_menuitems
from backend.api.review import Review, ruta_reviews
from backend.api.service import Service, ruta_services
from backend.api.bath import Bath, ruta_baths
from backend.api.reserva import Reserva, ruta_reservas

app.register_blueprint(ruta_users, url_prefix='/api')
app.register_blueprint(ruta_menuitems, url_prefix='/api')
app.register_blueprint(ruta_reviews, url_prefix='/api')
app.register_blueprint(ruta_services, url_prefix='/api')
app.register_blueprint(ruta_baths, url_prefix='/api')
app.register_blueprint(ruta_reservas, url_prefix='/api')
api.add_resource(CategoriaResource, '/categorias')

@app.route('/')
def index():
    return "Hola Mundo"

if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
