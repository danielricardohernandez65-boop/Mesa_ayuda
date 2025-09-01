from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "mesa_ayuda"
USER = "root"
PASSWORD = ""
HOST = "localhost"

# Credenciales de ADMIN
ADMIN_NAME = "Admin"
ADMIN_EMAIL = "admin@mesaayuda.com"
ADMIN_PASS = "TSzxvDl1nQ"


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "8=F&9w4Z{F"
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # ✅ MOVER las importaciones de modelos AQUÍ (después de db.init_app)
    from .models import Usuario, Rol, Ticket

    @app.errorhandler(404)
    def error_404(error):
        return render_template("error_404.html")

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # ✅ MOVER las importaciones de blueprints AQUÍ
    from .views.view_tec import tecni
    from .views.view_user import user
    from .views.view_admin import admin
    from .controllers.auth import auth

    @login_manager.user_loader
    def load_user(id):
        return Usuario.query.get(int(id))

    app.register_blueprint(user, url_prefix="/")
    app.register_blueprint(tecni, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    app.register_blueprint(admin, url_prefix="/")

    with app.app_context():
        create_database()
        create_initial_roles()
        create_admin()

    return app


def create_database():
    db.create_all()
    print("Base de Datos creada")


def create_initial_roles():
    roles = [
        {"nombre": "administrador"},
        {"nombre": "tecnico"},
        {"nombre": "cliente"},
    ]

    try:
        from .models.rol import Rol

        for rol_data in roles:
            if not Rol.query.filter_by(nombre=rol_data["nombre"]).first():
                rol = Rol(nombre=rol_data["nombre"])
                db.session.add(rol)

        db.session.commit()
        print("Roles iniciales creados")

    except Exception as e:
        db.session.rollback()
        print(f"Error creando roles: {e}")


def create_admin():
    try:
        from .models.rol import Rol
        from .models.user import Usuario

        admin_role = Rol.query.filter_by(nombre="administrador").first()

        if not admin_role:
            print("Error: No existe el rol administrador")
            return

        if Usuario.query.filter_by(rol_id=admin_role.id).first():
            print("Ya existe un administrador, omitiendo creación")
            return

        admin = Usuario(
            username=ADMIN_NAME,
            email=ADMIN_EMAIL,
            password=ADMIN_PASS,
            rol_id=admin_role.id,
        )

        db.session.add(admin)
        db.session.commit()
        print("Admin creado exitosamente")

    except Exception as e:
        db.session.rollback()
        print(f"Fallo al crear admin: {e}")
