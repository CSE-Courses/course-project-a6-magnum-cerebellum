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
    
    #If the player clicks their inventory while in battle this should be True
    battleInvClicked = False

    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface(MINIMAP_RES)

    clock = pygame.time.Clock()
    sprites = Sprites()

    #Initialize Player, Inventory, Equipment, Battle UI
    player = Player(playername)
    inventory = invClassHelpers.Inventory(player.startingItems)
    equipment = equipClassHelpers.Equipment()
    battleUI = battle_UIClassHelpers.BattleUI(player,inventory)
    heldItem = None
    config.text1.append(player.pos)
    drawing = Drawing(sc, sc_map, None)
    second_screen = pygame.Surface((400, 300))
    second_screen.fill(black)
    healthBar = health.Bar(config.white, config.CHAR_DETAIL_FONT_LARGE, (1285, 500), sc)
    
    while True:
        mouseX, mouseY = pygame.mouse.get_pos()

        sc.fill(black)
        player.movement()
        walls = ray_casting(player, drawing.textures)
        drawing.background(player.angle)
        drawing.world(walls + [obj.object_locate(player, healthBar) for obj in sprites.list_of_objects])
        sc.blit(second_screen, (0, 0))
        # second_screen.blit(second_screen, (0, config.scroll_y))
        drawing.mini_map(player)
        drawing.ui_elements(player,sc)
        drawing.activities_panel(second_screen)
        healthBar.updateBar()
        equipment.createEquip()
        activities.iterate_over_input(second_screen, 20)


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

                heldItem, healthBar, player = drawing.inventoryEquipmentUI(inventory, equipment, sc, event.type, event.button, mouseX, mouseY, heldItem, healthBar, player)
                drawing.blitMenuInfoBoxes(inventory, equipment)
                
                #print("Player Attack : " + str(player.attack))
                #print("Player Defense : " + str(player.defense))
                
                # if event.key == pygame.K_p:
                #     global paused
                #     paused = True
                #     pause()
                # if event.key == pygame.K_s:
                #     save(player)
                #     messages_to_add(0,0, None, None, None, None)
                # if event.key == pygame.K_l:
                #     load()
                #     player.pos = loaddata['pos']
                #     player.health = loaddata['health']
                #     player.actions = loaddata['actions']
                #     player.items = loaddata['items']
                #     player.hp = loaddata['hp']
                
                if event.button == 4:
                    config.scroll_y = min(config.scroll_y + 20, 0) #what happens when you scroll is that the activities panel goes
                                                                   #black and then the text are repeated
                                                                   #so you should use the second_screen recursively
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
        clock.tick(60)