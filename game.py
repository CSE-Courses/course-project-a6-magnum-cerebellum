import pygame
from config import *
from player import Player
import math
from map import world_map
from render import ray_casting
from drawing import Drawing


def GameMain(sc): 
    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface((display_width // MAP_SCALE, display_height // MAP_SCALE))
    clock = pygame.time.Clock()
    player = Player()
    drawing = Drawing(sc, sc_map)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
        player.movement()
        sc.fill(black)

        drawing.background()
        drawing.world(player.pos, player.angle)
        drawing.mini_map(player)

        pygame.display.flip()
        clock.tick()