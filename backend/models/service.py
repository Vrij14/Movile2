from backend.config.db import  db, ma, app

class Service(db.Model):
    __tablename__ = "tblservice"

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(250))
    imagen_url = db.Column(db.String(255))
    price = db.Column(db.Double)
    
    def __init__(self, title,description,imagen_url,price) :
       self.title = title
       self.description = description
       self.imagen_url = imagen_url
       self.price = price
       
with app.app_context():
    db.create_all()

class ServicesSchema(ma.Schema):
    class Meta:
        fields = ('id','title','description','imagen_url','price')