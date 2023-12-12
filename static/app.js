document.addEventListener('DOMContentLoaded', function(){
    const checkbox = document.getElementById('switch')

    const lightModeActivado =localStorage.getItem('lightModeActivado') === 'true';

    checkbox.checked=lightModeActivado;

    if(lightModeActivado){
        document.body.classList.add('light-mode')
    }

    checkbox.addEventListener('change', function(){
        document.body.classList.toggle('light-mode');
        localStorage.setItem('lightModeActivado',checkbox.checked)
    })

    
})

