from backend.config.db import  db, ma, app

class User(db.Model):
    __tablename__ = "tbluser"

    id = db.Column(db.Integer, primary_key =True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    passw = db.Column(db.String(150))

    def __init__(self, name, email, phone,passw) :
       self.name = name
       self.email = email
       self.phone = phone
       self.passw = passw

with app.app_context():
    db.create_all()

class UsersSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email','phone','passw')