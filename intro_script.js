function showSection(sectionId) {
    const sections = document.querySelectorAll('.section');
    sections.forEach(section => {
        section.classList.remove('active');
    });
    document.getElementById(sectionId).classList.add('active');
}

// Show the home section by default
document.addEventListener('DOMContentLoaded', () => {
    showSection('home');
});