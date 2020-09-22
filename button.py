import pygame

class Button:

    def __init__(self, text, color, font, pos, gameDisplay):
        self.text = text
        self.color = color
        self.font = font
        self.pos = pos

        self.set_rect()
        self.createButton(gameDisplay)

    def buttonText(self):
        self.rend = self.font.render(self.text, True, self.color)
 
    def set_rect(self):
        self.buttonText()
        self.rect = self.rend.get_rect()
        self.rect.center = self.pos

    def createButton(self, gameDisplay):
        self.buttonText()
        gameDisplay.blit(self.rend, self.rect)
    
    def check_Hover(self, gameDisplay):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.color = (255,0,0) # Red
        else:
            self.color = (255,255,255) # White
        self.createButton(gameDisplay)