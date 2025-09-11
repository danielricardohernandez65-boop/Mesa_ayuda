
from flask import Blueprint, flash, redirect, render_template, request
from flask_login import current_user, login_required

from website.controllers.tecnico_controller import TecnicoController


tecni = Blueprint("tecni", __name__)


@tecni.route("/tecnico-tickets")
@login_required
def admin_panel():
    if current_user.rol_id != 2:
        return redirect("/")

    tickets = []

    try:
        tickets = TecnicoController.ver_tickets_tecnico(tecnico_id=current_user.id)

    except Exception as e:
        flash(f"Error: {e}", "error")

    return render_template("tecnico.html", tickets=tickets)


@tecni.route("/actualizar-ticket", methods=["POST"])
@login_required
def asignar_tecnico():
    if current_user.rol_id != 2:
        return redirect("/")
    if request.method == "POST":
        try:
            ticket_id = request.form.get("ticket_id")

            prioridad = request.form.get("prioridad")
            estado = request.form.get("estado")
            print(f"ticket id: {ticket_id}")

            print(f"prioridad: {prioridad}")
            print(f"estado id: {estado}")

            TecnicoController.asignar_ticket(ticket_id, prioridad, estado)

            flash("Ticket actualizado correctamente", "success")
            return redirect("/tecnico-tickets")

        except Exception as e:
            flash(f"Error al actualizar ticket: {e}", "error")
            return redirect("/tecnico-tickets")
