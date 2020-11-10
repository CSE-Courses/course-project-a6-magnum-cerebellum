import pygame
import config

paused = False

def render_text(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def load():
    with open('savedgame.pkl', 'rb') as file:
        print('Loading...')
        global loaddata
        loaddata = pickle.load(file)

#saves the character's stats onto a pickle file at the same directory level
def save(player1):
    with open('savedgame.pkl', 'wb') as file:
        print('Saving...')
        data = {'pos':(3,3), 'health':100, 'actions': ['punch','kick',], 'items':['Computer','Book'],'hp':100}
        pickle.dump(data, file)
        print('Saved!')

def set_image(image, display):
    image_surface = pygame.image.load(image)
    display.blit(image_surface, (0, 0))

def unpause():
    global paused
    paused = False
    # gameDisplay.fill(config.black)

def pause():

    gameDisplay.fill(config.black)
    font = config.SPOOKY_BIG_FONT

    buttons = [Button("Continue", config.white, config.SPOOKY_SMALL_FONT,
                      ((config.display_width / 2), (config.display_height / 2)), gameDisplay),
               Button("Change Settings", config.white, config.SPOOKY_SMALL_FONT,
                      ((config.display_width / 2), (config.display_height / 1.5)), gameDisplay),
               Button("Quit Level", config.white, config.SPOOKY_SMALL_FONT,
                      ((config.display_width / 2), (config.display_height / 1.20)), gameDisplay),
               Button("Exit Game", config.white, config.SPOOKY_SMALL_FONT,
                      ((config.display_width / 2), (config.display_height / 1.1)), gameDisplay)]
    text = font.render('Pause', True, config.red)
    textrect = text.get_rect()
    textrect.center = (round(config.display_width/2), round(config.display_height/5))


    gameDisplay.blit(text, textrect)


    while(paused):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and buttons[3].rect.collidepoint(pygame.mouse.get_pos())):
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and buttons[2].rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                main_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and buttons[1].rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                options_menu()
            elif event.type == pygame.MOUSEBUTTONDOWN and buttons[0].rect.collidepoint(pygame.mouse.get_pos()) and event.button == 1:
                # buttons[:] = []
                unpause()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    unpause()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        for button in buttons:
            Button.check_Hover(button, gameDisplay)

        pygame.display.update()
        clock.tick(5)

class Checkbox:
    def __init__(self):
        self.draw()

    def draw(self):
        pygame.draw.circle(gameDisplay, config.white, (150 ,150), 75)



def destroy(self, name_of_class):
    name_of_class.List.remove(self)
    del self