#######################################################################################################
# Credits to TheBigKahuna353 on Reddit/Github for his sample inventory system which this is based off #
#######################################################################################################

#Import random nubmer picker for prototype inventory, remove later
import random
####

import pygame
import config
import random
from button import Button
from items import Item
import itemMenu

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class Inventory:
    def __init__(self):
        self.rows = 4
        self.col = 8

        #items[x][y][0] is the item
        #items[x][y][1] is item count
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        
        #size of the box itself
        self.box_size = 50

        #x, y position of the inventory
        self.x = 400
        self.y = 400

        #border thiccness
        self.border = 5
        self.borderRect = pygame.Rect(self.x,self.y
        ,(self.box_size + self.border)*self.col
        ,(self.box_size + self.border)*self.rows)

    def createInventory(self):

        #This draws the borders
        pygame.draw.rect(gameDisplay,(100,100,100),
                         (self.x
                         ,self.y
                         ,(self.box_size + self.border)*self.col + self.border
                         ,(self.box_size + self.border)*self.rows + self.border))

        #This draws the inside boxes
        for x in range(self.col):
            for y in range(self.rows):
                rect = ( (self.x + (self.box_size + self.border)*x + self.border )  
                ,  self.y + (self.box_size + self.border)*y + self.border 
                , self.box_size 
                , self.box_size )
                pygame.draw.rect(gameDisplay,config.gray,rect)
                
                #Render the items
                if self.items[x][y]:
                    gameDisplay.blit(self.items[x][y][0].resize(self.box_size),rect)
                    obj = config.SPOOKY_INVENTORY_FONT.render(str(self.items[x][y][1]),True,(0,0,0))
                    gameDisplay.blit(obj,(rect[0] + self.box_size//2, rect[1] + self.box_size//2))
                    
    #Get the box position that the mouse is over
    def boxPos(self):
        mouse = pygame.mouse.get_pos()
        
        x = mouse[0] - self.x
        y = mouse[1] - self.y

        #Use // to truncate to int
        x = x//(self.box_size + self.border)
        y = y//(self.box_size + self.border)
        return (x,y)
    
    #Add the item to the inventory, if there's a item already being selected, swap their positions
    def addToInventory(self, Item, position):
        row, col = position
        
        #If something contained in that box
        if self.items[row][col]:
            #If it's the same item, stack it
            if self.items[row][col][0].item_name == Item[0].item_name:
                
                #This is the number of that particular item
                #Item[1] allows it to stack multiple numbers, not just increase by 1
                self.items[row][col][1] += Item[1]

            #Otherwise swap the two items
            else:
                heldItem = self.items[row][col]
                self.items[row][col] = Item
                return heldItem
        #Nothing in box, so just place the Item
        else:
            self.items[row][col] = Item

    def discardFromInventory(self, Item, position, discardAmount):
        row, col = position

        if self.items[row][col]:
            
            if self.items[row][col][1] > 1 and discardAmount == "Discard One":
                self.items[row][col][1] -= 1
            else:
                self.items[row][col] = None

def inventoryMain():
    #Creates inventory
    player_inventory = Inventory()
    
    #The item the cursor is holding
    heldItem = None

    while True:
        #Re-fills display everytime
        gameDisplay.fill(config.white)    

        #Draw the inventory
        player_inventory.createInventory()

        #Get the position of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        #If an item is selected, hold it
        if heldItem:
            gameDisplay.blit(heldItem[0].resize(30),(mouseX,mouseY))
            obj = config.SPOOKY_INVENTORY_FONT.render(str(heldItem[1]),True,(0,0,0))
            gameDisplay.blit(obj,(mouseX + 15, mouseY + 15))  

        #Update display
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            
            #Below code used for item placement
            
            #Get the player's mouse position
            pos = player_inventory.boxPos()
            
            #If it's a left-click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            

                #Only if mouse position is within the inventory, do stuff with Item
                if player_inventory.borderRect.collidepoint(pygame.mouse.get_pos()):

                    #If item being held use addToInventory
                    if heldItem:
                        heldItem = player_inventory.addToInventory(heldItem, pos)

                    #Grabs item from the box as heldItem, then sets box to nothing    
                    elif player_inventory.items[pos[0]][pos[1]]:
                        #Array of Two
                        heldItem = player_inventory.items[pos[0]][pos[1]]
                        player_inventory.items[pos[0]][pos[1]] = None

            #Change this to options menu? Like if right-clicking consumable bring up a Use/Discord option
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:

                #If it's within a
                if player_inventory.borderRect.collidepoint(pygame.mouse.get_pos()) and player_inventory.items[pos[0]][pos[1]]:
                    item = player_inventory.items[pos[0]][pos[1]]

                    optionSelected = itemMenu.itemOptions(item[0].item_name, item[0].item_desc, item[0].item_type, player_inventory)

                    if ("Discard" in optionSelected):
                        player_inventory.discardFromInventory(item, pos, optionSelected)
                
                #TEMP: If it's a right click just grab a computer
                #Remove later when putting everything together
                elif heldItem == None:
                    randomItemPicker = [Item("Computer"), Item("Red Bull")]
                    heldItem = [randomItemPicker[random.randint(0,1)], 1]

#Uncomment these if you want to directly launch from inventory.py for faster debugging/testing
#inventoryMain()
#quit()