import pygame
import config
from button import Button
from player import Player

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class BattleUI():
    def __init__(self, player : Player, inventory):
        self.player = player
        self.inventory = inventory

        #x, y position of the Inventory/Battle UI should be same
        self.x = self.inventory.x #550
        self.y = self.inventory.y #550
        self.border = self.inventory.border
        
        #This contains the player's moves
        self.actions = [
        Button(self.player.actions[0], config.black, config.RPG_ACTION_FONT,
            (self.x + self.x/4.5, self.y + self.y/12), gameDisplay),
        Button(self.player.actions[1], config.black, config.RPG_ACTION_FONT,
            (self.x + self.x/4.5, self.y + self.y/5), gameDisplay),
        Button(self.player.actions[2], config.black, config.RPG_ACTION_FONT,
            (self.x + self.x/1.75, self.y + self.y/12), gameDisplay),
        Button(self.player.actions[3], config.black, config.RPG_ACTION_FONT,
            (self.x + self.x/1.75, self.y + self.y/5), gameDisplay),
        Button("Open Inventory", config.white, config.RPG_ACTION_FONT,
            (self.x + self.x/2.5, self.y + self.y/3), gameDisplay)]
        
    def createBattleUI(self):

        #This draws the huge dark gray box
        pygame.draw.rect(gameDisplay,(100,100,100),
                         (self.x
                         ,self.y
                         ,(self.inventory.box_size + self.border)*self.inventory.col + self.border
                         ,(self.inventory.box_size + self.border)*self.inventory.rows + self.border))
        #Left Top Width Height
        borderRect = (self.x + self.border
        , self.y + self.border
        , (self.inventory.box_size + self.border)*self.inventory.col - self.border
        , (self.inventory.box_size + self.border)*self.inventory.rows - self.border)

        pygame.draw.rect(gameDisplay, config.gray, borderRect)

        # This draws the inside boxes
        #for x in range(self.col):
        #    for y in range(self.rows):
#
 #               rect = ((self.x + (self.box_size + self.border) * x + self.border)
  #                      , self.y + (self.box_size + self.border) * y + self.border
   #                     , self.box_size
    #                    , self.box_size)
