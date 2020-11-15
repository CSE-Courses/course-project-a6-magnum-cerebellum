import pygame
import math

pygame.init()


paused = False

SPOOKY_BIG_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 120)
SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 60)
SPOOKY_SMALLER_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 25)
SPOOKY_INVENTORY_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 30)
SPOOKY_INVENTORY_OUTLINE = pygame.font.Font("assets/fonts/CHILLER.ttf", 35)
SPOOKY_INFO_OUTLINE = pygame.font.Font("assets/fonts/CHILLER.ttf", 32)
SPOOKY_ITEM_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 20)
RPG_ITEM_TYPE_FONT = pygame.font.Font("assets/fonts/RPGSYSTEM.ttf", 30)
RPG_ACTION_FONT = pygame.font.Font("assets/fonts/RPGSYSTEM.ttf", 25)

CHAR_DETAIL_FONT_LARGE = pygame.font.Font("assets/fonts/RPGSYSTEM.ttf", 30)
CHAR_DETAIL_FONT_SMALL = pygame.font.Font("assets/fonts/RPGSYSTEM.ttf", 20)
display_width = 1600
display_height = 800  #from 1200
render_display_width = 1200
render_display_height = 800
FPS = 60
TILE = 100
FPS_POS = (render_display_width - 65, 5)


# player settings
player_pos = ((render_display_width//2)//4, (render_display_height//2)-50)
player_angle = 0
player_speed = 2

# mini-map settings
MINIMAP_SCALE = 3
MINIMAP_RES = (render_display_width// MINIMAP_SCALE, render_display_height // MINIMAP_SCALE)
MAP_SCALE = 2 * MINIMAP_SCALE
MAP_TILE = TILE // MAP_SCALE
MAP_POS = (display_width-400, (display_height // MINIMAP_SCALE)-270)

# ray casting settings
FOV = math.pi / 3 
HALF_FOV = FOV / 2
NUM_RAYS = 300
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = (render_display_width // NUM_RAYS)

# texture settings
TEXTURE_WIDTH = 100
TEXTURE_HEIGHT = 100
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# sprite settings
DOUBLE_PI = math.pi * 2
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
gray = (180,180,180)
green = (0, 220, 0)
blue = (0, 0, 255)
dark_gray = (40, 40, 40)
purple = (120, 0, 120)
yellow = (220, 220, 0)
cyan = (0, 186, 255)

#for activities
text1 = []
scroll_y = 0
y_val = 20
counter = 1
storage = []
