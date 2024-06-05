from backend.config.db import  db, ma, app

class Review(db.Model):
    __tablename__ = "tblreview"

    id = db.Column(db.Integer, primary_key =True)
    description = db.Column(db.String(500))
    imagen_url = db.Column(db.String(255))
    reviewuser = db.Column(db.Integer, db.ForeignKey('tbluser.id'))

    def __init__(self,description,imagen_url,reviewuser) :
       self.description = description
       self.imagen_url = imagen_url
       self.reviewuser = reviewuser

with app.app_context():
    db.create_all()

class ReviewsSchema(ma.Schema):
    class Meta:
        fields = ('id','description','imagen_url','reviewuser')