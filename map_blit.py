import pygame
import game
import config 

class Map():
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.surface = None
        self.rect = None

    def gen_text(self):
        self.surface = config.SPOOKY_SMALL_FONT.render(self.text, True, config.black)

    def blit(self, gameDisplay):
        self.gen_text()
        gameDisplay.blit(self.surface, self.pos)
        self.rect = self.surface.get_rect()
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        return self.rect

    def enter(self, gameDisplay):
        game.GameMain(gameDisplay)
    def check_hover(self):
        pass