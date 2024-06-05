from backend.config.db import  db, ma, app

class Bath(db.Model):
    __tablename__ = "tblbath"

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(150))
    adress = db.Column(db.String(50))
    city = db.Column(db.String(50))
    imagen_url = db.Column(db.String(255))
    description = db.Column(db.String(250))
    rating = db.Column(db.Float)
    bathreview = db.Column(db.Integer, db.ForeignKey('tblreview.id'))
    
    def __init__(self,title,adress,city,imagen_url,description,rating,bathreview) :
       self.title = title
       self.adress = adress
       self.city = city
       self.imagen_url = imagen_url
       self.description = description
       self.rating = rating
       self.bathreview = bathreview
       
with app.app_context():
    db.create_all()

class BathsSchema(ma.Schema):
    class Meta:
        fields = ('id','title','adress','city','imagen_url','description','rating', 'bathreview')