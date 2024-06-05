from flask import Blueprint, request, jsonify, json
from backend.config.db import db, app, ma
from backend.models.review import Review, ReviewsSchema

ruta_reviews = Blueprint("ruta_review", __name__)

review_schema = ReviewsSchema()
reviews_schema = ReviewsSchema(many=True)

@ruta_reviews.route('/reviews', methods=['GET'])
def review():
    resultall = Review.query.all() #Select * from review
    resultado_review= reviews_schema.dump(resultall)
    return jsonify(resultado_review)

@ruta_reviews.route('/savereview', methods=['POST'])
def save():
    try:
        description = request.json['description']
        imagen_url = request.json['imagen_url']
        reviewuser = request.json['reviewcategoria']
        new_review = Review(description,imagen_url,reviewuser)

        db.session.add(new_review)
        db.session.commit()

        return jsonify({'status': 'OK', 'message': 'Los datos han sido guardados con éxito'}), 200
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al guardar los datos'}),500

@ruta_reviews.route('/updatereview', methods=['PUT'])
def Update():
    try:
        id = request.json['id']
        description = request.json['description']
        imagen_url = request.json['imagen_url']
        reviewuser = request.json['reviewuser']
        review = Review.query.get(id)
        if review :
            print(review)
            review.id = id
            review.description = description
            review.imagen_url = imagen_url
            review.reviewuser = reviewuser
            db.session.commit()
            return jsonify({'status': 'OK', 'message': 'Datos actualizados con éxito'}), 200
        else:
            return jsonify({'status': 'Error', 'message': 'No se encontró el review con el ID proporcionado'}), 404
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'status': 'Error', 'message': 'Ocurrió un error al actualizar los datos'}), 500

@ruta_reviews.route('/deletereview/<id>', methods=['DELETE'])
def eliminar(id):
    review = Review.query.get(id)
    db.session.delete(review)
    db.session.commit()
    return jsonify(review_schema.dump(review))