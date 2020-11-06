import time
import random
import pygame
import math
import music
import config
from button import Button
import inventory
from player import Player
from character import Character
from inventory import inventoryMain
import game

#####################################################################################
#This provides the function for blitting the character name and Major
#####################################################################################

class char_ui:
    def __init__(self, font, pos, name, character, gameDisplay):
        self.font = font
        self.pos = pos
        self.display = gameDisplay
        self.char = character
        self.type = character.__str__()
        self.name = name

        self.setRect()
        self.blitText()

    def genText(self):
        name = str(self.name)
        #clas = str(self.type)
        self.rend = self.font.render(name, True, config.black)
        #self.rend2 = self.font.render(clas, True, config.black)

    def setRect(self):
        self.genText()
        self.rect = self.rend.get_rect()
        #self.rect2 = self.rend.get_rect()
        self.rect.center = self.pos
        #Calculate offset needed for Major/class text
        newpos = ((930, 70))
        #self.rect2.center = newpos

    def blitText(self):
        self.genText()
        self.display.blit(self.rend, self.rect)
        #self.display.blit(self.rend2, self.rect2)