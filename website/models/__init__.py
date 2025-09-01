from .user import Usuario, iniciar_relaciones
from .rol import Rol
from .ticket import Ticket


iniciar_relaciones()

__all__ = ['Usuario', 'Rol', 'Ticket']