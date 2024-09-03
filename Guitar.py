# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Guitar

from music import *

import Notes

from Utils import BeQuiet

def GuitarPart():    
    guitarPart = Part(GUITAR, 1)
    mainGuitarPhrase = Phrase()
    mainGuitarPhrase.setTempo(190)
            
    # Instrumental Introduction
    mainGuitarPhrase.addNoteList(Notes.PPP1, Notes.DDD1)
    mainGuitarPhrase.addNoteList(Notes.PPP1, Notes.DDD1)
    mainGuitarPhrase.addNoteList(Notes.PPP2, Notes.DDD2)
    mainGuitarPhrase.addNoteList(Notes.PPP3, Notes.DDD3)
    mainGuitarPhrase.addNoteList(Notes.PPP4, Notes.DDD4)
    mainGuitarPhrase.addNoteList(Notes.PPP3, Notes.DDD3)
    mainGuitarPhrase.addNoteList(Notes.PPP5, Notes.DDD5)
    mainGuitarPhrase.addNoteList(Notes.PPP6, Notes.DDD6)
    
    # Voice Start
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP8), Notes.DDD8)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP9), Notes.DDD9)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP10), Notes.DDD10)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP11), Notes.DDD11)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP12), Notes.DDD12)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP13), Notes.DDD13)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP14), Notes.DDD14)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP15), Notes.DDD15) # **
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP8), Notes.DDD8)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP9), Notes.DDD9)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP10), Notes.DDD10)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP11), Notes.DDD11)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP12), Notes.DDD12)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP16), Notes.DDD16)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP17), Notes.DDD17)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP18), Notes.DDD18)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP19), Notes.DDD19)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP20), Notes.DDD20)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP21), Notes.DDD21)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP22), Notes.DDD22)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP23), Notes.DDD23)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP24), Notes.DDD24)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP25), Notes.DDD25)
    
    # Instrumental
    mainGuitarPhrase.addNoteList(Notes.PPP26, Notes.DDD26)
    
    # Voice Continue
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP27), Notes.DDD27)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP28), Notes.DDD28)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP29), Notes.DDD29)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP30), Notes.DDD30)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP31), Notes.DDD31)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP32), Notes.DDD32)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP33), Notes.DDD33)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP34), Notes.DDD34)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP35), Notes.DDD35)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP8), Notes.DDD8)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP7), Notes.DDD7)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP36), Notes.DDD36)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP10), Notes.DDD10)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP11), Notes.DDD11)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP12), Notes.DDD12)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP16), Notes.DDD16)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP17), Notes.DDD17)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP18), Notes.DDD18)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP19), Notes.DDD19)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP20), Notes.DDD20)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP21), Notes.DDD21)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP22), Notes.DDD22)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP37), Notes.DDD37)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP24), Notes.DDD24)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP38), Notes.DDD38)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP39), Notes.DDD39)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP40), Notes.DDD40)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP41), Notes.DDD41)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP42), Notes.DDD42)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP39), Notes.DDD39)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP43), Notes.DDD43)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP44), Notes.DDD44)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP45), Notes.DDD45)
    
    # Instrumental
    mainGuitarPhrase.addNoteList(Notes.PPP46, Notes.DDD46)
    mainGuitarPhrase.addNoteList(Notes.PPP47, Notes.DDD47)
    mainGuitarPhrase.addNoteList(Notes.PPP48, Notes.DDD48)
    mainGuitarPhrase.addNoteList(Notes.PPP49, Notes.DDD49)
    mainGuitarPhrase.addNoteList(Notes.PPP50, Notes.DDD50)
    mainGuitarPhrase.addNoteList(Notes.PPP51, Notes.DDD51)
    mainGuitarPhrase.addNoteList(Notes.PPP52, Notes.DDD52)
    mainGuitarPhrase.addNoteList(Notes.PPP52, Notes.DDD53)
    mainGuitarPhrase.addNoteList(Notes.PPP54, Notes.DDD54)
    
    # Voice Continue
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP55), Notes.DDD55)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP56), Notes.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP57), Notes.DDD57)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP58), Notes.DDD58)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP59), Notes.DDD59)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP60), Notes.DDD60)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP56), Notes.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP61), Notes.DDD61)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP62), Notes.DDD62)
    
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP63), Notes.DDD63)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP56), Notes.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP64), Notes.DDD64)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP65), Notes.DDD65)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP66), Notes.DDD66)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP56), Notes.DDD56)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP61), Notes.DDD61)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP62), Notes.DDD62)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP67), Notes.DDD67)
    mainGuitarPhrase.addNoteList(BeQuiet(Notes.PPP68), Notes.DDD68)
    
    # Finalizing with Instrumental Part
    mainGuitarPhrase.addNoteList(Notes.PPP3, Notes.DDD3)
    mainGuitarPhrase.addNoteList(Notes.PPP5, Notes.DDD5)
    mainGuitarPhrase.addNoteList(Notes.PPP69, Notes.DDD69)

    guitarPart.addPhrase(mainGuitarPhrase)
    
    return guitarPart