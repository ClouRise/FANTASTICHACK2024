document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector('#loginForm');
    if (form) {
        form.addEventListener('submit', (event) => {
            event.preventDefault();
            const usernameInput = document.getElementById('username');
            const passwordInput = document.getElementById('password');

            if (!usernameInput.value.trim()) {
                usernameInput.classList.add('input-error');
            } else {
                usernameInput.classList.remove('input-error');
            }

            if (!passwordInput.value.trim()) {
                passwordInput.classList.add('input-error');
            } else {
                passwordInput.classList.remove('input-error');
            }
        });
    }
});