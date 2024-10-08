# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Guitar

from music import *

import NotesMainMelody
import NotesSecundaryMelody

from Utils import BeQuiet

def GuitarPart():    
    guitarPart = Part(GUITAR, 1)
    mainGuitarPhrase = Phrase()
    mainGuitarPhrase.setTempo(190)
            
    # Instrumental Introduction
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP1, NotesMainMelody.DDD1)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP1, NotesMainMelody.DDD1)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP2, NotesMainMelody.DDD2)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP3, NotesMainMelody.DDD3)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP4, NotesMainMelody.DDD4)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP3, NotesMainMelody.DDD3)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP5, NotesMainMelody.DDD5)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP6, NotesMainMelody.DDD6)
    
    # Voice Start
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP7), NotesMainMelody.DDD7)
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP1, NotesSecundaryMelody.GDDD1)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP3, NotesSecundaryMelody.GDDD3)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP5, NotesSecundaryMelody.GDDD5)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList([REST], [QN])

    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP1, NotesSecundaryMelody.GDDD1)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP3, NotesSecundaryMelody.GDDD3)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP5, NotesSecundaryMelody.GDDD5)
    mainGuitarPhrase.addNoteList([REST], [EN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP6, NotesSecundaryMelody.GDDD6)

    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP19), NotesMainMelody.DDD19)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP20), NotesMainMelody.DDD20)
    mainGuitarPhrase.addNoteList([REST], [WN + WN + HN + HN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP6, NotesSecundaryMelody.GDDD6)

    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP22), NotesMainMelody.DDD22)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP23), NotesMainMelody.DDD23)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP24), NotesMainMelody.DDD24)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP25), NotesMainMelody.DDD25)
    
    # Instrumental
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP26, NotesMainMelody.DDD26)
    
    # Voice Continue # Main Choir
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP27), NotesMainMelody.DDD27)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP28), NotesMainMelody.DDD28)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP29), NotesMainMelody.DDD29)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP30), NotesMainMelody.DDD30)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP31), NotesMainMelody.DDD31)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP32), NotesMainMelody.DDD32)
    
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP33), NotesMainMelody.DDD33)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP34), NotesMainMelody.DDD34)
    
    # Pre-Choir #2
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP7), NotesMainMelody.DDD7)
    mainGuitarPhrase.addNoteList([REST], [HN + QN + QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP1, NotesSecundaryMelody.GDDD1)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP2, NotesSecundaryMelody.GDDD2)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP3, NotesSecundaryMelody.GDDD3)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP4, NotesSecundaryMelody.GDDD4)
    mainGuitarPhrase.addNoteList([REST], [QN])
    mainGuitarPhrase.addNoteList([REST], [QN])

    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP6, NotesSecundaryMelody.GDDD6)
    mainGuitarPhrase.addNoteList([REST], [HN])

    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP19), NotesMainMelody.DDD19)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP20), NotesMainMelody.DDD20)
    mainGuitarPhrase.addNoteList([REST], [WN + WN + HN + HN])
    mainGuitarPhrase.addNoteList(NotesSecundaryMelody.GPPP6, NotesSecundaryMelody.GDDD6)

    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP22), NotesMainMelody.DDD22)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP23), NotesMainMelody.DDD23)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP24), NotesMainMelody.DDD24)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP25), NotesMainMelody.DDD25)
            
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP39), NotesMainMelody.DDD39)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP40), NotesMainMelody.DDD40)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP41), NotesMainMelody.DDD41)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP42), NotesMainMelody.DDD42)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP39), NotesMainMelody.DDD39)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP43), NotesMainMelody.DDD43)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP44), NotesMainMelody.DDD44)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP45), NotesMainMelody.DDD45)
    
    # Instrumental
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP46, NotesMainMelody.DDD46)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP47, NotesMainMelody.DDD47)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP48, NotesMainMelody.DDD48)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP49, NotesMainMelody.DDD49)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP50, NotesMainMelody.DDD50)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP51, NotesMainMelody.DDD51)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP52, NotesMainMelody.DDD52)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP52, NotesMainMelody.DDD53)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP54, NotesMainMelody.DDD54)
    
    # Voice Continue
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP55), NotesMainMelody.DDD55)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP56), NotesMainMelody.DDD56)        
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP55), NotesMainMelody.DDD55)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP57), NotesMainMelody.DDD57)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP58), NotesMainMelody.DDD58)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP59), NotesMainMelody.DDD59)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP60), NotesMainMelody.DDD60)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP56), NotesMainMelody.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP61), NotesMainMelody.DDD61)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP62), NotesMainMelody.DDD62)
    
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP63), NotesMainMelody.DDD63)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP56), NotesMainMelody.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP64), NotesMainMelody.DDD64)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP65), NotesMainMelody.DDD65)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP66), NotesMainMelody.DDD66)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP56), NotesMainMelody.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP61), NotesMainMelody.DDD61)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP62), NotesMainMelody.DDD62)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP67), NotesMainMelody.DDD67)
    mainGuitarPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP68), NotesMainMelody.DDD68)
    
    # Finalizing with Instrumental Part
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP3, NotesMainMelody.DDD3)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP5, NotesMainMelody.DDD5)
    mainGuitarPhrase.addNoteList(NotesMainMelody.PPP69, NotesMainMelody.DDD69)

    guitarPart.addPhrase(mainGuitarPhrase)
    
    return guitarPart