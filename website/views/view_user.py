from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user
from website.models import Usuario

from website.controllers.auth import AuthController


user = Blueprint("user", __name__)

@user.route("/")
def home():
    
    return render_template("index.html")


@user.route("/sing-up", methods=["GET", "POST"])
def sing_up():
    if request.method == "POST":
        try:
            username = request.form.get("nombre")
            email = request.form.get("email")
            password = request.form.get("clave")

            AuthController.crear_usuario(username, email, password)

            flash("Cuenta creada exitosamente. Puedes iniciar sesión", "success")
            return redirect(url_for("user.login"))

        except Exception as e:
            flash(f"Error al crear cuenta: {e}", "error")

    return render_template("register.html")


@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            email = request.form.get("email")
            password = request.form.get("clave")

            print(f"Email: {email}")


            
            usuario = AuthController.autenticar_usuario(email, password)

            login_user(usuario)
            print("Inicio de sesion correcto")
            
            flash("Inicio de sesión exitoso", "success")
            return redirect("/")

        except Exception as e:
            print(f"Error en iniciar sesión: {e}")

            flash(f"Error al iniciar sesión: {e}", "error")

    return render_template("login.html")
