import pygame
from config import *
from player import Player
import math
from map import world_map
from render import ray_casting
import davis

class GameMain: 

    def __init__(self, sc):
        clock = pygame.time.Clock()
        player = Player()


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            player.movement()
            sc.fill(black)

            pygame.draw.rect(sc, blue, (0, 0, display_width, display_height/2))
            pygame.draw.rect(sc, dark_gray, (0, display_height/2, display_width, display_height/2))

            ray_casting(sc, player.pos, player.angle)

           # pygame.draw.circle(sc, green, (int(player.x), int(player.y)), 12)
          #  pygame.draw.line(sc, green, player.pos, (player.x + display_width * math.cos(player.angle),
                                                      #player.y + display_width * math. sin(player.angle)), 2)
            # for x,y in world_map:
            #pygame.draw.rect(sc, dark_gray, (player.x, player.y, TILE, TILE), 2)
            TextSurf, TextRect = davis.render_text("W A S D to move, Arrow Keys to turn", SPOOKY_SMALL_FONT, red)
            TextRect.center = ((round(display_width/2)),(round(display_height-100)))
            sc.blit(TextSurf, TextRect)
            pygame.display.flip()
            clock.tick(FPS)
            print(clock.get_fps())