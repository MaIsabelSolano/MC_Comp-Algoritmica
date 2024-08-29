# Unviersidad del valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# Música computacional
# Ma. Isabel Solano 20504

from music import *

score = Score()


# LETRA - PIANO ===============================================
pianoPart = Part()
mainPianoPhrase = Phrase()
mainPianoPhrase.setTempo(190);

# notas
pitches1   = [A3, G4, C5,       B4, G4, REST]
durations1 = [QN, QN, DQN, QN + EN, HN,   QN]

## agregar
mainPianoPhrase.addNoteList(pitches1, durations1)
pianoPart.addPhrase(mainPianoPhrase)
score.addPart(pianoPart)


# play it
Play.midi(score)