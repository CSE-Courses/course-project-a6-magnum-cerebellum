import pygame
from config import *
from player import Player
from sprites import *
from render import ray_casting
from drawing import Drawing


def GameMain(sc): 
    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface(MINIMAP_RES)
    clock = pygame.time.Clock()
    sprites = Sprites()
    player = Player("char one")
    drawing = Drawing(sc, sc_map)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        sc.fill(black)
        drawing.background(player.angle)
        walls = ray_casting(player, drawing.textures)
        drawing.world(walls + [obj.object_locate(player) for obj in sprites.list_of_objects])
        drawing.mini_map(player)
        pygame.display.flip()
        clock.tick()