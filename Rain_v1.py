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
PPP1  = [A3, G4, C5,       B4, G4, REST]
DDD1  = [QN, QN, DQN, QN + EN, HN,   EN]

PPP2  = [A3, G4, C5,       B4, REST, REST, REST]
DDD2  = [QN, QN, DQN, QN + QN,  SN,    EN,   QN]

PPP3  = [E4, E4,      D4, E4,      C4, E4,      B3, D4]
DDD3  = [QN, HN, HN + EN, QN, EN + EN, QN, EN + EN, DQN]

PPP4  = [E4, E4,      D4, E4,      C4, D4,       G4, REST]
DDD4  = [QN, HN, HN + EN, QN, EN + EN, QN, EN + DQN,   SN]

PPP5  = [E4, E4,      D4, E4,      C4, D4,      G4, D4, C4]
DDD5  = [QN, HN, HN + EN, QN, EN + EN, QN, EN + EN, QN, EN]

PPP6  = [C4, G4,      D4, G4, D4,      E4, REST, E4]
DDD6  = [HN, QN, QN + QN, QN, QN, QN + HN,   EN, QN]

PPP7  = [C5, B4, G4, E4]
DDD7  = [QN, QN, QN, QN]

PPP8  = [G4,       A4, REST, E4]
DDD8  = [DQN, EN + EN,   SN, QN]

PPP9  = [G4,       A4, G4, A4, REST]
DDD9  = [DQN, EN + QN, QN, DHN,  EN]

PPP10 = [REST, G4, G4]
DDD10 = [  QN, HN, HN]



## agregar
mainPianoPhrase.addNoteList(PPP1, DDD1)
mainPianoPhrase.addNoteList(PPP1, DDD1)
mainPianoPhrase.addNoteList(PPP2, DDD2)
mainPianoPhrase.addNoteList(PPP3, DDD3)
mainPianoPhrase.addNoteList(PPP4, DDD4)
mainPianoPhrase.addNoteList(PPP3, DDD3)
mainPianoPhrase.addNoteList(PPP5, DDD5)
mainPianoPhrase.addNoteList(PPP6, DDD6)
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP8, DDD8)
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP9, DDD9)

pianoPart.addPhrase(mainPianoPhrase)
score.addPart(pianoPart)


# play it
Play.midi(score)