from flask import Blueprint, flash, redirect, render_template, request
from flask_login import login_required, current_user

from website.controllers.admin_controller import AdminController


admin = Blueprint("admin", __name__)


@admin.route("/adminvista")
@login_required
def admin_panel():
    if current_user.rol_id != 1:
        return redirect("/")

    tickets = []
    clientes = []
    tecnicos = []

    try:
        tickets = AdminController.ver_todos_tickets()
        clientes = AdminController.ver_todos_clientes()
        tecnicos = AdminController.ver_todos_tecnicos()

    except Exception as e:
        flash(f"Error: {e}", "error")

    return render_template(
        "admin.html", tickets=tickets, clientes=clientes, tecnicos=tecnicos
    )


@admin.route("/crear-tecnico", methods=["GET", "POST"])
@login_required
def crear_tecnico():
    if current_user.rol_id != 1:
        return redirect("/")
    if request.method == "POST":
        try:
            username = request.form.get("nombre")
            email = request.form.get("email")
            password = request.form.get("clave")

            AdminController.crear_tecnico(username, email, password)

            flash("Técnico creado correctamente", "success")
            return redirect("/adminvista")

        except Exception as e:
            flash(f"Error al crear cuenta: {e}", "error")
            return redirect("/adminvista")


@admin.route("/asignar-tecnico", methods=["POST"])
@login_required
def asignar_tecnico():
    if current_user.rol_id != 1:
        return redirect("/")
    if request.method == "POST":
        try:
            ticket_id = request.form.get("ticket_id")
            tecnico_id = request.form.get("tecnico_id")
            prioridad = request.form.get("prioridad")
            estado = request.form.get("estado")
            print(f"ticket id: {ticket_id}")
            print(f"tecnico id: {tecnico_id}")
            print(f"prioridad: {prioridad}")
            print(f"estado id: {estado}")

            AdminController.asignar_ticket(ticket_id, tecnico_id, prioridad, estado)

            flash("Técnico asignado correctamente", "success")
            return redirect("/adminvista")

        except Exception as e:
            flash(f"Error al crear cuenta: {e}", "error")
            return redirect("/adminvista")


@admin.route("/eliminar-usuario", methods=["POST"])
@login_required
def eliminar_ticket_vista():
    if request.method == "POST":
        if current_user.rol_id != 1:
            return redirect("/")
        try:
            user_id = request.form.get("user_id")
            print(f"User ID: {user_id}")
            AdminController.eliminar_usuario(user_id)
            flash("Usuario eliminado exitosamente", "success")
            return redirect("/adminvista")
        except Exception as e:
            flash(f"Error al eliminar usuario: {e}", "error")
            return redirect("/adminvista")
