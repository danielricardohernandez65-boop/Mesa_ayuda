// Función para normalizar los nombres de estados y prioridades
function normalizarTexto(texto) {
    return texto.toLowerCase()
        .replace(/[áàäâ]/g, 'a')
        .replace(/[éèëê]/g, 'e')
        .replace(/[íìïî]/g, 'i')
        .replace(/[óòöô]/g, 'o')
        .replace(/[úùüû]/g, 'u')
        .replace(/ñ/g, 'n')
        .replace(/\s+/g, '-')
        .replace(/[^a-z0-9-]/g, '');
}

// Aplicar clases normalizadas a los badges y colores de borde
function aplicarEstilosTickets() {
    const statusBadges = document.querySelectorAll('.status-badge');
    const priorityBadges = document.querySelectorAll('.priority-badge');
    
    statusBadges.forEach(badge => {
        const estado = badge.textContent.trim();
        const claseNormalizada = 'status-' + normalizarTexto(estado);
        badge.className = 'status-badge ' + claseNormalizada;
    });
    
    priorityBadges.forEach(badge => {
        const prioridad = badge.textContent.trim();
        const claseNormalizada = 'priority-' + normalizarTexto(prioridad);
        badge.className = 'priority-badge ' + claseNormalizada;
    });
    
    // Añadir bordes izquierdos según prioridad
    const ticketCards = document.querySelectorAll('.ticket-card');
    ticketCards.forEach(card => {
        const priorityBadge = card.querySelector('.priority-badge');
        if (priorityBadge) {
            if (priorityBadge.classList.contains('priority-alta') || 
                priorityBadge.classList.contains('priority-critica')) {
                card.style.borderLeftColor = '#e74c3c';
            } else if (priorityBadge.classList.contains('priority-media')) {
                card.style.borderLeftColor = '#f39c12';
            } else {
                card.style.borderLeftColor = '#27ae60';
            }
        }
    });
}

// Configurar el modal de eliminación
function configurarModalEliminacion() {
    const deleteModal = document.getElementById('deleteTicketModal');
    
    if (deleteModal) {
        deleteModal.addEventListener('show.bs.modal', function(event) {
            // Botón que activó el modal
            const button = event.relatedTarget;
            
            // Extraer información de los atributos data-bs-*
            const ticketId = button.getAttribute('data-ticket-id');
            const ticketTitle = button.getAttribute('data-ticket-title');
            
            // Actualizar el modal con esta información
            const modalTitle = deleteModal.querySelector('.modal-title');
            const modalBodyInput = deleteModal.querySelector('#ticketIdInput');
            const ticketTitleConfirm = deleteModal.querySelector('#ticketTitleConfirm');
            
            modalTitle.textContent = 'Confirmar Eliminación - Ticket #' + ticketId;
            ticketTitleConfirm.textContent = '"' + ticketTitle + '"';
            modalBodyInput.value = ticketId;
            
            console.log('Preparando eliminación del ticket:', ticketId, ticketTitle);
        });
    }
}

// Configurar el formulario de eliminación
function configurarFormularioEliminacion() {
    const deleteForm = document.getElementById('deleteTicketForm');
    
    if (deleteForm) {
        deleteForm.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const ticketId = document.getElementById('ticketIdInput').value;
            console.log('Enviando solicitud para eliminar ticket ID:', ticketId);
            
            // Aquí puedes agregar una animación de carga
            const submitBtn = this.querySelector('button[type="submit"]');
            const originalText = submitBtn.innerHTML;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Eliminando...';
            submitBtn.disabled = true;
            
            // Enviar el formulario
            this.submit();
        });
    }
}

// Configurar todos los eventos de eliminación
function configurarEliminacionTickets() {
    configurarModalEliminacion();
    configurarFormularioEliminacion();
}

// Ejecutar cuando el DOM esté cargado
document.addEventListener('DOMContentLoaded', function() {
    // Animación de las tarjetas de estadísticas
    const statCards = document.querySelectorAll('.stat-card');
    
    statCards.forEach((card, index) => {
        card.style.animationDelay = `${index * 0.1}s`;
        card.classList.add('fade-in-up');
    });
    
    // Aplicar estilos a los tickets
    aplicarEstilosTickets();
    
    // Configurar eliminación de tickets
    configurarEliminacionTickets();
    
    // Interacción con las tarjetas de tickets
    const ticketCards = document.querySelectorAll('.ticket-card');
    
    ticketCards.forEach(card => {
        card.addEventListener('click', function(e) {
            if (!e.target.closest('.view-ticket-btn') && !e.target.closest('.delete-ticket-btn')) {
                // Aquí puedes agregar la lógica para ver el ticket completo
                console.log('Ver ticket completo');
            }
        });
    });
    
    // Botones de paginación
    const paginationButtons = document.querySelectorAll('.pagination-btn:not(.disabled)');
    
    paginationButtons.forEach(button => {
        button.addEventListener('click', function() {
            paginationButtons.forEach(btn => btn.classList.remove('active'));
            this.classList.add('active');
            // Aquí puedes agregar la lógica para cambiar de página
        });
    });
    
    // Validación del formulario de nuevo ticket
    const ticketForm = document.querySelector('.ticket-form');
    
    if (ticketForm) {
        ticketForm.addEventListener('submit', function(e) {
            const title = this.querySelector('input[name="titulo"]');
            const description = this.querySelector('textarea[name="descripcion"]');
            let isValid = true;
            
            if (!title.value.trim()) {
                highlightField(title, false);
                isValid = false;
            } else {
                highlightField(title, true);
            }
            
            if (!description.value.trim() || description.value.trim().length < 10) {
                highlightField(description, false);
                isValid = false;
            } else {
                highlightField(description, true);
            }
            
            if (!isValid) {
                e.preventDefault();
                showNotification('Por favor, completa todos los campos requeridos correctamente.', 'error');
            }
        });
    }
    
    function highlightField(field, isValid) {
        if (isValid) {
            field.style.borderColor = '#4caf50';
        } else {
            field.style.borderColor = '#f44336';
        }
    }
    
    function showNotification(message, type = 'success') {
        // Aquí puedes implementar un sistema de notificaciones bonito
        alert(message);
    }
    
    // Filtros y ordenación (placeholder para funcionalidad futura)
    const filterButtons = document.querySelectorAll('.filter-btn');
    
    filterButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Aquí puedes implementar la lógica de filtrado y ordenación
            console.log('Funcionalidad de ' + this.textContent.trim());
        });
    });
});