// Agregar la clase 'sub__menu_active' al submenú si la página actual está dentro del submenú activo
window.addEventListener('DOMContentLoaded', function() {
    var currentPagePath = "{{ request.path }}";
    if (currentPagePath === "/fotografias/" || currentPagePath === "/videos/") {
        document.querySelector('.sub__menu').classList.add('sub__menu_active');
    }
});