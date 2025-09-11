from urllib import request
from website import db
from website.models.ticket import Ticket
from website.models.user import Usuario


class TecnicoController:
    @staticmethod
    def ver_tickets_tecnico(tecnico_id):
        try:
            tickets_tecnico = Ticket.query.filter_by(tecnico_id=tecnico_id).all()

            return tickets_tecnico
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @staticmethod
    def asignar_ticket(ticket_id, prioridad, estado):
        try:
            Ticket.query.filter_by(id=ticket_id).update(
                dict(
                    prioridad=prioridad,
                    estado=estado,
                )
            )
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(e)
