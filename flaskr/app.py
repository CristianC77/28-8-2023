from flaskr import create_app
from .modelos import db, Usuario, Album, Medio
from .modelos import AlbumSchema

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

with app.app_context():
    AlbumSchema = AlbumSchema()
    a = Album(titulo='Puebas', anio=2002, description='Hola', medios=Medio.cd)
    db.session.add(a)
    db.session.commit()
    print([Album_Schema.dumps(album) for album in Album.query.all()])