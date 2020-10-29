import pygame
import config
from items import Item

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class Equipment:
    def __init__(self):
        self.rows = 2
        self.col = 3
        
        '''
        #For Menu that shows when right-click item
        self.itemMenuClicked = False
        self.itemMousePos = None
        self.itemMenu = None
        self.currentItem = None
        self.itemBox = None

        #For Description box that shows when clicking Info Option
        self.infoBoxClicked = False
        self.infoBox = None

        #items[x][y][0] is the item
        #items[x][y][1] is item count
        self.items = [[None for _ in range(self.rows)] for _ in range(self.col)]
        '''     

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
        self.x = 200
        self.y = 200

        #border thiccness
        self.border = 10
        self.borderRect = pygame.Rect(self.x,self.y
        ,(self.box_size + self.border)*self.col
        ,(self.box_size + self.border)*self.rows)

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
                        obj = config.SPOOKY_INVENTORY_FONT.render("1", True, config.white)
                        outline = config.SPOOKY_INVENTORY_OUTLINE.render("1", True, config.black)
                        gameDisplay.blit(outline, (rect[0] + self.box_size // 2 + 10, rect[1] + self.box_size // 2 + 2))
                        gameDisplay.blit(obj, (rect[0] + self.box_size // 2 + 10, rect[1] + self.box_size // 2 + 2))  

    def equipItem(self, item):
        old_item = None
        if (item[0].equip_type == "Weapon"):
            old_item = self.equipment[(1,1)]
            self.equipment[(1,1)] = item                
            return old_item
        return old_item
