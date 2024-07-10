# Imports go at the top
from microbit import *
import music
Introp1 = ["r:192","r:12","G3:24","G3:24","G3:24","F3:6","G3:6","G3:12","G3:24","G3:18","F#4:6","F4:6","Eb4:6"]
Introp2 = ["D4:42","r:6","r:48","r:8","Eb4","D4","C4","Bb3","A3","C4","Bb3","A3","F#3:30","r:42","r:48","r","F3:3","G3","r:6","G3:12","Bb3:3","G3","r:6","G3:12"]
Introp3 = ["G3:96","G3"]
BassLine1 = ["G3:6","F3","G3","Bb3","C4","Bb3","C#4","D4"]
BassLine2 = ["G4:6","G4","F#4","F#4","F4","F4","Eb4","D4"]

set_volume(75)
music.set_tempo(ticks=12,bpm=120)
while True:
    if button_a.was_pressed():
        #page 1
        music.play(Introp1)
        #page 2
        music.play(Introp2)
        #page 3
        music.play(Introp3)
        for i in range(3):
            music.play(BassLine1)
        music.play(BassLine2)
        #page 4
        for i in range(2):
            for i in range(3):
                music.play(BassLine1)
            music.play(BassLine2)
        #page 5
        for i in range(3):
            music.play(BassLine1)
        music.play(BassLine2)
        for i in range(4):
            music.play(BassLine1)
        #page 6
        for i in range(3):
            music.play(BassLine1)
        music.play(BassLine2)
        music.play(["D5:12","C#5","C5","B4","Bb4:6","A4","G4","Eb4","D4:18","r:6","D4:78","r:6","D4:12"])
        #page 7
        music.play(["r:12","D4","C#4","C4","B3:8","Bb3","A3","Ab3","G3","F#3","G3:78","r:6","D4:12"])
        for i in range(3):
            music.play(BassLine1)
        music.play(BassLine2)
        #page 8
