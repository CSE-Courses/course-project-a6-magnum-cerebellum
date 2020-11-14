import pygame
import invClassHelpers
import equipClassHelpers
from config import *
import config
from player import Player
from sprites import *
from render import ray_casting
from drawing import Drawing

import activities
from items import Item

def GameMain(sc, playername):

    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface(MINIMAP_RES)

    clock = pygame.time.Clock()
    sprites = Sprites()

    player = Player(playername)
    inventory = invClassHelpers.Inventory()
    equipment = equipClassHelpers.Equipment()

    drawing = Drawing(sc, sc_map, None)
    heldItem = None

    config.text1.append(player.pos)
    second_screen = pygame.Surface((400, 300))

    second_screen.fill(black)
    drawing.activities_panel(second_screen)

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
        inventory.createInventory()
        equipment.createEquip()
        drawing.mini_map(player)
        drawing.blitHeldItem(heldItem, mouseX, mouseY)
        drawing.blitMenuInfoBoxes(inventory, equipment)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                heldItem = drawing.inventoryEquipmentUI(inventory, equipment, sc, event.type, event.button, mouseX, mouseY, heldItem)
                drawing.blitMenuInfoBoxes(inventory, equipment)
                if event.key == pygame.K_p:
                    global paused
                    paused = True
                    pause()
                if event.key == pygame.K_s:
                    save(player)
                    messages_to_add(0,0, None, None, None, None)
                if event.key == pygame.K_l:
                    load()
                    player.pos = loaddata['pos']
                    player.health = loaddata['health']
                    player.actions = loaddata['actions']
                    player.items = loaddata['items']
                    player.hp = loaddata['hp']
                if event.button == 4:
                    config.scroll_y = min(config.scroll_y + 20, 0)
                    print('up')
                if event.button == 5:
                    config.scroll_y = max(config.scroll_y - 20, -300)
                    print('down')
                    print(config.scroll_y)

        pygame.display.flip()
        clock.tick(30)