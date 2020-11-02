import pygame
from config import *
import config
from player import Player
import math
from map import world_map
from render import ray_casting
from drawing import Drawing
import activities


def GameMain(sc):
    sc = pygame.display.set_mode((display_width, display_height))
    sc_map = pygame.Surface((display_width // MAP_SCALE, display_height // MAP_SCALE))
    clock = pygame.time.Clock()

    player = Player("char one")
    drawing = Drawing(sc, sc_map)

    config.text1.append(player.pos)
    second_screen = pygame.Surface((400, 300))

    second_screen.fill(black)
    drawing.activities_panel(second_screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    config.scroll_y = min(config.scroll_y + 20, 0)
                    print('up')
                if event.button == 5:
                    config.scroll_y = max(config.scroll_y - 20, -300)
                    print('down')
                    print(config.scroll_y)
        player.movement()
        sc.fill(black)
        drawing.background()
        drawing.world(player.pos, player.angle)
        drawing.mini_map(player)
        sc.blit(second_screen, (0, config.scroll_y))
        activities.iterate_over_input(second_screen, 20)

        pygame.display.flip()
        clock.tick(30)