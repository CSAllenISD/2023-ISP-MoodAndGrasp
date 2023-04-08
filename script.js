document.addEventListener('DOMContentLoaded', () => {
    const nextButton = document.getElementById('nextButton');
    const questions = document.querySelectorAll('.question');

    nextButton.addEventListener('click', () => {
        for (let i = 0; i < questions.length; i++) {
            if (questions[i].classList.contains('active')) {
                questions[i].classList.remove('active');
                if (i + 1 < questions.length) {
                    questions[i + 1].classList.add('active');
                } else {
                    questions[0].classList.add('active');
                }
                break;
            }
        }
    });
});
const hamburgerMenu = document.getElementById('hamburger-menu');
const navLinks = document.querySelector('.nav-links');

hamburgerMenu.addEventListener('click', () => {
    navLinks.classList.toggle('show');
});
