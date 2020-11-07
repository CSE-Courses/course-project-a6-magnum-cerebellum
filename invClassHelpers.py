import pygame
import config
from items import Item

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
        self.x = 500
        self.y = 550

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
                    if self.items[x][y][0].item_type != "Equip":
                        obj = config.SPOOKY_INVENTORY_FONT.render(str(self.items[x][y][1]), True, config.white)
                        outline = config.SPOOKY_INVENTORY_OUTLINE.render(str(self.items[x][y][1]), True, config.black)
                        gameDisplay.blit(outline, (rect[0] + self.box_size // 2 + 10, rect[1] + self.box_size // 2 + 2))
                        gameDisplay.blit(obj, (rect[0] + self.box_size // 2 + 10, rect[1] + self.box_size // 2 + 2))

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
            if (self.items[row][col][0].item_name == Item[0].item_name
                and self.items[row][col][0].item_type != "Equip"):
                
                #This is the number of that particular item
                #Item[1] allows it to stack multiple numbers, not just increase by 1
                self.items[row][col][1] += Item[1]
                config.text1 = config.text1 + ["added a " + str(self.items[row][col][0].item_name)]

            #Otherwise swap the two items

            else:
                heldItem = self.items[row][col]
                self.items[row][col] = Item
                config.text1 = config.text1 + ["swapped items"]

                return heldItem

        
        #Nothing in box, so just place the Item
        else:
            self.items[row][col] = Item
            config.text1 = config.text1 + ["added a " + str(self.items[row][col][0].item_name)]

    def discardFromInventory(self,position, discardAmount):
        row, col = position

        if self.items[row][col]:
            #get rid of 1 item
            if self.items[row][col][1] > 1 and discardAmount == "Discard One":
                config.text1 = config.text1 + ["discarded a " + str(self.items[row][col][0].item_name)]
                self.items[row][col][1] -= 1

            #get rid of all items
            else:
                config.text1 = config.text1 + ["discarded all " + str(self.items[row][col][0].item_name) + "s from inventory"]
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
                boxRect = pygame.Rect(  (self.menuX + self.border), self.menuY + (self.box_size + self.border) * row + self.border, self.box_size + 72, self.box_size)
                self.optionsRects.append(boxRect)

                pygame.draw.rect(gameDisplay,config.gray,boxRect)

                text = config.SPOOKY_INVENTORY_FONT.render(self.optionsTextArray[row], True, config.red)
                
                outline = config.SPOOKY_INVENTORY_FONT.render(self.optionsTextArray[row], True, config.black)
                text_rect = text.get_rect(center=boxRect.center)
                
                #def outlineText(text, font, color, outlineColor, outlineSize):
                gameDisplay.blit(outlineText(self.optionsTextArray[row],config.SPOOKY_INVENTORY_FONT, config.red, config.black, 1, False, 0), text_rect)

    def populateOptionsArray(self):
        self.numberOfBoxes = 4
        if (self.itemType == "Equip"):
            self.optionsTextArray.extend( ["Info","Equip", "Discard One"] )
        elif (self.itemType == "Consumable"):
            self.optionsTextArray.extend( ["Info","Use", "Discard One", "Discard All"] )
    
    def populateEquipOptions(self):
        self.numberOfBoxes = 2
        self.optionsTextArray.extend( ["Info", "Unequip"])

###Below for info options box

class infoBox:
    def __init__(self, mousePosition, item):
        #size of the box itself
        self.box_size = 30
        self.item = item
        self.item_desc = item.item_desc
        self.item_name = item.item_name
        self.item_type = item.item_type
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
        
        if (self.item_type == "Equip"):
            if (self.item.equip_type == "Weapon"):
                self.item_type += ": " + "Deals " + str(self.item.damage) + " damage"
        elif (self.item_type == "Consumable"):
            self.item_type += ": " + "Heals " + str(self.item.damage) + " hp"
        drawText(gameDisplay, self.item_name, config.white, itemNameBox, config.SPOOKY_INVENTORY_FONT, 2, config.black)
        drawText(gameDisplay, self.item_type, config.white, itemTypeBox, config.SPOOKY_ITEM_FONT, 2, config.black)

        config.SPOOKY_INVENTORY_FONT.set_underline(False)

        drawText(gameDisplay, self.item_desc, config.red, itemDescBox, config.SPOOKY_INVENTORY_FONT, 1, config.black)

#CLASSES END HERE

#HELPERS BELOW

#Provides wrap-around text into the rect provided
#https://www.pygame.org/wiki/TextWrap

def drawText(surface, text, color, rect, font, outlineSize, outlineColor):
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1
        image = None

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width+5 and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # Render the line and blit it to the surface
        image = font.render(text[:i], True, color)
        surface.blit(outlineText(text, font, color, outlineColor, outlineSize, True, i), (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text

def blitItemMenu(inventory):
    inventory.itemMenu = itemOptionMenu(inventory.itemMousePos, inventory.currentItem[0])
    inventory.itemMenu.populateOptionsArray()
    inventory.itemMenu.createOptions()

def blitInfoBox(inventory):
    currentItem = inventory.currentItem[0]

    inventory.infoBox = infoBox(inventory.itemMousePos, currentItem)
    inventory.infoBox.createInfo()

###This is to give the text an outline since pygame doesn't actually have a support for it
#Condensed version of outline code on https://github.com/lordmauve/pgzero

def outlineText(text, font, color, outlineColor, outlineSize, wraparound, limit):
    textsurface = font.render(text, True, color).convert_alpha()
    outline = font.render(text,True, outlineColor)

    if wraparound :
        textsurface = font.render(text[:limit], True, color).convert_alpha()
        outline = font.render(text[:limit],True, outlineColor)

    w = textsurface.get_width() + 2 * outlineSize
    h = font.get_height()

    outlineSurface = pygame.Surface((w, h + 2 * outlineSize)).convert_alpha()
    outlineSurface.fill((0, 0, 0, 0))

    surf = outlineSurface.copy()

    outlineSurface.blit(outline, (0, 0))

    #Blit the outline on
    for dx, dy in calculateOutline(outlineSize):
        surf.blit(outlineSurface, (dx + outlineSize, dy + outlineSize))

    surf.blit(textsurface, (outlineSize, outlineSize))
    return surf

#Helps calculate the outline to blit around for outlineText
outlineList = {}
def calculateOutline(r):
    r = int(round(r))
    if r in outlineList:
        return outlineList[r]
    x, y, e = r, 0, 1 - r
    outlineList[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points