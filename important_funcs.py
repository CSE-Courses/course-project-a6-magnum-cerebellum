import math
import pygame
import config

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

class funcs:
    def roundup(x):
        return int(math.ceil(x / 10.0)) * 10