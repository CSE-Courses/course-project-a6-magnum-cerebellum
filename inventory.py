import pygame
import config
import random
from button import Button

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class Inventory:
    def __init__(self):
        self.rows = 1
        self.col = 8
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        self.box_size = 50
        self.x = 400
        self.y = 400
        self.border = 5
        self.borderRect = pygame.Rect(self.x,self.y,(self.box_size + self.border)*self.col,(self.box_size + self.border)*self.rows)

    def createInventory(self):

        #This draws the borders
        pygame.draw.rect(gameDisplay,(100,100,100),
                         (self.x,self.y,(self.box_size + self.border)*self.col + self.border,(self.box_size + self.border)*self.rows + self.border))

        #This draws the inside boxes
        for x in range(self.col):
            for y in range(self.rows):
                rect = ( (self.x + (self.box_size + self.border)*x + self.border )  ,  self.x + (self.box_size + self.border)*y + self.border , self.box_size , self.box_size )
                pygame.draw.rect(gameDisplay,config.gray,rect)
                
                #Item
                #if self.items[x][y]:
                #    gameDisplay.blit(self.items[x][y][0].resize(self.box_size),rect)
                #    obj = config.SPOOKY_INVENTORY_FONT.render(str(self.items[x][y][1]),True,(0,0,0))
                #    gameDisplay.blit(obj,(rect[0] + self.box_size//2, rect[1] + self.box_size//2))
                    
    #Get the box position that the mouse is over
    def boxPos(self):
        mouse = pygame.mouse.get_pos()
        
        x = mouse[0] - self.x
        y = mouse[1] - self.y
        x = x/(self.box_size + self.border)
        y = y/(self.box_size + self.border)
        return (x,y)
    
    
    
def inventoryMain():
    player_inventory = Inventory()
    gameDisplay.fill(config.white)    

    while True:

        #Draw the inventory
        player_inventory.createInventory()

        mouseX, mouseY = pygame.mouse.get_pos()
        
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            #Below code used for potential items, but no item class yet
            
            #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #    pos = player_inventory.boxPos()
            #    if player_inventory.borderRect.collidepoint(pygame.mouse.get_pos()):
            #        if player_inventory.items[pos[0]][pos[1]]:
            #            selected = player_inventory.items[pos[0]][pos[1]]
            #            player_inventory.items[pos[0]][pos[1]] = None


#Uncomment these if you want to run from inventory.py for faster debugging/testing

#inventoryMain()
#quit()