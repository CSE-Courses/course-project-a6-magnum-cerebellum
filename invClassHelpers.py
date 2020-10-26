import pygame
import config

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

#CLASSES START HERE
###Below for Inventory

class Inventory:
    def __init__(self):
        self.rows = 4
        self.col = 8

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


        # This draws the inside boxes
        for x in range(self.col):
            for y in range(self.rows):

                rect = ((self.x + (self.box_size + self.border) * x + self.border)
                        , self.y + (self.box_size + self.border) * y + self.border
                        , self.box_size
                        , self.box_size)
                pygame.draw.rect(gameDisplay, config.gray, rect)

                # Render the items
                if self.items[x][y]:
                    gameDisplay.blit(self.items[x][y][0].resize(self.box_size), rect)
                    obj = config.SPOOKY_INVENTORY_FONT.render(str(self.items[x][y][1]), True, (0, 0, 0))
                    gameDisplay.blit(obj, (rect[0] + self.box_size // 2, rect[1] + self.box_size // 2))

    def createItemMenu(self, boxPos, currentItem, mousePos):
        self.itemBox = boxPos
        self.currentItem = currentItem
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

###Below for right-clicking item menu

class itemOptionMenu:
    def __init__(self, mousePosition, item):
        self.itemType = item.item_type
        
        #size of the box itself
        self.box_size = 30
        self.numberOfBoxes = None
        
        #x, y position of the inventory
        self.menuX = mousePosition[0]
        self.menuY = mousePosition[1]

        #border thiccness
        self.border = 5
        self.borderRect = None

        #Menu options to select from
        self.optionsTextArray = []
        self.optionsRects = []

    def createOptions(self):
        #draw border box
        self.borderRect = pygame.Rect(self.menuX, self.menuY, (self.box_size + self.border) + 77, (self.box_size + self.border) * self.numberOfBoxes + self.border)

        pygame.draw.rect(gameDisplay,config.black,self.borderRect)

        #draw the inside 
        for col in range(1):

            for row in range (self.numberOfBoxes):
                boxRect = pygame.Rect(  (self.menuX + self.border), self.menuY + (self.box_size + self.border) * row + self.border, self.box_size + 72, self.box_size  )
                
                pygame.draw.rect(gameDisplay,config.gray,boxRect)

                text = config.SPOOKY_INVENTORY_FONT.render(self.optionsTextArray[row], True, config.red)
                text_rect = text.get_rect(center=boxRect.center)
                self.optionsRects.append(boxRect)

                gameDisplay.blit(text, text_rect)

    def populateOptionsArray(self):
        self.numberOfBoxes = 4
        if (self.itemType == "Equip"):
            self.optionsTextArray.extend( ["Info","Equip", "Discard One", "Discard All"] )
        elif (self.itemType == "Consumable"):
            self.optionsTextArray.extend( ["Info","Use", "Discard One", "Discard All"] )

###Below for info options box

class infoBox:
    def __init__(self, mousePosition, item_desc, item_name, item_type):
        #size of the box itself
        self.box_size = 30
        self.item_desc = item_desc
        self.item_name = item_name
        self.item_type = item_type
        #x, y position of the inventory
        self.menuX = mousePosition[0]
        self.menuY = mousePosition[1]

        #border thiccness
        self.border = 5
        self.borderRect = None

    def createInfo(self):
        #draw border box
        self.borderRect = pygame.Rect(self.menuX, self.menuY, (self.box_size + self.border) + 205, self.box_size + 115  + self.border*2)

        pygame.draw.rect(gameDisplay,config.black,self.borderRect)

        #Left, Top, Width, Height
        #draw the inside 
        itemNameBox = pygame.Rect(  (self.menuX + self.border), self.menuY + self.border, self.box_size + 200, self.box_size + 10)
        itemTypeBox = pygame.Rect(  (self.menuX + self.border), self.menuY + 40, self.box_size + 200, self.box_size)
        itemDescBox = pygame.Rect ( (self.menuX + self.border), self.menuY + 60, self.box_size + 200, self.box_size + 60 ) 

        #drawText wraps from the top left, so create three separate boxes for the Item Name, Description, Type Box
        pygame.draw.rect(gameDisplay,config.gray,itemNameBox)
        pygame.draw.rect(gameDisplay,config.gray,itemTypeBox)
        pygame.draw.rect(gameDisplay,config.gray,itemDescBox)

        config.SPOOKY_INVENTORY_FONT.set_underline(True)
        drawText(gameDisplay, self.item_name, config.black, itemNameBox, config.SPOOKY_INVENTORY_FONT)
        drawText(gameDisplay, self.item_type, config.black, itemTypeBox, config.SPOOKY_ITEM_FONT)
        config.SPOOKY_INVENTORY_FONT.set_underline(False)
        drawText(gameDisplay, self.item_desc, config.red, itemDescBox, config.SPOOKY_INVENTORY_FONT)

#CLASSES END HERE

#Helper Below

#Provides wrap-around text into the rect provided
#https://www.pygame.org/wiki/TextWrap

def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width+5 and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def blitItemMenu(inventory):
    inventory.itemMenu = itemOptionMenu(inventory.itemMousePos, inventory.currentItem[0])
    inventory.itemMenu.populateOptionsArray()
    inventory.itemMenu.createOptions()
    pygame.display.update()

def blitInfoBox(inventory):
    inventory.infoBox = infoBox(inventory.itemMousePos, inventory.currentItem[0].item_desc, inventory.currentItem[0].item_name, inventory.currentItem[0].item_type)
    inventory.infoBox.createInfo()
    pygame.display.update()