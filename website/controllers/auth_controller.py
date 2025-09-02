
from website.models import Usuario

from website import db

# from flask_login import current_user, login_user, logout_user, login_required
class AuthController:
    @staticmethod
    def crear_usuario(username, email, password):
        # Validaciones
        if Usuario.query.filter_by(email=email).first():
            raise Exception("El email ya está registrado")

        if Usuario.query.filter_by(username=username).first():
            raise Exception("El nombre de usuario ya existe")

        # Crear usuario
        nuevo_usuario = Usuario(
            username=username,
            email=email,
            password=password,
        )

        db.session.add(nuevo_usuario)
        db.session.commit()

        return nuevo_usuario

    @staticmethod
    def autenticar_usuario(email, password):
        usuario = Usuario.query.filter_by(email=email).first()

        if not usuario:
            raise Exception("Usuario no encontrado")

        if not usuario.verify_password(password):
            raise Exception("Contraseña incorrecta")

        return usuario
