# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Piano

from music import *

import NotesMainMelody
import NotesSecundaryMelody
from Utils import BeQuiet

def PianoPart():
    pianoPart = Part()
    mainPianoPhrase = Phrase()
    mainPianoPhrase.setTempo(190)
    
    # Introduction
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP1, NotesSecundaryMelody.DDD1)
    
    # Start Epic Piano
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP2, NotesSecundaryMelody.DDD2)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP2, NotesSecundaryMelody.DDD2)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP2, NotesSecundaryMelody.DDD2)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP2, NotesSecundaryMelody.DDD2)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP3, NotesSecundaryMelody.DDD3)
    mainPianoPhrase.addNoteList(BeQuiet(NotesSecundaryMelody.PPP3), NotesSecundaryMelody.DDD3)
    mainPianoPhrase.addNoteList(BeQuiet(NotesSecundaryMelody.PPP3), NotesSecundaryMelody.DDD3)
    
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP4, NotesSecundaryMelody.DDD4)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP4, NotesSecundaryMelody.DDD4)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP5, NotesSecundaryMelody.DDD5)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP5, NotesSecundaryMelody.DDD5)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP6, NotesSecundaryMelody.DDD6)
    
    # Chords for acompaning the voice - Voice Start
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP7, NotesSecundaryMelody.DDD7)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP7, NotesSecundaryMelody.DDD7)
    
    mainPianoPhrase.addNoteList([REST], [EN])
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8_1)

    # Instrumental Part
    mainPianoPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP26), NotesMainMelody.DDD26)
    
    # mainPianoPhrase.addNoteList([REST], [QN + QN]) # For Testign Apart
    # Main Choir
    mainPianoPhrase.addNoteList([REST], [QN + QN + QN + EN])
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP9, NotesSecundaryMelody.DDD9)
    
    mainPianoPhrase.addNoteList([REST], [QN + WN + HN])    
    # Pre-Choir #2
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP7, NotesSecundaryMelody.DDD7)
    
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8_1)
    
    # Instrumental Part
    mainPianoPhrase.addNoteList(BeQuiet(NotesMainMelody.PPP26), NotesMainMelody.DDD26)
    
    # Main Choir
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP9, NotesSecundaryMelody.DDD9)
       
    pianoPart.addPhrase(mainPianoPhrase)
    
    return pianoPart
