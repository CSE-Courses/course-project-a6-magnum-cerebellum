import pygame
import invClassHelpers
import equipClassHelpers
from config import *
from player import Player
from sprites import *
from render import ray_casting
from drawing import Drawing
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

    while True:
        mouseX, mouseY = pygame.mouse.get_pos()

        sc.fill(black)
        player.movement()
        drawing.mini_map(player)
        walls = ray_casting(player, drawing.textures)
        drawing.background(player.angle)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        drawing.ui_elements(player,sc)
        inventory.createInventory()
        equipment.createEquip()
        
        drawing.blitHeldItem(heldItem, mouseX, mouseY)
        drawing.blitMenuInfoBoxes(inventory, equipment)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                heldItem = drawing.inventoryEquipmentUI(inventory, equipment, sc, event.type, event.button, mouseX, mouseY, heldItem)
                drawing.blitMenuInfoBoxes(inventory, equipment)


        pygame.display.flip()
        clock.tick()