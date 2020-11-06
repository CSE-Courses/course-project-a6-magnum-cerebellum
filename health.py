import time
import random
import pygame
import math
import music
import config
from button import Button

#####################################################################################
#This provides the functions for computing and displaying health/mana bars.
#####################################################################################

class Bar:

    def __init__(self, color, font, pos, gameDisplay):
        self.color = color
        self.font = font
        self.pos = pos
        #self.rend  # Used for rendering
        self.lowflag = False # Flag set when health is =< 25% total health, will be implemented further
        self.display = gameDisplay
        # This initialization will be changed according to character stats once set up
        self.totalhealth = 100
        self.totalmana = 100
        #
        self.currenthealth = self.totalhealth
        self.currentmana = self.totalmana

        self.set_rect()
        self.createBar()


    def barText(self):
        bar = "HP: " + str(self.currenthealth) + " / " + str(self.totalhealth)
        bar2 = "MP: " + str(self.currentmana) + " / " + str(self.totalmana)
        self.rend2 = self.font.render(bar2, True, self.color)
        # if self.currenthealth / self.totalhealth <= .25:
        #     bar = "MP: " + str(self.currentmana) + " / " + str(self.totalmana)
        # else:
        #     bar = "HP: " + str(self.currenthealth) + " / " + str(self.totalhealth)
        #     bar2 = "MP: " + str(self.currentmana) + " / " + str(self.totalmana)
        #     self.rend2 = self.font.render(bar2, True, self.color)
        self.rend = self.font.render(bar, True, self.color)


    def set_health(self, health):
        self.currenthealth = health
        #self.updateBar()

    def createBar(self):
        self.barText()
        self.display.blit(self.rend, self.rect)
        self.display.blit(self.rend2, self.rect2)

    def set_rect(self):
        self.barText()
        self.rect = self.rend.get_rect()
        self.rect2 = self.rend.get_rect()
        self.rect.center = self.pos
        # Calculate offset needed for second bar
        newpos = ((self.pos[0], self.pos[1] + 50))
        self.rect2.center = newpos

    def clearBar(self, color):
        self.rend.fill((color))
        self.rend2.fill((color))

    def updateBar(self):
        self.barText()
        # Check if we should render health as red first
        if self.currenthealth / self.totalhealth <= .25:
            healthBar = "HP: " + str(self.currenthealth) + " / " + str(self.totalhealth)
            self.display.blit(self.font.render(healthBar, True, config.red), self.rect)
            self.display.blit(self.rend2, self.rect2)
        else:
            # This should overwrite the previous blits? Will need to test
            self.display.blit(self.rend, self.rect)
            self.display.blit(self.rend2, self.rect2)


    def subtractHealth(self, lost):
        self.currenthealth -= lost
        if (self.currenthealth < 0): self.currenthealth = 0
        self.updateBar()

    def addHealth(self, gain):
        self.currenthealth += gain
        if (self.currenthealth > 100): self.currenthealth = 100
        self.updateBar()

    def subtractMana(self, lost):
        self.currentmana -= lost
        if (self.currentmana < 0): self.currentmana = 0
        self.updateBar()

    def addMana(self, gain):
        self.currentmana += gain
        if (self.currentmana > 100): self.currentmana = 0
        self.updateBar()






