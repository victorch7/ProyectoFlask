function togglePassword(fieldId) {
    let field = document.getElementById(fieldId);
    let type = field.type === 'password' ? 'text' : 'password';
    field.type = type;
    // Cambiar el ícono del ojo según el tipo
    this.classList.toggle('bi-eye-fill');
    this.classList.toggle('bi-eye-slash-fill');
}