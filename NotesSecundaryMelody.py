# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Notas Melodia

from music import *

# PPP1 = [REST, REST, REST, REST, REST, REST]
# DDD1 = [QN  , QN  , DQN , QN + EN, HN,  EN]
#       1     1     1.5   1  + 0.5
#       5

# FOR PIANO
PPP1 = [[CS3, E3, GS2], REST, REST]
DDD1 = [WN + QN, HN,  EN]

PPP2 = [B4, B4, B4, B4, B4, B4]
DDD2 = [EN, EN, EN, EN, EN, EN]

PPP3 = [[G4, C4, A4],[G4, C4, A4]]
DDD3 = [EN, EN]

PPP4 = [[C2, C1], [B1, B0], [G1, G0], [F1, F0], [G1, G0], [B1, B0]]
DDD4 = [DQN, DQN, DQN, DQN, QN, QN]

PPP5 = [[C2, C1], [D2, D1], [E2, E1], [F2, F1], [E2, E1], [D2, D1]]
DDD5 = [DQN, DQN, DQN, DQN, QN, QN]

PPP6 = [[F1, F0], F1, [C2, F2, A2], [G1, G0], G1, [D2, G2, B2], [A2, E2, A1]]
DDD6 = [QN, QN, QN, HN, QN, QN, QN + HN]

PPP7 = [
    REST, [CS2, E2, GS4], REST, [A2, CS3, E3], 
    [B1, DS4, FS4], [E2, GS2, B2], [FS2, A2, CS3], [GS2, B2, E3],
    [A1, CS2, E2], [GS2, C3, DS3]
]
DDD7 = [WN + QN, WN, WN + SN, WN, WN, WN + WN, WN + WN, WN + WN, WN + DHN, WN + HN]

PPP8 = [
    REST, [A2, CS3, E3], [GS2, B2, DS3], [CS2, E2, GS2], 
    [FS2, A2, CS3], [B1, DS2, FS2], [E2, GS2, B2]
]
DDD8 = [
    WN + DHN, WN + WN, WN, WN, WN, WN, WN
]
DDD8_1 = [
    DHN + EN, WN + WN, WN, WN, WN, WN + HN, WN
]

PPP9 = [
    [A3, CS4, E4], [GS3, B3, DS4], [CS3, E3, GS3], [CS3, E3, GS3],
    [FS3, A3, CS4], [B2, DS3, FS3], [CS3, E3, GS3], [CS3, E3, GS3],
    [A3, CS4, E4], [GS3, B3, DS4], [CS3, E3, GS3], [CS3, E3, GS3],
    [FS3, A3, CS4], [GS3, B3, DS4], [A3, CS4, E4], [B2, DS3, FS3], [A3, CS4, E4], [A3, CS4, E4]
]
DDD9 = [
    WN + DHN, WN + QN, HN + QN, HN ,
    WN + DHN + QN, WN + QN, HN + QN, HN + QN,
    WN + HN, WN, HN + QN, HN ,
    WN + DHN, WN + QN, HN, HN, QN, QN
]

# FOR GUITAR
GPPP1 = [C3, B3, E4, D4, B3, G3]
GDDD1 = [QN, QN, DQN, DQN, QN, QN]

GPPP2 = [A2, B3, E4, D4, B3]
GDDD2 = [QN, QN, DQN, DQN, DQN]

GPPP3 = [E2, B3, E4, D4, B3]
GDDD3 = [QN, QN, DQN, DQN, DQN]

GPPP4 = [F2, B3, E4, D4, E4]
GDDD4 = [QN, QN, DQN, DQN, DQN]

GPPP5 = [G2, CS4, D4]
GDDD5 = [QN, QN, QN]

GPPP6 = [C2, G2, C3, F3, G3, F3, B2, C3]
GDDD6 = [EN, EN, EN, SN, SN, EN, EN, QN]

