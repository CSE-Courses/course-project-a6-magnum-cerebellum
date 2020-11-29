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
import encounter
from items import Item
from button import Button
import enemies
from battle import Battle


def GameMain(sc, playername):
    #If the player is in battle, it will bring up battle UI instead of Inventory
    #global in_battle
    playerInBattle = True
    playerIsBattling = False
    show = True
    #If the player clicks their inventory while in battle this should be True
    battleInvClicked = False

    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface(MINIMAP_RES)

    clock = pygame.time.Clock()
    sprites = Sprites()

    #Initialize Player, Inventory, Equipment, Battle UI
    player = Player(playername)
    enemy =  None
    inventory = invClassHelpers.Inventory(player.startingItems)
    equipment = equipClassHelpers.Equipment()
    battleUI = battle_UIClassHelpers.BattleUI(player,inventory)
    heldItem = None
    config.text1.append(player.pos)
    drawing = Drawing(sc, sc_map, None)
    second_screen = pygame.Surface((400, 300))
    second_screen.fill(black)
    healthBar = health.Bar(config.white, config.CHAR_DETAIL_FONT_LARGE, (1285, 500), sc)
    enemy_healthBar = health.Bar(config.white, config.CHAR_DETAIL_FONT_LARGE, (100, 650), sc, False)
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
        enemyBlit = drawing.enemyEncounter(sc, enemy)
        healthBar.updateBar()
        equipment.createEquip()
        activities.iterate_over_input(second_screen, 20)

        if playerIsBattling:
            attackButton = drawing.attackButton(sc)
            defendButton = drawing.defendButton(sc)
            if show:
                enemy_healthBar.show_bar()
                show = False
            if enemy != None:
                enemy_healthBar.set_health(enemy.hp)
            else:
                enemy_healthBar.set_health(100)
            enemy_healthBar.updateBar()
            

        if (playerInBattle == False or battleInvClicked):
            inventory.createInventory()
            if (battleInvClicked):
                Button.check_Hover(inventory.back, sc)
            drawing.blitHeldItem(heldItem, mouseX, mouseY)
            drawing.blitMenuInfoBoxes(inventory, equipment)

        if encounter.in_battle:
            encounter.enemy_trigger(sc)


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

                #click battle button to begin. Clicking button during or after a battle will start a new battle with a random enemy 
                elif enemyBlit.collidepoint(pygame.mouse.get_pos()):
                    print("battle beginning...") 
                    enemy = enemies.random_enemy()
                    playerIsBattling = True
                    battle_object = Battle(player, enemy)
                    enemy_healthBar.show_bar()
                    break
                
                # battle enemy with attacks (decrease enemy hp or defend (increase player hp))
                elif playerIsBattling:  
                    enemy_healthBar.clearBar()
                    if attackButton.collidepoint(pygame.mouse.get_pos()):
                        attack_value = player.attack
                        battle_object.attack_ememy_with_damage(attack_value)
                        enemy_healthBar.set_health(enemy.hp)
                        print("attack with " + str(attack_value))
                        if not battle_object.isActive:
                            print("battle over, enemy defeated")
                            playerIsBattling = False
                            show =  True
                            break
                        else:
                            action = enemy.random_attack()
                            damage = action.damage   
                            battle_object.attack_player_with_damage(damage) 
                            print("enemy attack with damage " + str(damage)) 
                            if not battle_object.isActive:
                                print("battle over, player defeated")
                                playerIsBattling = False
                                show =  True
                                healthBar.set_health(player.hp)
                                break
                        healthBar.set_health(player.hp)
                    
                    elif defendButton.collidepoint(pygame.mouse.get_pos()): 
                        defend_value = player.defense
                        battle_object.defend_with_damage(defend_value)
                        print("defend with " + str(defend_value))
                        healthBar.set_health(player.hp)
                    
                    
                     
                    
       
        pygame.display.flip()
        clock.tick(60)