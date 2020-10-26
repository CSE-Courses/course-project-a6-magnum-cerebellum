#Import random number picker for prototype inventory, remove later
import random
####
import pygame
import config
import random
from button import Button
from items import Item
import invClassHelpers
import time

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

def inventoryMain():
    # Creates inventory
    inventory = invClassHelpers.Inventory()

    # The item the cursor is holding
    heldItem = None

    while True:
        # Re-fills display everytime
        gameDisplay.fill(config.white)

        # Draw the inventory
        inventory.createInventory()


        # Get the position of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # If an item is selected, hold it
        if heldItem:
            gameDisplay.blit(heldItem[0].resize(30), (mouseX, mouseY))
            obj = config.SPOOKY_INVENTORY_FONT.render(str(heldItem[1]), True, (0, 0, 0))
            gameDisplay.blit(obj, (mouseX + 15, mouseY + 15))

        if inventory.itemMenuClicked:
            invClassHelpers.blitItemMenu(inventory)

        elif inventory.infoBoxClicked:
            invClassHelpers.blitInfoBox(inventory)

        #So everytime mouse moves this is called
        for event in pygame.event.get():
            mouse = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            # Get the player's mouse position
            pos = inventory.boxPos()

            # If it's a LEFT-CLICK
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                #If the an item was already right-clicked on, detect if player clicks on an option or outside the option list. Close the menu either way.
                if inventory.itemMenuClicked and inventory.itemMenu.borderRect.collidepoint(mouse):
                    menu = inventory.itemMenu
                    for i in range(len(menu.optionsRects)):
                    #If an option is being selected, do the effect then break out
                    #When integrating this w/ rest of UI, EX. equipment add into here too!
                    #When fully integrating into the actual main screen, do effect

                        if (menu.optionsRects[i].collidepoint(mouse)):
                            #Implemented Discards
                            if ("Discard" in menu.optionsTextArray[i]):
                                inventory.discardFromInventory(inventory.currentItem, inventory.itemBox, menu.optionsTextArray[i])
                                break
                            elif (menu.optionsTextArray[i] == "Info"):
                                inventory.infoBoxClicked = True
                                break                         
                            
                            #WIP effects to be implemented/integrated with other parts of the game

                            #elif (menu.optionsTextArray[i] == "Equip"):
                            #    break
                            #elif (menu.optionsTextArray[i] == "Use"):
                            #    break
                    inventory.itemMenuClicked = False

                #This means they clicked elsewhere, should still close the item options menu
                elif inventory.itemMenuClicked or inventory.infoBoxClicked :
                    inventory.itemMenuClicked = False
                    inventory.infoBoxClicked = False

                # Only if mouse position is within the inventory, do stuff with Item
                elif inventory.borderRect.collidepoint(pygame.mouse.get_pos()):

                    # If item being held use addToInventory
                    if heldItem:
                        heldItem = inventory.addToInventory(heldItem, pos)

                    # Grabs item from the box as heldItem, then sets box to nothing
                    elif inventory.items[pos[0]][pos[1]]:
                        # Array of Two
                        heldItem = inventory.items[pos[0]][pos[1]]
                        inventory.items[pos[0]][pos[1]] = None

            ### If it's a right-click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                # If it's a right-click on a box, intitialize things for Item Menu inside Inventory Class
                if inventory.borderRect.collidepoint(mouse) and inventory.items[pos[0]][pos[1]]:
                    inventory.createItemMenu(pos, inventory.items[pos[0]][pos[1]], mouse)
                    
                # TEMP: If it's a right click just grab a computer
                # Remove later when putting everything together
                elif heldItem == None:
                    randomItemPicker = [Item("Computer"), Item("Red Bull"), Item("Book")]
                    heldItem = [randomItemPicker[random.randint(0, 2)], 1]
        
        # Update display
        pygame.display.update()

# Uncomment these if you want to directly launch from inventory.py for faster debugging/testing
inventoryMain()
quit()
