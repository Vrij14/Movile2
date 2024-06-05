from backend.config.db import  db, ma, app

class Reserva(db.Model):
    __tablename__ = "tblreserva"

    id = db.Column(db.Integer, primary_key =True)
    email = db.Column(db.String(50))
    pService = db.Column(db.String(50))
    fecha = db.Column(db.String(50))
    hora = db.Column(db.String(50))
    nombre = db.Column(db.String(150))
    phone = db.Column(db.String(50))
    mPago = db.Column(db.String(50))
    reservabath = db.Column(db.Integer, db.ForeignKey('tblbath.id'))
    reservaservice = db.Column(db.Integer, db.ForeignKey('tblservice.id'))
    
    def __init__(self,email,pService,fecha,hora,nombre,phone,mPago,reservabath,reservaservice) :
       self.email = email
       self.pService = pService
       self.fecha = fecha
       self.hora = hora
       self.nombre = nombre
       self.phone = phone
       self.mPago = mPago
       self.reservabath = reservabath
       self.reservabath = reservaservice
       
with app.app_context():
    db.create_all()

class ReservasSchema(ma.Schema):
    class Meta:
        fields = ('id','email','pService','fecha','hora','nombre','phone','mPago','reservabath','reservaservice')