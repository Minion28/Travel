const cont = document.getElementById('cont');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    cont.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    cont.classList.remove("active");
});