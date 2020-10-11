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
        self.borderRect = pygame.Rect(self.menuX, self.menuY, (self.box_size + self.border) + 55, (self.box_size + self.border) * self.numberOfBoxes + self.border)

        pygame.draw.rect(gameDisplay,config.black,self.borderRect)

        #draw the inside 
        for col in range(1):

            for row in range (self.numberOfBoxes):
                boxRect = pygame.Rect(  (self.menuX + self.border)
                    , self.menuY + (self.box_size + self.border) * row + self.border
                    , self.box_size + 50
                    , self.box_size  )
                pygame.draw.rect(gameDisplay,config.gray,boxRect)

                text = config.SPOOKY_INVENTORY_FONT.render(self.optionsTextArray[row], True, config.red)
                text_rect = text.get_rect(center=boxRect.center)
                self.optionsRects.append(text_rect)

                gameDisplay.blit(text, text_rect)

    def populateOptionsArray(self):
        self.optionsTextArray = ["Info"]
        self.numberOfBoxes = 3
        if (self.itemType == "Equip"):
            self.optionsTextArray.extend( ["Equip", "Discard"] )
        elif (self.itemType == "Consumable"):
            self.optionsTextArray.extend( ["Use", "Discard"] )

#Takes in an item type, mouse position, and inventory 
def itemOptions(itemType, mousePosition, inventory, itemPosition):
    pos = pygame.mouse.get_pos()
    notSelected = True
    
    #Render the item menu til an option is selected, or if left clicked somewhere outside, close
    while notSelected:
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
                    #If an option is being selected
                        if (optionsRectList[i].collidepoint(pygame.mouse.get_pos())):
                            if (optionTextList[i] == "Discard"):
                                return "Discard"
                else: 
                    return
