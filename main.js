const readline = require('readline');

function contarLetras(frase) {
    /**
     * Cuenta el número de letras alfabéticas en una frase.
     * Ignora espacios, números y puntuación.
     */
    return frase.split('').filter(c => c.match(/[a-zA-Z]/)).length;
}

function main() {
    const rl = readline.createInterface({
        input: process.stdin,
        output: process.stdout
    });

    console.log("Bienvenido a la aplicación de conteo de letras.");

    function preguntar() {
        rl.question("Ingresa una frase (o 'salir' para terminar): ", (frase) => {
            if (frase.toLowerCase() === 'salir') {
                console.log("¡Hasta luego!");
                rl.close();
                return;
            }
            const letras = contarLetras(frase);
            console.log(`El número de letras en la frase es: ${letras}`);
            preguntar();
        });
    }

    preguntar();
}

main();