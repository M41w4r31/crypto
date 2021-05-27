#!/usr/bin/env python3
from random import choice

preguntas = ['78 * 9',
                           '55 * 2',
                           '___ is the linux pet',
                           '44 * 5',
                           '22 * 5',
                           'The ____ is the best university of the country']

## Picking a Birthday Message


aleatorio = choice (preguntas)

print (aleatorio)

messageNumber = input('Answer : ')


if aleatorio == preguntas[0]:
    if messageNumber == '702':
        print ("Correcto")
if aleatorio == preguntas[1]:
    if messageNumber == '110':
        print ("Correcto")
if aleatorio == preguntas[2]:
    if messageNumber == 'tux':
        print ("Correcto")
if aleatorio == preguntas[3]:
    if messageNumber == '220':
        print ("Correcto")
if aleatorio == preguntas[4]:
    if messageNumber == '110':
        print ("Correcto")
if aleatorio == preguntas[5]:
    if messageNumber == 'UANL':
        print ("Correcto") 