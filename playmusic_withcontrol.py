#pip install pygame

#Hide pygame support message during import pygame
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

from pygame import mixer

file = "music.mp3"

mixer.init()
mixer.music.load(file)
PAUSE = 0
q = input("Press <ENTER> to play")
while True:
    if mixer.music.get_busy() == False:
        mixer.music.play()
        q = input("Press <ENTER> to pause")
    else:
        if q == "" and PAUSE == 0:
            mixer.music.pause()
            PAUSE = 1
            q = input("Press <ENTER> to play")   
        elif q == "" and PAUSE == 1:
            mixer.music.unpause()
            PAUSE = 0
            q = input("Press <ENTER> to pause")   
     
