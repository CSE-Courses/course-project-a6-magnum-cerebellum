import config
import pygame
from button import Button
import format_text
clock = pygame.time.Clock()


def transistion_character_selection_gameplay(gameDisplay, player):
    gameDisplay = pygame.display.set_mode((config.display_width, config.display_height),0, 32)
    gameDisplay.fill(config.black)
    sprite = player.character.sprite_size(300,300)
    gameDisplay.blit(sprite, (config.display_width/4, config.display_height/4))
    format_text.blit_text(gameDisplay, f'Welcome to Escape from Davis {player.character} \n Your journey will begin in the basement of Davis Hall, you must battle your way to the roof. \n You will start with {player.hp} health points, dont let it fall to 0! \n click "start game" to begin your escape!' ,(1000,1000), (config.display_width/2, config.display_height/4), config.SPOOKY_SMALLER_FONT, config.yellow)
 
    buttons = [
        Button("START GAME", config.white, config.SPOOKY_SMALL_FONT, ((config.display_width / 2), (config.display_height / 1.1)), gameDisplay),
    ]
      
    while True:
        for event in pygame.event.get():

            if (event.type == pygame.QUIT):
                pygame.quit()
                quit()
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                return gameDisplay
        
        for button in buttons:
            Button.check_Hover(button, gameDisplay)
        pygame.display.update()
        clock.tick(15)
    return gameDisplay