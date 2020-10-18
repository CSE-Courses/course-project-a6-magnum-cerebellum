import pygame
from button import Button
import config
from daviscopy import gameDisplay



buttons = [Button("Sword", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/2)), gameDisplay),
    Button("Dagger", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.5)), gameDisplay),
    Button("Knife", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.20)), gameDisplay),
    Button("Axe", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width/2),(config.display_height/1.1)), gameDisplay)]

gameDisplay.fill(config.black)