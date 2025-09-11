document.addEventListener('DOMContentLoaded', function() {
    // Animación de elementos flotantes
    const floatingElements = document.querySelectorAll('.floating-element');
    
    floatingElements.forEach(element => {
        element.addEventListener('mouseenter', () => {
            element.style.animationPlayState = 'paused';
        });
        
        element.addEventListener('mouseleave', () => {
            element.style.animationPlayState = 'running';
        });
    });
    
    // Validación de formulario
    const loginForm = document.querySelector('.auth-form');
    
    if (loginForm) {
        loginForm.addEventListener('submit', function(e) {
            const email = document.getElementById('email');
            const password = document.getElementById('clave');
            let isValid = true;
            
            // Validación básica de email
            if (!email.value || !email.value.includes('@')) {
                highlightField(email, false);
                isValid = false;
            } else {
                highlightField(email, true);
            }
            
            // Validación de contraseña
            if (!password.value || password.value.length < 6) {
                highlightField(password, false);
                isValid = false;
            } else {
                highlightField(password, true);
            }
            
            if (!isValid) {
                e.preventDefault();
                // Agregar animación de shake al formulario
                loginForm.classList.add('form-shake');
                setTimeout(() => {
                    loginForm.classList.remove('form-shake');
                }, 500);
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
});