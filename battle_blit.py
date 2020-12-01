from player import Player
from enemies import Enemy
from items import Item
import time
import random
from health import Bar
import pygame
import config
from battle import Battle
from button import Button
from tiffsInventory import inventoryMain
import tiffInvHelpers


clock = pygame.time.Clock()

def battleMain(player : Player, enemy : Enemy, prevDisplay):
    backgroundColor = config.green
    message1 = config.SPOOKY_BIG_FONT.render("", False, backgroundColor)
    message2 = config.SPOOKY_BIG_FONT.render("", False, backgroundColor)
    display = pygame.display.set_mode((config.display_width, config.display_height))
    display.fill(backgroundColor)

    inventory = tiffInvHelpers.Inventory(display, player, (config.display_width/2, config.display_height/(4/3)) , 40)
    heldItem = None

    battle = Battle(player, enemy)
    players_turn = True
    healthBar_player = Bar(config.black, config.SPOOKY_SMALLER_FONT, (config.display_width/4, config.display_height/12), display)
    healthBar_enemy = Bar(config.black, config.SPOOKY_SMALLER_FONT, (config.display_width/(4/3), config.display_height/12), display)
    while battle.isActive:
        display.fill(config.green)

        x = config.display_width/4
        y = config.display_height/12
        surf = pygame.Surface((100,100))
        display.blit(surf, (x,y))
   
        font = config.SPOOKY_SMALL_FONT
        player_ = font.render("Player", False, config.red)
        enemy_ = font.render("Enemy", False, config.red)
        display.blit(player_, (config.display_width/4, 0))
        display.blit(enemy_, (config.display_width/(4/3), 0))
        
        healthBar_player.set_health(player.hp)
        healthBar_player.createBar()
        
        healthBar_enemy.set_health(enemy.hp)
        healthBar_enemy.createBar()
        
        text = config.SPOOKY_BIG_FONT.render("Choose next attack", False, config.black)
        display.blit(text, (config.display_width/6, config.display_height/2))
        display.blit(message1, (config.display_width/6, config.display_height/4))
        display.blit(message2, (config.display_width/6, config.display_height/3))
        for event in pygame.event.get():
            
            heldItem, item_selected = inventory_utilities(display, inventory, heldItem, event)

            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()

            elif players_turn:
                if (item_selected != None):
                    
                    print("enemy hp before", enemy.hp)
                    battle.attack_enemy(item_selected)
                    damage = item_selected.amount
                    print("player attack with damage", damage)
                    print("enemy hp after", enemy.hp)
                    healthBar_enemy.clearBar(backgroundColor)
                    message1 = config.SPOOKY_BIG_FONT.render(f'Player attacked with {damage} hp damage ', False, config.black)
                    players_turn = False
                
            if not players_turn:
                print("player hp before", player.hp)
                action = enemy.random_attack()
                damage = action.damage
                print("enemy attack with damage", damage)
                
                battle.attack_player(action)
                
                print("player hp after", player.hp)
                healthBar_player.clearBar(backgroundColor)
                message2 = config.SPOOKY_BIG_FONT.render(f'Enemy attacked with {damage} hp damage ', False, config.red)
                players_turn = True
               
               
            pygame.display.update()
            clock.tick(15)
    while True:
        display.fill(config.green)
        healthBar_player.clearBar(backgroundColor)
        healthBar_player.set_health(player.hp)
        healthBar_player.createBar()

        healthBar_enemy.clearBar(backgroundColor)
        healthBar_enemy.set_health(enemy.hp)
        healthBar_enemy.createBar()
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
        if player.hp <= 0:
            text = config.SPOOKY_BIG_FONT.render(f'Player has died', False, config.black)
        else:
           text = config.SPOOKY_BIG_FONT.render(f'Enemy has died', False, config.black) 
        player_ = font.render("Player", False, config.red)
        enemy_ = font.render("Enemy", False, config.red)
        display.blit(player_, (config.display_width/4, 0))
        display.blit(enemy_, (config.display_width/(4/3), 0))
        display.blit(text, (config.display_width/6, config.display_height/2))
        display.blit(message1, (config.display_width/6, config.display_height/4))
        display.blit(message2, (config.display_width/6, config.display_height/3))
        pygame.display.update()
        clock.tick(15)
                
    
    return 

def inventory_utilities(gameDisplay, inventory, heldItem, event):
    inventory.createInventory(gameDisplay)
    item_selected = None
    mouseX, mouseY = pygame.mouse.get_pos()
    mouse = pygame.mouse.get_pos()
    info_box = False
    if heldItem:
        gameDisplay.blit(heldItem[0].resize(30), (mouseX, mouseY))

        if (heldItem[0].item_type != "Equip"):
            obj = config.SPOOKY_INVENTORY_FONT.render(str(heldItem[1]), True, config.white)
            outline = config.SPOOKY_INVENTORY_OUTLINE.render(str(heldItem[1]), True, config.black)
            gameDisplay.blit(outline, (mouseX + 20, mouseY + 20))
            gameDisplay.blit(obj, (mouseX + 20, mouseY + 20))
                
    if inventory.itemMenuClicked:
        tiffInvHelpers.blitItemMenu(inventory, gameDisplay)

    elif inventory.infoBoxClicked:
        tiffInvHelpers.blitInfoBox(inventory, gameDisplay)
        info_box = True

    pos = inventory.boxPos()
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

        #If the an item was already right-clicked on, detect if player clicks on an option or outside the option list. Close the menu either way.
        if inventory.itemMenuClicked and inventory.itemMenu.borderRect.collidepoint(mouse):
            menu = inventory.itemMenu
            for i in range(len(menu.optionsRects)):
                if (menu.optionsRects[i].collidepoint(mouse)):
                    if ("Discard" in menu.optionsTextArray[i]):
                        inventory.discardFromInventory(inventory.itemBox, menu.optionsTextArray[i])
                        break
                    elif (menu.optionsTextArray[i] == "Info"):
                        inventory.infoBoxClicked = True
                        break
                    elif (menu.optionsTextArray[i] == "Use") :

                        return heldItem, Item("Computer")
                
            inventory.itemMenuClicked = False


        #This means they clicked elsewhere, should still close the item options menu
        elif (inventory.itemMenuClicked or inventory.infoBoxClicked ) :
            inventory.itemMenuClicked = inventory.infoBoxClicked = False
        
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
        inventory.itemMenuClicked = False
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
        # If it's a right-click on a box, intitialize things for Item Menu inside Inventory Class
        if inventory.borderRect.collidepoint(mouse) and inventory.items[pos[0]][pos[1]]:
            inventory.createItemMenu(pos, inventory.items[pos[0]][pos[1]], mouse)

        elif info_box:
            pass
        elif heldItem == None:
            randomItemPicker = [Item("Computer"), Item("Book"),Item("Red Bull")]
            heldItem = [randomItemPicker[random.randint(2, 2)], 1]
    return heldItem, item_selected