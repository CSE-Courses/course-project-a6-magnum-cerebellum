import pygame

pygame.init()


black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gray = (180,180,180)

SPOOKY_BIG_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 120)
SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 60)
SPOOKY_INVENTORY_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 30)
SPOOKY_ITEM_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 20)

RPG_ITEM_TYPE_FONT = pygame.font.Font("assets/fonts/RPGSYSTEM.ttf", 30)
display_width = 1024
display_height = 768