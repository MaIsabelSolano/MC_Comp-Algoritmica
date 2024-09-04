# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Main Code - Rain

from music import *

from Trombone import TrombonePart
from Piano import PianoPart
from Guitar import GuitarPart

## REFERENCES =========================================================
# https://www.youtube.com/watch?v=rZLNxpz5bfY (trombon)
# https://musescore.com/user/9026011/scores/2688026 (notas de abajo)
# https://musescore.com/user/29706205/scores/6033100 (alternativa)
# https://www.youtube.com/watch?v=H0pm-00elvo (Piano para los precoros)
## ====================================================================

score = Score()

# Insert in the score all the instruments Parts
score.addPart(PianoPart())
score.addPart(GuitarPart())
score.addPart(TrombonePart())

# play it
View.sketch(score)
Play.midi(score)
