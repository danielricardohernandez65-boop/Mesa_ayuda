from website import db


class Rol(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(150), unique=True, nullable=False)


    usuarios = db.relationship(
        'Usuario', 
        foreign_keys='Usuario.rol_id',
        backref='rol', 
        lazy=True,
        cascade='all, delete-orphan'
    )

    def __str__(self):
        return "<Rol %r>" % Rol.id
