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
DDD3  = [QN, EN, EN + EN, QN, EN + EN, QN, EN + EN, DDQN]

PPP4  = [E4, E4,      D4, E4,      C4, D4,       G4, REST]
DDD4  = [QN, EN, EN + EN, QN, EN + EN, QN, EN + DQN,   SN]

PPP5  = [E4, E4,      D4, E4,      C4, D4,      G4, D4, C4]
DDD5  = [QN, EN, EN + EN, QN, EN + EN, QN, EN + EN, QN, EN]

PPP6  = [C4, G4,      D4, G4, D4,      E4, REST, E4]
DDD6  = [HN, QN, QN + QN, QN, QN, QN + HN,   EN, QN]

PPP7  = [C5, B4, G4, E4]
DDD7  = [QN, QN, QN, QN]

PPP8  = [G4,       A4, REST, E4]
DDD8  = [DQN, EN + EN,   SN, QN]

PPP9  = [G4,       A4, G4, A4, REST]
DDD9  = [DQN, EN + QN, QN, DHN,  EN]

PPP10 = [REST, G4, G4,      G4, D4, E4, F4]
DDD10 = [  QN, QN, EN, EN + EN, QN, QN, QN]

PPP11 = [ F4, E4, E4, REST, REST, E4]
DDD11 = [DQN, EN, HN,   QN,   EN, QN]

PPP12 = [F4, E4, D4, E4,      F4, REST, F4]
DDD12 = [QN, QN, QN, EN, EN + HN,   EN, QN]

PPP13 = [G4, F4, E4, F4,      G4, REST]
DDD13 = [QN, QN, QN, EN, EN + HN,   EN]

PPP14 = [REST, A4, A4,      A4, E4, F4, A4]
DDD14 = [  EN, QN, EN, EN + QN, QN, QN, QN]

PPP15 = [A4, GS4,      E4, REST, E4]
DDD15 = [QN, EN, EN + EN,   EN, QN]

PPP16 = [G4, F4, E4, F4,      G4, REST, G4, G4]
DDD16 = [QN, QN, QN, EN, EN + HN,   EN, EN, EN]

PPP17 = [A4, A4,      A4, REST, A4]
DDD17 = [QN, EN, EN + EN,   SN, QN]

PPP18 = [GS4, E4,  G4,      A4, REST, REST, REST]
DDD18 = [ QN, QN, DQN, EN + QN,   QN,   HN,   WN]

PPP19 = [C5, C5, C5,      C5, F4,      C5, REST, REST, C5, C5, C5]
DDD19 = [EN, EN, EN, EN + EN, QN, EN + QN,   QN,   SN, EN, EN, EN]

PPP20 = [C5, B4, B4,      B4, E4,      C5, B4, A4, REST, E4, E4]
DDD20 = [EN, EN, EN, EN + EN, QN, EN + EN, EN, QN,   QN, EN, EN]

PPP21 = [F4,       G4, A4, G4, D4, E4, F4,  F4, E4, E4, REST]
DDD21 = [DQN, EN + EN, QN, QN, QN, QN, QN, DQN, EN, HN,   WN]

PPP22 = [C5, C5, C5,      C5, F4,      C5, REST, REST, C5, D5, C5]
DDD22 = [EN, EN, EN, EN + EN, QN, EN + QN,   QN,   SN, EN, EN, EN]

PPP23 = [C5, B4, B4,      B4, E4,      C5, B4, A4, REST, E4]
DDD23 = [EN, EN, EN, EN + EN, QN, EN + EN, EN, QN,   QN, EN]

PPP24 = [ F4,      G4,      A4, REST, A4, B4, A4]
DDD24 = [DQN, EN + QN, QN + HN,   EN, EN, EN, EN]

PPP25 = [GS4,      E4,      B4, REST]
DDD25 = [DQN, EN + QN, QN + HN,   HN]

PPP26 = [E4, REST,     GS5, REST, A4]
DDD26 = [QN,   EN, EN + EN,   EN, QN]

PPP27 = [REST,  B4, A4, E5, D5, REST, C5, D5, E5, G5, E5, D5, C5]
DDD27 = [  EN, DQN, QN, QN, QN,   QN, QN, QN, QN, EN, EN, QN, QN]

PPP28 = [B4,       C5, REST, A4, E5]
DDD28 = [DHN, QN + QN,   QN, QN, QN]

PPP29 = [D5, REST, A4, E5, D5, D5, C5, B4]
DDD29 = [QN,   QN, QN, QN, QN, QN, QN, QN]

PPP30 = [B4, B4,      C5, REST, A4, E5]
DDD30 = [HN, QN, QN + QN,   QN, QN, QN]

PPP31 = [D5, REST, C5, D5, E5, G5, E5, D5, C5]
DDD31 = [QN,   QN, QN, QN, QN, EN, EN, QN, QN]

PPP32 = [B4, B4, B4, D5,      C5, REST, A4]
DDD32 = [QN, QN, QN, EN, EN + HN,   QN, QN]

PPP33 = [E5,      A4,      D5, C5, REST, A4]
DDD33 = [DQN, EN + QN, QN + QN, QN,   QN, QN]

PPP34 = [E5,       A4,      G5, E5, D5, D5, E5,       E5]
DDD34 = [DQN, EN + QN, QN + QN, QN, QN, QN, QN, DHN + WN]

PPP35 = [REST, REST, E4]
DDD35 = [  HN,   QN, QN]

PPP36 = [G4,       A4,      A4, REST]
DDD36 = [DQN, EN + QN, QN + HN,   HN]



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
mainPianoPhrase.addNoteList(PPP10, DDD10)
mainPianoPhrase.addNoteList(PPP11, DDD11)
mainPianoPhrase.addNoteList(PPP12, DDD12)
mainPianoPhrase.addNoteList(PPP13, DDD13)
mainPianoPhrase.addNoteList(PPP14, DDD14)
mainPianoPhrase.addNoteList(PPP15, DDD15) # **
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP8, DDD8)
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP9, DDD9)
mainPianoPhrase.addNoteList(PPP10, DDD10)
mainPianoPhrase.addNoteList(PPP11, DDD11)
mainPianoPhrase.addNoteList(PPP12, DDD12)
mainPianoPhrase.addNoteList(PPP16, DDD16)
mainPianoPhrase.addNoteList(PPP17, DDD17)
mainPianoPhrase.addNoteList(PPP18, DDD18)

mainPianoPhrase.addNoteList(PPP19, DDD19)
mainPianoPhrase.addNoteList(PPP20, DDD20)
mainPianoPhrase.addNoteList(PPP21, DDD21)

mainPianoPhrase.addNoteList(PPP22, DDD22)
mainPianoPhrase.addNoteList(PPP23, DDD23)
mainPianoPhrase.addNoteList(PPP24, DDD24)
mainPianoPhrase.addNoteList(PPP25, DDD25)

mainPianoPhrase.addNoteList(PPP26, DDD26)
mainPianoPhrase.addNoteList(PPP27, DDD27)
mainPianoPhrase.addNoteList(PPP28, DDD28)
mainPianoPhrase.addNoteList(PPP29, DDD29)
mainPianoPhrase.addNoteList(PPP30, DDD30)
mainPianoPhrase.addNoteList(PPP31, DDD31)
mainPianoPhrase.addNoteList(PPP32, DDD32)

mainPianoPhrase.addNoteList(PPP33, DDD33)
mainPianoPhrase.addNoteList(PPP34, DDD34)

mainPianoPhrase.addNoteList(PPP35, DDD35)
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP8, DDD8)
mainPianoPhrase.addNoteList(PPP7, DDD7)
mainPianoPhrase.addNoteList(PPP36, DDD36)
mainPianoPhrase.addNoteList(PPP10, DDD10)

mainPianoPhrase.addNoteList(PPP11, DDD11)
mainPianoPhrase.addNoteList(PPP12, DDD12)
mainPianoPhrase.addNoteList(PPP16, DDD16)
mainPianoPhrase.addNoteList(PPP17, DDD17)
mainPianoPhrase.addNoteList(PPP18, DDD18)

mainPianoPhrase.addNoteList(PPP19, DDD19)



pianoPart.addPhrase(mainPianoPhrase)
score.addPart(pianoPart)


# play it
# View.sketch(score)
Play.midi(score)