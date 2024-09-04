# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Trombone

from music import *

import NotesMainMelody

from Utils import BeQuiet

def TrombonePart():
    trombonePart = Part(TROMBONE, 2)
    mainTrombonePhrase = Phrase()
    mainTrombonePhrase.setTempo(190)
    
    # Instrumental Introduction
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP1), NotesMainMelody.DDD1)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP1), NotesMainMelody.DDD1)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP2), NotesMainMelody.DDD2)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP3), NotesMainMelody.DDD3)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP4), NotesMainMelody.DDD4)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP3), NotesMainMelody.DDD3)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP5), NotesMainMelody.DDD5)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP6), NotesMainMelody.DDD6)
    
    # Voice Start
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP8, NotesMainMelody.DDD8)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP9, NotesMainMelody.DDD9)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP10, NotesMainMelody.DDD10)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP11, NotesMainMelody.DDD11)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP12, NotesMainMelody.DDD12)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP13, NotesMainMelody.DDD13)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP14, NotesMainMelody.DDD14)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP15, NotesMainMelody.DDD15)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP8, NotesMainMelody.DDD8)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP9, NotesMainMelody.DDD9)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP10, NotesMainMelody.DDD10)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP11, NotesMainMelody.DDD11)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP12, NotesMainMelody.DDD12)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP16, NotesMainMelody.DDD16)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP17, NotesMainMelody.DDD17)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP18, NotesMainMelody.DDD18)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP19, NotesMainMelody.DDD19)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP20, NotesMainMelody.DDD20)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP21, NotesMainMelody.DDD21)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP22, NotesMainMelody.DDD22)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP23, NotesMainMelody.DDD23)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP24, NotesMainMelody.DDD24)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP25, NotesMainMelody.DDD25)
    
    # Instrumental
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP26), NotesMainMelody.DDD26)
    
    # Voice Continue
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP27, NotesMainMelody.DDD27)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP28, NotesMainMelody.DDD28)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP29, NotesMainMelody.DDD29)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP30, NotesMainMelody.DDD30)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP31, NotesMainMelody.DDD31)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP32, NotesMainMelody.DDD32)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP33, NotesMainMelody.DDD33)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP34, NotesMainMelody.DDD34)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP35, NotesMainMelody.DDD35)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP8, NotesMainMelody.DDD8)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP7, NotesMainMelody.DDD7)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP36, NotesMainMelody.DDD36)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP10, NotesMainMelody.DDD10)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP11, NotesMainMelody.DDD11)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP12, NotesMainMelody.DDD12)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP16, NotesMainMelody.DDD16)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP17, NotesMainMelody.DDD17)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP18, NotesMainMelody.DDD18)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP19, NotesMainMelody.DDD19)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP20, NotesMainMelody.DDD20)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP21, NotesMainMelody.DDD21)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP22, NotesMainMelody.DDD22)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP37, NotesMainMelody.DDD37)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP24, NotesMainMelody.DDD24)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP38, NotesMainMelody.DDD38)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP39, NotesMainMelody.DDD39)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP40, NotesMainMelody.DDD40)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP41, NotesMainMelody.DDD41)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP42, NotesMainMelody.DDD42)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP39, NotesMainMelody.DDD39)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP43, NotesMainMelody.DDD43)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP44, NotesMainMelody.DDD44)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP45, NotesMainMelody.DDD45)
    
    # Instrumental
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP46), NotesMainMelody.DDD46)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP47), NotesMainMelody.DDD47)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP48), NotesMainMelody.DDD48)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP49), NotesMainMelody.DDD49)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP50), NotesMainMelody.DDD50)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP51), NotesMainMelody.DDD51)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP52), NotesMainMelody.DDD52)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP52), NotesMainMelody.DDD53)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP54), NotesMainMelody.DDD54)
    
    # Voice Continue
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP55, NotesMainMelody.DDD55)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP56, NotesMainMelody.DDD56)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP57, NotesMainMelody.DDD57)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP58, NotesMainMelody.DDD58)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP59, NotesMainMelody.DDD59)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP60, NotesMainMelody.DDD60)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP56, NotesMainMelody.DDD56)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP61, NotesMainMelody.DDD61)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP62, NotesMainMelody.DDD62)
    
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP63, NotesMainMelody.DDD63)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP56, NotesMainMelody.DDD56)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP64, NotesMainMelody.DDD64)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP65, NotesMainMelody.DDD65)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP66, NotesMainMelody.DDD66)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP56, NotesMainMelody.DDD56)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP61, NotesMainMelody.DDD61)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP62, NotesMainMelody.DDD62)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP67, NotesMainMelody.DDD67)
    mainTrombonePhrase.addNoteList(NotesMainMelody.PPP68, NotesMainMelody.DDD68)
    
    # Finalizing with Instrumental Part
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP3), NotesMainMelody.DDD3)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP5), NotesMainMelody.DDD5)
    mainTrombonePhrase.addNoteList(BeQuiet(NotesMainMelody.PPP69), NotesMainMelody.DDD69)
    
    trombonePart.addPhrase(mainTrombonePhrase)
    
    return trombonePart