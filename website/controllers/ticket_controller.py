from sqlalchemy import case, func
from website.models.ticket import Ticket
from website import db


class TicketController:
    @staticmethod
    def crear_ticket(titulo, descripcion, usuario_id):
        nuevo_ticket = Ticket(
            titulo=titulo, descripcion=descripcion, usuario_id=usuario_id
        )

        db.session.add(nuevo_ticket)
        db.session.commit()

        return nuevo_ticket

    @staticmethod
    def ver_tickets(usuario_id):
        tickets_usuario = Ticket.query.filter_by(usuario_id=usuario_id).all()

        return tickets_usuario

    @staticmethod
    def estados_tickets(usuario_id):
        counts = (
            db.session.query(
                func.sum(case((Ticket.estado == "En progreso", 1), else_=0)).label(
                    "progreso"
                ),
                func.sum(
                    case((Ticket.estado == "Pendiente cliente", 1), else_=0)
                ).label("pendiente_cliente"),
                func.sum(
                    case((Ticket.estado == "Pendiente tercero", 1), else_=0)
                ).label("pendiente_tercero"),
                func.sum(
                    case((Ticket.estado == "Pendiente aprovacion", 1), else_=0)
                ).label("pendiente_aprovacion"),
            )
            .filter(Ticket.usuario_id == usuario_id)
            .first()
        )

        respuesta = {
            "progreso": counts.progreso or 0,
            "pendiente_cliente": counts.pendiente_cliente or 0,
            "pendiente_tercero": counts.pendiente_tercero or 0,
            "pendiente_aprovacion": counts.pendiente_aprovacion or 0,
        }

        return respuesta
