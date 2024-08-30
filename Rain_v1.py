# Unviersidad del valle de Guatemala
# Facultad de Ingeniería
# Departamento de Ciencias de la Computación
# Música computacional
# Ma. Isabel Solano 20504

from music import *

## REFERENCES ===============================================
# https://www.youtube.com/watch?v=rZLNxpz5bfY (trombon)
# https://musescore.com/user/9026011/scores/2688026 (notas de abajo)
# https://musescore.com/user/29706205/scores/6033100 (alternativa)


score = Score()


# LETRA - PIANO ===============================================
pianoPart = Part()
mainPianoPhrase = Phrase()
mainPianoPhrase.setTempo(190);

# notas
pitches1   = [A3, G4, C5,       B4, G4, REST]
durations1 = [QN, QN, DQN, QN + EN, HN,   EN]
pitches2   = [A3, G4, C5,       B4, REST, REST, REST]
durations2 = [QN, QN, DQN, QN + QN,  SN,    EN,   QN]
pitches3   = [E4, E4, D4, D4, E4, C4]
durations3 = [QN, QN, QN, EN, QN, EN]

## agregar
mainPianoPhrase.addNoteList(pitches1, durations1)
mainPianoPhrase.addNoteList(pitches1, durations1)
mainPianoPhrase.addNoteList(pitches2, durations2)
mainPianoPhrase.addNoteList(pitches3, durations3)
pianoPart.addPhrase(mainPianoPhrase)
score.addPart(pianoPart)


# play it
Play.midi(score)