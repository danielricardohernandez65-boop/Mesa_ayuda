from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import  login_user
from website.models import Usuario

from website import db


user = Blueprint("user", __name__)



@user.route("/sing-up", methods=["GET", "POST"])
def sing_up():
    if request.method == "POST":
        username = request.form.get("nombre")
        email = request.form.get("email")
        password = request.form.get("clave")

        new_user: Usuario = Usuario()
        new_user.username = username
        new_user.email = email
        new_user.password = password

        try:
            db.session.add(new_user)
            db.session.commit()
            flash("Cuenta creada exitosamente, Puedes inicar sesión")
            return redirect(url_for("auth.login"))
        except Exception as e:
            db.session.rollback()
            flash(f"Fallo creación de cuenta: {e}")

    return render_template("nuevo.html")


@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("clave")

        customer = Usuario.query.filter_by(email=email).first()

        if customer:
            if customer.verify_password(password=password):
                flash("Bienvenido")
                login_user(customer)
                return redirect("/")
            else:
                flash("Contraseña incorrecta")

        else:
            flash("El usaurio no existe, crea una cuenta")

    return render_template("ingresar.html")