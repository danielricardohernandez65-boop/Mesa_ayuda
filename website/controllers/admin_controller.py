from urllib import request
from website import db
from website.models.ticket import Ticket
from website.models.user import Usuario


class AdminController:
    @staticmethod
    def ver_todos_tickets():
        try:
            tickets_todos = Ticket.query.all()

            return tickets_todos
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @staticmethod
    def ver_todos_clientes():
        try:
            clientes_todos = Usuario.query.filter_by(rol_id=3).all()

            return clientes_todos
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @staticmethod
    def ver_todos_tecnicos():
        try:
            tecnicos_todos = Usuario.query.filter_by(rol_id=2).all()

            return tecnicos_todos
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @staticmethod
    def crear_tecnico(username, email, password):
        # Validaciones
        try:
            if Usuario.query.filter_by(email=email).first():
                raise Exception("El email ya está registrado")

            if Usuario.query.filter_by(username=username).first():
                raise Exception("El nombre de técnico ya existe")

            # Crear usuario
            nuevo_tecnico = Usuario(
                username=username, email=email, password=password, rol_id=2
            )

            db.session.add(nuevo_tecnico)
            db.session.commit()

            return nuevo_tecnico
        except Exception as e:
            db.session.rollback()
            raise Exception(e)

    @staticmethod
    def asignar_ticket(ticket_id, tecnico_id, prioridad, estado):
        try:
            Ticket.query.filter_by(id=ticket_id).update(
                dict(prioridad=prioridad, estado=estado, tecnico_id=tecnico_id)
            )
            db.session.commit()
            return True
        except Exception as e:
            db.session.rollback()
            raise Exception(e)
        
    @staticmethod
    def eliminar_usuario(usuario_id):
        try:
            usuario_eliminar: Usuario = Usuario.query.get(usuario_id)
            db.session.delete(usuario_eliminar)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise Exception(e)
        return True
    
