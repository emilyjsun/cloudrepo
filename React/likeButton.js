let btn = document.createElement('button');
btn.textContent = 'Like';
btn.addEventListener('click', () => {
    btn.textContent = 'You clicked me!';
})

let div = document.getElementById('like_button_container');
div.appendChild(btn);