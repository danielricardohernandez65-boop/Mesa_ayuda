from sqlalchemy import case, func
from website.models.ticket import Ticket
from website import db


class TicketController:
    @staticmethod
    def crear_ticket(titulo, descripcion, usuario_id):
        try:
            nuevo_ticket = Ticket(
                titulo=titulo, descripcion=descripcion, usuario_id=usuario_id
            )

            db.session.add(nuevo_ticket)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception("Error al crear ticket")

        return nuevo_ticket

    @staticmethod
    def ver_tickets(usuario_id):
        tickets_usuario = Ticket.query.filter_by(usuario_id=usuario_id).all()

        return tickets_usuario

    @staticmethod
    def eliminar_ticket(ticket_id):
        try:
            ticket_eliminar: Ticket = Ticket.query.get(ticket_id)
            db.session.delete(ticket_eliminar)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(e)
        return True

    @staticmethod
    def estados_tickets(usuario_id):
        try:
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
        except Exception as e:
            db.session.rollback()
            raise Exception("Error al ver estados ticket")

        return respuesta
