#Import random number picker for prototype inventory, remove later
import random
####
import pygame
import config
import random
from button import Button
from items import Item
import invClassHelpers
import equipClassHelpers
import time
from health import Bar
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

def inventoryMain():
    # Creates inventory
    gameDisplay.fill(config.white)

    inventory = invClassHelpers.Inventory()
    equipment = equipClassHelpers.Equipment()
    # The item the cursor is holding
    heldItem = None
    healthBar = Bar(config.black, config.SPOOKY_SMALLER_FONT, (830, 150), gameDisplay)
    healthBar.createBar()

    while True:
        # Get the position of the mouse
        mouseX, mouseY = pygame.mouse.get_pos()

        # So everytime mouse moves this is called
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()

            # Re-fills display everytime
            gameDisplay.fill(config.white)
            healthBar.updateBar()
            # Draw the inventory and Equipment GUI
            inventory.createInventory()
            equipment.createEquip()

            #Get Current Position of the Mouse
            mouse = pygame.mouse.get_pos()

            # If an item is selected, hold it
            if heldItem:
                gameDisplay.blit(heldItem[0].resize(30), (mouseX, mouseY))

                if (heldItem[0].item_type != "Equip"):
                    obj = config.SPOOKY_INVENTORY_FONT.render(str(heldItem[1]), True, config.white)
                    outline = config.SPOOKY_INVENTORY_OUTLINE.render(str(heldItem[1]), True, config.black)
                    gameDisplay.blit(outline, (mouseX + 20, mouseY + 20))
                    gameDisplay.blit(obj, (mouseX + 20, mouseY + 20))

            if inventory.itemMenuClicked:
                invClassHelpers.blitItemMenu(inventory)

            elif inventory.infoBoxClicked:
                invClassHelpers.blitInfoBox(inventory)

            elif equipment.infoBoxClicked:
                equipClassHelpers.blitEquipInfoBox(equipment)

            elif equipment.itemMenuClicked:
                equipClassHelpers.blitEquipItemMenu(equipment)

            # Get the player's mouse position
            pos = inventory.boxPos()
            equipPos = equipment.boxPos()
            #print(equipPos)
            # If it's a LEFT-CLICK
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                #If the an item was already right-clicked on, detect if player clicks on an option or outside the option list. Close the menu either way.
                if inventory.itemMenuClicked and inventory.itemMenu.borderRect.collidepoint(mouse):
                    menu = inventory.itemMenu
                    for i in range(len(menu.optionsRects)):
                    #If an option is being selected, do the effect then break out
                    #When integrating this w/ rest of UI, EX. equipment add into here too!
                    #When fully integrating into the actual main screen, do effect

                        if (menu.optionsRects[alli].collidepoint(mouse)):
                            #Implemented Discards
                            if ("Discard" in menu.optionsTextArray[i]):
                                inventory.discardFromInventory(inventory.itemBox, menu.optionsTextArray[i])
                                break
                            elif (menu.optionsTextArray[i] == "Info"):
                                inventory.infoBoxClicked = True
                                break

                            #WIP effects to be implemented/integrated with other parts of the game

                            elif (menu.optionsTextArray[i] == "Equip"):
                                swappedItem = equipment.equipItem(inventory.currentItem)

                                if (swappedItem == None):
                                    inventory.discardFromInventory(inventory.itemBox, "Discard One")
                                elif (swappedItem[0].item_name != inventory.currentItem[0].item_name):

                                    inventory.discardFromInventory(inventory.itemBox, "Discard One")
                                    inventory.addToInventory(swappedItem, inventory.itemBox)
                                break
                            elif (menu.optionsTextArray[i] == "Use"):
                                healthBar.addHealth(inventory.currentItem[0].damage)
                                #healthBar.subtractHealth(inventory.currentItem[0].damage)
                                #healthBar.subtractMana(inventory.currentItem[0].damage)

                                inventory.discardFromInventory(inventory.itemBox, "Discard One")
                                break
                    inventory.itemMenuClicked = False

                elif equipment.itemMenuClicked and equipment.itemMenu.borderRect.collidepoint(mouse):
                    menu = equipment.itemMenu
                    for i in range(len(menu.optionsRects)):
                        if (menu.optionsRects[i].collidepoint(mouse)):
                            if (menu.optionsTextArray[i] == "Info"):
                                equipment.infoBoxClicked = True
                                break
                            elif (menu.optionsTextArray[i] == "Unequip"):
                                equipment.unequipItem(equipment, inventory)
                                break
                    equipment.itemMenuClicked = False

                #This means they clicked elsewhere, should still close the item options menu
                elif (inventory.itemMenuClicked or inventory.infoBoxClicked or equipment.itemMenuClicked or equipment.infoBoxClicked) :
                    inventory.itemMenuClicked = inventory.infoBoxClicked = equipment.itemMenuClicked = equipment.infoBoxClicked = False

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

                elif (equipment.borderRect.collidepoint(mouse)
                and equipPos != (2,0) and equipPos != (0,0) and equipment.equipment[equipPos]):
                    equipment.createEquipItemMenu(equipPos, mouse)

                # TEMP: If it's a right click just grab a computer
                # Remove later when putting everything together
                elif heldItem == None:
                    randomItemPicker = [Item("Computer"), Item("Book"),Item("Red Bull")]
                    heldItem = [randomItemPicker[random.randint(2, 2)], 1]

        # Update display
        pygame.display.update()

# Uncomment these if you want to directly launch from inventory.py for faster debugging/testing

# inventoryMain()
# quit()

