//Seccion del javascript proyecto Asistente virtual


//Seccion de reconocimiento de voz

const grab = document.getElementById('grabar');
const text = document.getElementById('texto_salida');
const salida = document.getElementById('textosal');

let recognition = new webkitSpeechRecognition();
recognition.lang = 'es-ES';
recognition.continuous = true;
recognition.interimResults = false;
//seccion donde carga los resultados de la transformacion de voz a texto
recognition.onresult = (event) => {
    const result = event.results;
    const frase = result[result.length - 1][0].transcript;
    recognition.abort();
    text.value = frase;
    salida.value = ""
    recognition.abort();
}
//Seccion de activacion de funcion de reconocimiento de voz
grab.addEventListener('click', () => {
    recognition.start();
});

//Funcion de reproduccion de animacion
function anima_foto(direccion){
    document.getElementById('imani').src =direccion
}    
//Seccion de funcion de transformacion de texto a audio
function voz(texto){
    const speech = new SpeechSynthesisUtterance();
    speech.text = texto;
    speech.volumen = 1;
    speech.rate = 1;
    speech.pitch = 1;

    window.speechSynthesis.speak(speech);
}


