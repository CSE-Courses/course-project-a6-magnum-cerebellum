import pygame
import config

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class itemOptionMenu:
    def __init__(self, mousePosition, itemType):
        self.itemType = itemType
        
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
                boxRect = pygame.Rect(  (self.menuX + self.border)
                    , self.menuY + (self.box_size + self.border) * row + self.border
                    , self.box_size + 72
                    , self.box_size  )
                pygame.draw.rect(gameDisplay,config.gray,boxRect)

                text = config.SPOOKY_INVENTORY_FONT.render(self.optionsTextArray[row], True, config.red)
                text_rect = text.get_rect(center=boxRect.center)
                self.optionsRects.append(text_rect)

                gameDisplay.blit(text, text_rect)

    def populateOptionsArray(self):
        self.numberOfBoxes = 4
        if (self.itemType == "Equip"):
            self.optionsTextArray.extend( ["Info","Equip", "Discard One", "Discard All"] )
        elif (self.itemType == "Consumable"):
            self.optionsTextArray.extend( ["Info","Use", "Discard One", "Discard All"] )

class infoBox:
    def __init__(self, mousePosition, item_desc, item_name):
        #size of the box itself
        self.box_size = 30
        self.item_desc = item_desc
        self.item_name = item_name

        #x, y position of the inventory
        self.menuX = mousePosition[0]
        self.menuY = mousePosition[1]

        #border thiccness
        self.border = 5
        self.borderRect = None

    def createInfo(self):
        #draw border box
        self.borderRect = pygame.Rect(self.menuX, self.menuY, (self.box_size + self.border) + 205, self.box_size + 100  + self.border*2)

        pygame.draw.rect(gameDisplay,config.black,self.borderRect)

        #Left, Top, Width, Height

        #draw the inside 
        itemNameBox = pygame.Rect(  (self.menuX + self.border)
                    , self.menuY + self.border
                    , self.box_size + 200
                    , self.box_size + 10)
        
        itemDescBox = pygame.Rect ( (self.menuX + self.border)
        , self.menuY + self.box_size + 15
        , self.box_size + 200
        , self.box_size + 60 ) 

        #drawText wraps from the top left, so create two seperate boxes for the Item Name and Item Description Box
        pygame.draw.rect(gameDisplay,config.gray,itemNameBox)
        pygame.draw.rect(gameDisplay,config.gray,itemDescBox)

        config.SPOOKY_INVENTORY_FONT.set_underline(True)
        drawText(gameDisplay, self.item_name, config.black, itemNameBox, config.SPOOKY_INVENTORY_FONT)
        config.SPOOKY_INVENTORY_FONT.set_underline(False)
        drawText(gameDisplay, self.item_desc, config.red, itemDescBox, config.SPOOKY_INVENTORY_FONT)

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

def displayInfo(itemName, itemDesc, mousePosition, inventory):
    while True:
        gameDisplay.fill(config.white)
        inventory.createInventory()

        descBox = infoBox(mousePosition, itemDesc, itemName)
        descBox.createInfo()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                return

#Takes in an item type, mouse position, and inventory 
def itemOptions(itemName, itemDesc, itemType, inventory):
    pos = pygame.mouse.get_pos()
    
    #Render the item menu til an option is selected, or if left clicked somewhere outside, close
    while True:
        gameDisplay.fill(config.white)
        inventory.createInventory()

        menu = itemOptionMenu(pos, itemType)
        menu.populateOptionsArray()
        menu.createOptions()

        optionsRectList = menu.optionsRects
        optionTextList = menu.optionsTextArray

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if menu.borderRect.collidepoint(pygame.mouse.get_pos()):
                    for i in range( len(optionsRectList) ):

                    #If an option is being selected, return the option selected
                    #When integrating this w/ rest of UI, EX. equipment add into here too!

                        if (optionsRectList[i].collidepoint(pygame.mouse.get_pos())):
                            #Implemented Discards
                            if (optionTextList[i] == "Discard One"):
                                return "Discard One"
                            elif (optionTextList[i] == "Discard All"):
                                return "Discard All"
                            elif (optionTextList[i] == "Info"):
                                displayInfo(itemName, itemDesc, pos, inventory)
                                return "Info"
                            
                            #WIP effects to be implemented
                            elif (optionTextList[i] == "Equip"):
                                return "Equip"
                            elif (optionTextList[i] == "Use"):
                                return "Use"
                #They clicked outside the menu, should still close it
                else: 
                    return "No Selection"
