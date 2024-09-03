# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Guitar

from music import *

import Notes

def GuitarPart():    
    guitarPart = Part(GUITAR, 1)
    mainGuitarPhrase = Phrase()
    mainGuitarPhrase.setTempo(190)
    
    guitarPart.addPhrase(mainGuitarPhrase)
    
    return guitarPart