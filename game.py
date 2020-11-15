import pygame
import invClassHelpers
import equipClassHelpers
import battle_UIClassHelpers
from config import *
import config
from player import Player
from sprites import *
from render import ray_casting
from drawing import Drawing
import health
import activities
from items import Item
from button import Button

def GameMain(sc, playername):
    #If the player is in battle, it will bring up battle UI instead of Inventory
    playerInBattle = True
    #playerInBattle = False
    
    #If the player clicks their inventory while in battle this should be True
    battleInvClicked = False

    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface(MINIMAP_RES)

    clock = pygame.time.Clock()
    sprites = Sprites()

    player = Player(playername)
    inventory = invClassHelpers.Inventory()
    equipment = equipClassHelpers.Equipment()
    battleUI = battle_UIClassHelpers.BattleUI(player,inventory)

    drawing = Drawing(sc, sc_map, None)
    heldItem = None

    config.text1.append(player.pos)
    second_screen = pygame.Surface((400, 300))

    second_screen.fill(black)
    drawing.activities_panel(second_screen)
    healthBar = health.Bar(config.white, config.CHAR_DETAIL_FONT_LARGE, (1285, 500), sc)
    
    while True:
        mouseX, mouseY = pygame.mouse.get_pos()

        sc.fill(black)
        player.movement()
        walls = ray_casting(player, drawing.textures)
        drawing.background(player.angle)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])

        sc.blit(second_screen, (0, config.scroll_y))
        activities.iterate_over_input(second_screen, 20)
        drawing.ui_elements(player,sc)
        healthBar.updateBar()
        equipment.createEquip()
        drawing.mini_map(player)

        if (playerInBattle == False or battleInvClicked):
            inventory.createInventory()
            if (battleInvClicked):
                Button.check_Hover(inventory.back, sc)
            drawing.blitHeldItem(heldItem, mouseX, mouseY)
            drawing.blitMenuInfoBoxes(inventory, equipment)

        else: #The player is in battle
            battleUI.createBattleUI()

            #the hover check is what's blitting the actions to the screen each time also
            #battleUI.actions[0] to [3] is the player's moves. [4] is "Open Inventory"
            for button in battleUI.actions:
                Button.check_Hover(button, sc)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN and (playerInBattle == False or battleInvClicked):
                #If they clicked "Back" in the Inventory
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and inventory.back.rect.collidepoint(pygame.mouse.get_pos()):
                    battleInvClicked = False
                    break

                heldItem, healthBar = drawing.inventoryEquipmentUI(inventory, equipment, sc, event.type, event.button, mouseX, mouseY, heldItem, healthBar)
                drawing.blitMenuInfoBoxes(inventory, equipment)
                if event.button == 4:
                    config.scroll_y = min(config.scroll_y + 20, 0)
                    print('up')
                if event.button == 5:
                    config.scroll_y = max(config.scroll_y - 20, -300)
                    print('down')
                    print(config.scroll_y)

            #If they left-click
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                #If they clicked "Open Inventory" in the Battle UI
                if battleUI.actions[4].rect.collidepoint(pygame.mouse.get_pos()):
                    battleInvClicked = True           

        pygame.display.flip()
        clock.tick(30)