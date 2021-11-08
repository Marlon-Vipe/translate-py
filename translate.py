#Import libraries.
from typing import Text
from textblob import TextBlob
import os


def main():
    print('Bienvenido al traductor\n')

    print('  1. Español \n  2. Ingles \n  3. Frances \n')
    language = input('Ingrese el idioma de la palabra o frase a traducir:  ')
    if language == '1':
        translate('es')
    elif language == '2':
        translate('en')
    elif language == '3':
        translate('fr')
    else:
        input('Debe ser un carácter válido, presione cualquier tecla para continuar')
        os.system('cls')
        main()


def exitTranslate():
    condition = input('Desea continuar? y/n ---> ')
    if condition == 'y' or condition == 'Y':
        os.system('cls')
        main()
    elif condition == 'n' or condition == 'N':
        print('Gracias por usar el mejor traductor')
        exit()
    elif condition not in ('y', 'n'):
        print('Debe colocar y ó n\n')
        exitTranslate()

def translate(text):
    os.system('cls')
    haski = input('Ingrese la palabra o frase a traducir:  ')
    haski = TextBlob(haski)
    try:
        traduccion = haski.translate(to=text)
        print(traduccion)

    except Exception as e:
        print('Ha ocurrido un error. Es posible que hayas puesto una palabra del mismo idioma a traducir o un carácter inválido. \n')
        input('Presione cualquier tecla para continuar')
        os.system('cls')
        translate(text)
    exitTranslate()


main()
