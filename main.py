#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def contar_letras(frase):
    """
    Cuenta el número de letras alfabéticas en una frase.
    Ignora espacios, números y puntuación.
    """
    return sum(1 for c in frase if c.isalpha())

def main():
    print("Bienvenido a la aplicación de conteo de letras.")
    while True:
        frase = input("Ingresa una frase (o 'salir' para terminar): ")
        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break
        letras = contar_letras(frase)
        print(f"El número de letras en la frase es: {letras}")

if __name__ == "__main__":
    main()