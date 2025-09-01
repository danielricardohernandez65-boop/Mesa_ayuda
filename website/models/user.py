from website import db
from flask_login import UserMixin
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    username = db.Column(db.String(100))
    password_hash = db.Column(db.String(255))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    rol_id = db.Column(db.Integer, db.ForeignKey("rol.id"), nullable=False, default=3)

    @property
    def password(self):
        raise AttributeError("Clave no se puede leer")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password=password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password=password)

    def __repr__(self):
        return f"<Usuario {self.username}>"


def iniciar_relaciones():
    #from .ticket import Ticket

    tickets_creados = db.relationship(  # noqa: F841
        "Ticket",
        foreign_keys="Ticket.usuario_id",
        backref="cliente",
        lazy=True,
        cascade="all, delete-orphan",
    )

    tickets_asignados = db.relationship( # noqa: F841
        "Ticket", foreign_keys="Ticket.tecnico_id", backref="tecnico", lazy=True
    )
