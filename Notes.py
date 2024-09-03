# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Notas Melodia

from music import *

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

PPP37 = [B4, B4,      B4, E4,      C5, B4, A4, REST, E4]
DDD37 = [QN, EN, EN + EN, QN, EN + EN, EN, QN,   QN, QN]

PPP38 = [GS4,      E4,      B5, REST, A4, E5]
DDD38 = [DQN, EN + QN, QN + QN,   QN, QN, QN]

PPP39 = [D5, REST, C5, D5, E5, G5, E5, D5, C5]
DDD39 = [QN,   QN, QN, QN, QN, EN, EN, QN, QN]

PPP40 = [ B4,      C5, REST, A4, E5]
DDD40 = [DHN, QN + QN,   QN, QN, QN]

PPP41 = [D5, REST, A4, E5, D5, D5, C5, B4]
DDD41 = [QN, QN, QN, QN, QN, QN, QN, QN]

PPP42 = [B4,      C5, REST, A4, E5]
DDD42 = [HN, QN + QN,   QN, QN, QN]

PPP43 = [B4, B4, B4, D5,     C5, REST, A4]
DDD43 = [QN, QN, QN, EN, EN + HN,  QN, QN]

PPP44 = [E5,       A4,      D5, C5, REST, A4]
DDD44 = [DQN, EN + QN, QN + QN, QN,   QN, QN]

PPP45 = [E5,       A4,      G5, E5, D5, D5, E5,       E5, REST, B4, C5]
DDD45 = [DQN, EN + QN, QN + QN, QN, QN, QN, QN, DHN + HN,   QN, EN, EN]

PPP46 = [ E4, D4, E4,  C4, A4]
DDD46 = [DHN, EN, EN, DHN, QN]

PPP47 = [A4, REST, E4, G4, E4, E4, ES4]
DDD47 = [QN,   QN, EN, SN, SN, EN,  EN]

PPP48 = [E4, C4, B3,      G3, ES4, A4]
DDD48 = [EN, EN, EN, EN + EN,  QN, EN]

PPP49 = [A4, G4, A4, G4, E4, E4, D4,      C4, C4, A3,      C4, G4, C4, D4]
DDD49 = [EN, EN, EN, EN, EN, EN, EN, EN + EN, EN, EN, EN + EN, EN, EN, EN]

PPP50 = [E4, ES4, E4, D4, C4, D4, E4, ES4]
DDD50 = [EN,  EN, EN, EN, EN, EN, EN,  EN]

PPP51 = [E4, D4, C4, D4, E4, ES4, E4, D4, C4, D4, E4]
DDD51 = [EN, EN, EN, EN, EN,  EN, EN, EN, EN, EN, EN]

PPP52 = [E4, D4, C4, D4, E4, D4, C4, D4]
DDD52 = [EN, EN, EN, EN, EN, EN, EN, EN]

PPP53 = [E4, D4, C4, D4, E4, G4, E4, G4]
DDD53 = [EN, EN, EN, EN, EN, EN, EN, EN]

PPP54 = [E4, G4,      E4, REST, G4, C5, C5, D5,      C5, REST, G4, E5, D5, D5, D5]
DDD54 = [EN, EN, EN + EN,   EN, EN, EN, EN, EN, EN + EN,   EN, EN, EN, EN, EN, WN]

PPP55 = [E5, A4, E5]
DDD55 = [HN, QN, QN]

PPP56 = [D5, REST, C5, D5, E5, G5, E5, D5, C5]
DDD56 = [QN,   QN, QN, QN, QN, EN, EN, QN, QN]

PPP57 = [BS4,      C5, REST, A4, E5, D5, REST, A4, E5]
DDD57 = [DHN, QN + QN,   QN, QN, QN, QN,   QN, QN, QN]

PPP58 = [B4,       C5, REST, A4, E5, D5, REST, A4, E5]
DDD58 = [DHN, QN + QN,   QN, QN, QN, QN,   QN, QN, QN]

PPP59 = [D5, D5, C5, B4]
DDD59 = [QN, QN, QN, QN]

PPP60 = [B4, B4,      C5, REST, A4, E5]
DDD60 = [HN, QN, QN + QN,   QN, QN, QN]

PPP61 = [B4, B4, D5,      C5, REST, A4]
DDD61 = [HN, QN, EN, EN + HN,   QN, QN]

PPP62 = [E5,       A4,      D5, C5, REST, A4]
DDD62 = [DQN, EN + QN, QN + QN, QN,   QN, QN]

PPP63 = [E5,       A4,      G5, REST, A4, E5]
DDD63 = [DQN, EN + QN, QN + QN,   QN, QN, QN]

PPP64 = [ B4,      C5, REST, A4, E5]
DDD64 = [DHN, QN + QN,   QN, QN, QN]

PPP65 = [D5, REST, A4, E5,      E5, D5, C5, B4]
DDD65 = [QN,   QN, QN, EN, EN + QN, QN, QN, QN]

PPP66 = [B4, B4,      C5, REST, A4, E5]
DDD66 = [HN, QN, QN + QN,   QN, QN, QN]

PPP67 = [E5,       A4,      G5, E5, D5, D5]
DDD67 = [DQN, EN + QN, QN + QN, QN, QN, QN]

PPP68 = [E5,                 E5, REST]
DDD68 = [QN, DHN + WN + WN + WN,   WN]

PPP69 = [C4, G4,      D4, G4, D4,       E4, REST]
DDD69 = [HN, QN, QN + QN, QN, QN, QN + DHN,   QN]