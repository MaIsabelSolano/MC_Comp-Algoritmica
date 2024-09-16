# Universidad del valle de Guatemala
# Facultad de Ingenieria
# Departamento de Ciencias de la Computacion
# Musica computacional
# Ma. Isabel Solano 20504
# Cristian Laynez 201281

# Piano

from music import *

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

    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8)
    mainPianoPhrase.addNoteList(NotesSecundaryMelody.PPP8, NotesSecundaryMelody.DDD8_1)

    # Main Choir
       
    pianoPart.addPhrase(mainPianoPhrase)
    
    return pianoPart
