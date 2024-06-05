from backend.config.db import  db, ma, app

class MenuItem(db.Model):
    __tablename__ = "tblmenuitem"

    id = db.Column(db.Integer, primary_key =True)
    title = db.Column(db.String(150))
    icon_url = db.Column(db.String(255))

    def __init__(self, title,icon_url) :
       self.title = title
       self.icon_url = icon_url

with app.app_context():
    db.create_all()

class MenuItemsSchema(ma.Schema):
    class Meta:
        fields = ('id','title','icon_url')