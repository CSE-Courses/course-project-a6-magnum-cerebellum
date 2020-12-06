import config
import pygame
from button import Button
import format_text
import config
import game
import music
import music_choice
import format_text
from button import Button
clock = pygame.time.Clock()

# Renders win screen once player has defeated final enemy
def win_screen(gameDisplay, player):
    
    music_player = music.Music_Player()
    music_player.play_victory
    music_player.set_volume(0.5)
    music_choice.win()
    gameDisplay.fill(config.black)
    buttons = [
        Button("QUIT", config.white, config.SPOOKY_SMALL_FONT,
               ((config.display_width / 2), (config.display_height / 1.2)),
               gameDisplay),
        ]
    text = f'Congratulations, {player.character}! You have escaped from the depths of Davis Hall.... \n Or have you? To be continued....'
    while True:
        format_text.blit_text(gameDisplay, text, (config.display_width/1.5, config.display_height), (config.display_width/2.5, config.display_height/5), config.SPOOKY_SMALL_FONT, config.red)

        for event in pygame.event.get():
            if (event.type == pygame.QUIT or
                    (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].text == "QUIT" and buttons[0].rect.collidepoint
                        (pygame.mouse.get_pos()))):
                pygame.quit()
                quit()
          
        for button in buttons:
            Button.check_Hover(button, gameDisplay)
    
        pygame.display.update()
        clock.tick(15)

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
            #clicked start game
            elif (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[0].rect.collidepoint(pygame.mouse.get_pos())):
                print("Clicked Start Game")
                game.GameMain(gameDisplay, player.character)

        
        for button in buttons:
            Button.check_Hover(button, gameDisplay)
        pygame.display.update()
        clock.tick(15)
    return gameDisplay