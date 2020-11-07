import pygame
from config import *
from render import ray_casting
from map import mini_map
import activities
import config

class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'1': pygame.image.load("assets/textures/wall1.png").convert(),
                         '2': pygame.image.load("assets/textures/wall2.png").convert(),
                         'S': pygame.image.load("assets/textures/sky.png").convert()
                         }
    
    def background(self, angle):
        sky_offset = -5 * math.degrees(angle) % render_display_width
        self.sc.blit(self.textures['S'], (sky_offset, 0))
        self.sc.blit(self.textures['S'], (sky_offset - render_display_width, 0))
        self.sc.blit(self.textures['S'], (sky_offset + render_display_width, 0))
        pygame.draw.rect(self.sc, dark_gray, (0, render_display_height//2, render_display_width, render_display_height//2))

    def world(self, world_objects):
        for obj in sorted(world_objects, key=lambda n: n[0], reverse=True):
            if obj[0]:
                _, object, object_pos = obj
                self.sc.blit(object, object_pos)

    def mini_map(self, player):
        self.sc_map.fill(black)


        map_x, map_y = player.x // MAP_SCALE, player.y // MAP_SCALE

        pygame.draw.line(self.sc_map, yellow, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                                 map_y + 12 * math.sin(player.angle)), 2)
        pygame.draw.circle(self.sc_map, red, (int(map_x), int(map_y)), 5)
        for x, y in mini_map:

            pygame.draw.rect(self.sc_map, dark_gray, (x, y, MAP_TILE, MAP_TILE))
        self.sc.blit(self.sc_map, MAP_POS)

    def activities_panel(self,second_screen):

        activities.setup(second_screen)#player_pos)

