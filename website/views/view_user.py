from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from website.controllers.ticket_controller import TicketController


from website.controllers.auth_controller import AuthController


user = Blueprint("user", __name__)


@user.route("/")
def home():
    return render_template("home.html")


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


@user.route("/logout", methods=["GET", "POST"])
@login_required
def log_out():
    logout_user()
    return redirect("/")


@user.route("/ticktes")
@login_required
def ticktes_user():
    try:
        ticktes_user=  TicketController.ver_tickets(usuario_id=current_user.id)

        numero_estados = TicketController.estados_tickets(usuario_id=current_user.id)

    except Exception as e:
        flash(f"Error al crear cuenta: {e}", "error")

    return render_template("ticktes_user.html", ticktes=ticktes_user, estados=numero_estados )


@user.route("/crear_ticket", methods=["GET", "POST"])
@login_required
def crear_ticket():
    if request.method == "POST":
        try:
            titulo = request.form.get("titulo")
            descripcion = request.form.get("descripcion")

            TicketController.crear_ticket(
                titulo=titulo, descripcion=descripcion, usuario_id=current_user.id
            )

            flash("Ticket creado exitosamente", "success")
            return redirect("/ticktes")

        except Exception as e:
            flash(f"Error al crear cuenta: {e}", "error")
