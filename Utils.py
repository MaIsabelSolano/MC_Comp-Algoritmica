# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Utils

from music import *

def BeQuiet(notesList = []):
    restNotes = []
    for _ in range(len(notesList)):
        restNotes.append(REST)
    return restNotes