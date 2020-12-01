import pygame
import random
from config import *
from render import ray_casting
from map import mini_map

import activities
import config
import health

from character_UI import char_ui
from invClassHelpers import *
from equipClassHelpers import  *
from items import Item
from enemies import Enemy

class Drawing:
    def __init__(self, sc, sc_map, heldItem):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'1': pygame.image.load("assets/textures/wall1.png").convert(),
                         '2': pygame.image.load("assets/textures/wall2.png").convert(),
                         'S': pygame.image.load("assets/textures/sky.png").convert()
                         }

    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % render_display_width
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - render_display_width, 0))
        self.sc.blit(self.textures['S'], (sky_offset + render_display_width, 0))
        pygame.draw.rect(self.sc, dark_gray, (0, render_display_height//2, render_display_width, render_display_height//2))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def mini_map(self, player):
        self.sc_map.fill(black)


        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.line(self.sc_map, yellow, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, red, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:

            pygame.draw.rect(self.sc_map, dark_gray, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)


    def activities_panel(self,second_screen):

        activities.setup(second_screen)#player_pos)
    
    def ui_elements(self, player, gameDisplay):
        char_ui(CHAR_DETAIL_FONT_LARGE, player_pos, player.character, player.character, gameDisplay)

    def blitHeldItem(self, heldItem, mouseX, mouseY):
        if heldItem:
                self.sc.blit(heldItem[0].resize(30), (mouseX, mouseY))
                if (heldItem[0].item_type != "Equip"):
                    obj = SPOOKY_INVENTORY_FONT.render(str(heldItem[1]), True, white)
                    outline = SPOOKY_INVENTORY_OUTLINE.render(str(heldItem[1]), True, black)
                    self.sc.blit(outline, (mouseX + 20, mouseY + 20))
                    self.sc.blit(obj, (mouseX + 20, mouseY + 20))

    def blitMenuInfoBoxes(self, inventory, equipment):

        if inventory.itemMenuClicked:
            blitItemMenu(inventory)

        if equipment.itemMenuClicked:
            blitEquipItemMenu(equipment)

        if inventory.infoBoxClicked:
            blitInfoBox(inventory)

        if equipment.infoBoxClicked:
            blitEquipInfoBox(equipment)

    #Big inventory chunk below
    def inventoryEquipmentUI(self, inventory, equipment, gameDisplay, eventType, eventButton, mouseX, mouseY, heldItem, healthBar, player):

        inventory.createInventory()
        equipment.createEquip()
        mouse = pygame.mouse.get_pos()
        
        self.blitHeldItem(heldItem, mouseX, mouseY)
        self.blitMenuInfoBoxes(inventory, equipment)

        # Get the player's mouse position
        pos = inventory.boxPos()
        equipPos = equipment.boxPos()
        # If it's a LEFT-CLICK
        if eventType == pygame.MOUSEBUTTONDOWN and eventButton == 1:

            #If the an item was already right-clicked on, detect if player clicks on an option or outside the option list. Close the menu either way.
            if inventory.itemMenuClicked and inventory.itemMenu.borderRect.collidepoint(mouse):
                menu = inventory.itemMenu
                for i in range(len(menu.optionsRects)):
                #If an option is being selected, do the effect then break out
                #When integrating this w/ rest of UI, EX. equipment add into here too!
                #When fully integrating into the actual main screen, do effect

                    if (menu.optionsRects[i].collidepoint(mouse)):
                        #DISCARD OPTION
                        if ("Discard" in menu.optionsTextArray[i]):
                            inventory.discardFromInventory(inventory.itemBox, menu.optionsTextArray[i])

                        #INFO OPTION
                        elif (menu.optionsTextArray[i] == "Info"):
                            inventory.infoBoxClicked = True                    

                        #EQUIP OPTION
                        elif (menu.optionsTextArray[i] == "Equip"):
                            swappedItem = equipment.equipItem(inventory.currentItem)
                            if (swappedItem == None):
                                inventory.discardFromInventory(inventory.itemBox, "Discard One")
                            elif (swappedItem[0].item_name != inventory.currentItem[0].item_name):
                                inventory.discardFromInventory(inventory.itemBox, "Discard One")
                                inventory.addToInventory(swappedItem, inventory.itemBox)
                                #Swapped with an Equip so need to decrement the old equip values
                                if (swappedItem[0].equip_type == "Weapon"):
                                    player.attack -= swappedItem[0].amount
                                else:
                                    player.defense -= swappedItem[0].amount
                                    
                            #Change player value
                            if (inventory.currentItem[0].equip_type == "Weapon"):
                                player.attack += inventory.currentItem[0].amount
                            else:
                                player.defense += inventory.currentItem[0].amount
                        
                        #USE OPTION
                        elif (menu.optionsTextArray[i] == "Use"):
                            if (inventory.currentItem[0].effect == "Health"):
                                healthBar.subtractHealth(inventory.currentItem[0].amount)
                            elif (inventory.currentItem[0].effect == "Mana"):
                                healthBar.addMana(inventory.currentItem[0].amount)
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
                            equip_type, value = equipment.unequipItem(equipment, inventory)
                            #Successful unequip
                            if (equip_type != None):
                                if(equip_type == "Weapon"):
                                    player.attack -= value
                                else : #Then it's armor
                                    player.defense -= value
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
        elif eventType == pygame.MOUSEBUTTONDOWN and eventButton == 3:
            
            #This means they clicked elsewhere, should still close the item options menu
            if (inventory.itemMenuClicked or inventory.infoBoxClicked or equipment.itemMenuClicked or equipment.infoBoxClicked) :
                inventory.itemMenuClicked = inventory.infoBoxClicked = equipment.itemMenuClicked = equipment.infoBoxClicked = False

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
                heldItem = [randomItemPicker[random.randint(0, 2)], 1]
        return heldItem, healthBar, player

    def enemyEncounter(self, display, enemy: Enemy):
        text = config.SPOOKY_ITEM_FONT.render("Battle Enemy", True, config.black, config.gray)
        rect = display.blit(text, (0, config.display_height/2))
        return rect
    def attackButton(self, display):
        text = config.SPOOKY_ITEM_FONT.render("Attack", True, config.black, config.gray)
        rect = display.blit(text, (0, config.display_height/2 + 50))
        return rect
    def defendButton(self, display):
        text = config.SPOOKY_ITEM_FONT.render("Defend", True, config.black, config.gray)
        rect = display.blit(text, (0, config.display_height/2 + 80))
        return rect

