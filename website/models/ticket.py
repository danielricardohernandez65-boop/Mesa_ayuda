from website import db
from datetime import datetime


class Ticket(db.Model):  
    __tablename__ = "ticket"

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200), nullable=False)  
    descripcion = db.Column(db.Text, nullable=False)  
    prioridad = db.Column(db.String(50), default="Media")
    estado = db.Column(db.String(50), default="En progreso")
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    date_updated = db.Column(db.DateTime(), onupdate=datetime.utcnow)

    
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    tecnico_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=True)

    

    def __repr__(self):
        return f"<Ticket {self.id} - {self.estado}>"
