import time
import random
import pygame
import math
import music
import config
from button import Button
import health
from player import Player
from character import Character

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
        self.blitPortrait()
        self.bar = health.Bar(config.white, config.CHAR_DETAIL_FONT_LARGE, (1285, 500), gameDisplay)

    def genText(self):
        name = str(self.name)
        clas = str(self.type)
        self.rend = self.font.render(name, True, config.red)
        self.rend2 = self.font.render(clas, True, config.red)

    def setRect(self):
        self.genText()
        self.rect = self.rend.get_rect()
        self.rect2 = self.rend.get_rect()
        self.rect.center = self.pos
        #Calculate offset needed for Major/class text
        newpos = ((1280, 450))
        self.rect2.center = newpos

    def blitText(self):
        self.genText()
        # Commented out the below blit because we don't have naming the character implemented yet.
        #self.display.blit(self.rend, self.rect)
        self.display.blit(self.rend2, self.rect2)

    def blitPortrait(self):
        image = "assets/portraits/" + self.type + ".png"
        image_surface = pygame.image.load(image)
        self.display.blit(image_surface, (1380, 420))