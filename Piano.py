# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Piano

from music import *

import Notes

def PianoPart():
    pianoPart = Part()
    mainPianoPhrase = Phrase()
    mainPianoPhrase.setTempo(190);
       
    pianoPart.addPhrase(mainPianoPhrase)
    
    return pianoPart
