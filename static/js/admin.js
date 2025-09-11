document.addEventListener('DOMContentLoaded', function () {
    // Modal de asignar técnico
    const asignarTecnicoModal = document.getElementById('asignarTecnicoModal');
    if (asignarTecnicoModal) {
        handleAssignTechnicianModal(asignarTecnicoModal);
    }

    // Modal de eliminar usuario
    const deleteUserModal = document.getElementById('deleteUserModal');
    if (deleteUserModal) {
        handleDeleteUserModal(deleteUserModal);
    }
});

function handleAssignTechnicianModal(modal) {
    modal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const ticketId = button.getAttribute('data-ticket-id');
        const ticketTitle = button.getAttribute('data-ticket-title');

        const ticketDisplay = modal.querySelector('#ticket_display');
        const ticketIdInput = modal.querySelector('#ticket_id');

        if (ticketDisplay && ticketIdInput) {
            ticketDisplay.value = `#${ticketId} - ${ticketTitle}`;
            ticketIdInput.value = ticketId;
        }
    });

    const form = document.getElementById('assignTechnicianForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            const tecnicoSelect = form.querySelector('select[name="tecnico_id"]');
            if (tecnicoSelect && tecnicoSelect.value === "") {
                event.preventDefault();
                alert('Por favor selecciona un técnico');
                return false;
            }
        });
    }
}

function handleDeleteUserModal(modal) {
    modal.addEventListener('show.bs.modal', function (event) {
        const button = event.relatedTarget;
        const userId = button.getAttribute('data-user-id');
        const userName = button.getAttribute('data-user-name');
        const userType = button.getAttribute('data-user-type');

        console.log('Datos recibidos:', { userId, userName, userType });

        // Buscar elementos DENTRO del modal actual
        const confirmMessage = modal.querySelector('#userInfoConfirm');
        const userIdInput = modal.querySelector('#userIdInput');
        const userTypeInput = modal.querySelector('#userTypeInput');

        console.log('Elementos encontrados:', {
            confirmMessage: !!confirmMessage,
            userIdInput: !!userIdInput,
            userTypeInput: !!userTypeInput
        });

        // Actualizar los valores
        if (confirmMessage) {
            confirmMessage.textContent = `${userType.charAt(0).toUpperCase() + userType.slice(1)}: ${userName} (ID: ${userId})`;
        }

        if (userIdInput) {
            userIdInput.value = userId;
            console.log('userIdInput value set to:', userIdInput.value);
        }

        if (userTypeInput) {
            userTypeInput.value = userType;
            console.log('userTypeInput value set to:', userTypeInput.value);
        }
    });

    // También agrega un listener para el envío del formulario para debuggear
    const form = modal.querySelector('#deleteUserForm');
    if (form) {
        form.addEventListener('submit', function (event) {
            console.log('Formulario enviado');
            console.log('Datos del formulario:', {
                user_id: form.querySelector('#userIdInput')?.value,
                user_type: form.querySelector('#userTypeInput')?.value
            });
        });
    }
}