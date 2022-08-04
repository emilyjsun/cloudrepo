console.log('you are linked')

let linksButtons = document.getElementsByTagName('a');
console.log(linksButtons);

let btnA = document.getElementById('btnA');
console.log(btnA);

btnA.addEventListener('click',() => {
    btnA.classList.add('btn-secondary'); //remove as well
    btnA.textContent = "Hello World"
    btnA.innerHTML = "<em>Rainy</em>"
})

