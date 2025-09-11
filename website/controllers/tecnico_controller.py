from urllib import request

from sqlalchemy import case, func
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
        

    @staticmethod
    def estado_admin(tecnico_id):
        try:
            # Total de tickets
            total_tecnico = db.session.query(func.count(Ticket.id)).filter(Ticket.tecnico_id == tecnico_id).scalar()

            counts = (
                db.session.query(
                    func.sum(case((Ticket.prioridad == "Baja", 1), else_=0)).label(
                        "baja"
                    ),
                    func.sum(
                        case((Ticket.prioridad == "Media", 1), else_=0)
                    ).label("media"),
                    func.sum(
                        case((Ticket.prioridad == "Alta", 1), else_=0)
                    ).label("alta"),
                    
                )
                .filter(Ticket.tecnico_id == tecnico_id)
                .first()
            )

            respuesta = {
                "total": total_tecnico or 0,
                "baja": counts.baja or 0,
                "media": counts.media or 0,
                "alta": counts.alta or 0,
            }
        except Exception as e:
            db.session.rollback()
            raise Exception(f"problema en estado admin: {e}")

        return respuesta
