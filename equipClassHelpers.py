import pygame
import config
from items import Item
from invClassHelpers import itemOptionMenu
from invClassHelpers import infoBox

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class Equipment:
    def __init__(self):
        self.rows = 2
        self.col = 3

        #For Menu that shows when right-click equip
        self.itemMenuClicked = False
        self.itemMousePos = None
        self.itemMenu = None
        self.itemBox = None

        #For Description box that shows when clicking Info Option
        self.infoBoxClicked = False
        self.infoBox = None

        #Set this to an item!
        self.equipment = {
            (1, 0) : None, #Helmet
            (0, 1) : None, #Armor
            (1, 1) : None, #Weapon
            (2, 1) : None  #Shoes
        }

        #size of the box itself
        self.box_size = 65

        #x, y position of the inventory
        self.x = 1250
        self.y = 630

        #border thiccness
        self.border = 10
        self.borderRect = pygame.Rect(self.x,self.y
        ,(self.box_size + self.border)*self.col
        ,(self.box_size + self.border)*self.rows)

    #Redraws the Equipment GUI
    def createEquip(self):

        #This draws the borders
        pygame.draw.rect(gameDisplay,(100,100,100),
                         ( (self.x + self.box_size + self.border)
                         ,self.y
                         ,(self.box_size + self.border) + self.border
                         ,(self.box_size + self.border) + self.border))

        pygame.draw.rect(gameDisplay,(100,100,100),
                         ( self.x
                         , (self.y + self.box_size + self.border)
                         ,(self.box_size + self.border)*self.col + self.border
                         ,(self.box_size + self.border) + self.border))

        # This draws the inside boxes
        for x in range(0, self.col):
            for y in range(0, self.rows):
                if ((x,y) != (0,0) and (x,y) != (2,0)):
                    rect = ((self.x + (self.box_size + self.border) * x + self.border)
                            , self.y + (self.box_size + self.border) * y + self.border
                            , self.box_size
                            , self.box_size)
                    pygame.draw.rect(gameDisplay, config.gray, rect)

                    if self.equipment[(x,y)]:
                        gameDisplay.blit(self.equipment[(x,y)][0].resize(self.box_size), rect)

    def createEquipItemMenu(self, boxPos, mousePos):
        self.itemBox = boxPos
        self.itemMousePos = mousePos
        self.itemMenuClicked = True

    # Get the box position that the mouse is over
    def boxPos(self):
        mouse = pygame.mouse.get_pos()

        x = mouse[0] - self.x
        y = mouse[1] - self.y

        #Use // to truncate to int
        x = x//(self.box_size + self.border)
        y = y//(self.box_size + self.border)
        return (x,y)

    #To be Implemented : Decreasing player's stats after equip/unequip
    def equipItem(self, item):
        old_item = None
        if (item[0].equip_type == "Weapon"):
            config.text1.append("equipped a " + str(item[0].item_name))
            old_item = self.equipment[(1,1)]
            self.equipment[(1,1)] = item
        elif (item[0].equip_type == "Helmet"):
            old_item = self.equipment[(1,0)]
            self.equipment[(1,0)] = item
        elif (item[0].equip_type == "Armor"):
            old_item = self.equipment[(0,1)]
            self.equipment[(0,1)] = item
        elif (item[0].equip_type == "Shoes"):
            old_item = self.equipment[(2,1)]
            self.equipment[(2,1)] = item       

        return old_item
    '''
    Need to make sure here you return the equipped item to the first inventory slot free
    If none free, don't unequip.
    '''    
    #Later on, include the player so can edit the player's items
    def unequipItem(self, equipment, inventory):
        equippedItem = equipment.equipment[equipment.itemBox]
        for x in range(self.rows):
            for y in range(self.col):
                if inventory.items[y][x] == None:
                    inventory.items[y][x] = equippedItem
                    equipment.equipment[equipment.itemBox] = None
                    return equippedItem[0].equip_type, equippedItem[0].amount
        return None

def blitEquipItemMenu(equipment):
    equipment.itemMenu = itemOptionMenu(equipment.itemMousePos, equipment.equipment[equipment.itemBox][0])
    equipment.itemMenu.populateEquipOptions()
    equipment.itemMenu.createOptions()


def blitEquipInfoBox(equipment):
    currentItem = equipment.equipment[equipment.itemBox]
    equipment.infoBox = infoBox(equipment.itemMousePos, currentItem[0])
    equipment.infoBox.createInfo()
