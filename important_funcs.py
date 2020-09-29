import math
import pygame
import config
import music


gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))



class funcs:
    def roundup(x):
        return int(math.ceil(x / 10.0)) * 10

    def reRenderVol(volDisplay, vol, text):
        volDisplay.text = text
        volDisplay.buttonText()
        gameDisplay.fill(config.black)
        volDisplay.createButton(gameDisplay)
        vol.createButton(gameDisplay)

    def render_text(text, font, color):
        textSurface = font.render(text, True, color)
        return textSurface, textSurface.get_rect()

