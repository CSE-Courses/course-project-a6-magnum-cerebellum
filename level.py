import pygame
import config

gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))


x = 50
y = 50
player_width = 40
player_height = 60
velocity = 25
health = 100
score = 0

run = True


def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()


#mainloop
score_font = pygame.font.SysFont('comicsans',30, True)
# health_font = pygame.font.SysFont('comicsans',30, True)

def health_func():
    text = score_font.render('Health: ' + str(health), 1, (0, 255, 0))
    gameDisplay.blit(text, (860, 10))
    pygame.display.update()

def score_func():
    text = score_font.render('Score: ' + str(score), 1, (255,0,0))
    gameDisplay.blit(text, (860,60))
    pygame.display.update()

while(run):
    w, h = pygame.display.get_surface().get_size()
    pygame.time.delay(120)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > velocity:
        x = x - velocity
    if keys[pygame.K_RIGHT] and x < w - player_width - velocity:
        x = x + velocity
    if keys[pygame.K_UP] and y > velocity:
        y = y - velocity
    if keys[pygame.K_DOWN] and y < h - player_height - velocity:
        y = y + velocity
    gameDisplay.fill((0,0,0))
    pygame.draw.rect(gameDisplay, (255,0,0), (x, y, player_width, player_height))
    health_func()
    score_func()

    mouse = pygame.mouse.get_pos()

    if 100+100 > mouse[0] > 100 and 650 + 50 > mouse [1] > 650 :
        pygame.draw.rect(gameDisplay, (0, 255, 0), (100, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 150, 0), (240, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 580, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 715, 100, 50))
    if 240 + 100 > mouse[0] > 240 and 650 + 50 > mouse[1] > 650:
        pygame.draw.rect(gameDisplay, (0, 150, 0), (100, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 255, 0), (240, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 580, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 715, 100, 50))

    else:
        pygame.draw.rect(gameDisplay, (0, 150, 0), (100, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 150, 0), (240, 650, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 150, 0), (170, 580, 100, 50))
        pygame.draw.rect(gameDisplay, (0, 150, 0), (170, 715, 100, 50))
    bg = pygame.image.load("Mockup1.jpg")

    SPOOKY_SMALL_FONT = pygame.font.Font("assets/fonts/CHILLER.ttf", 20) #changed the size here
    textSurf, textRect = text_objects("Left", SPOOKY_SMALL_FONT)
    textRect.center = ((100 + (100/2)), (650 + (50/2)))
    textSurf1, textRect1 = text_objects("Right", SPOOKY_SMALL_FONT)
    textRect1.center = ((240 + (100/2)), (650 + (50/2)))

    textSurf2, textRect2 = text_objects("Up", SPOOKY_SMALL_FONT)
    textRect2.center = ((170 + (100 / 2)), (580 + (50 / 2)))
    textSurf3, textRect3 = text_objects("Down", SPOOKY_SMALL_FONT)
    textRect3.center = ((170 + (100 / 2)), (715 + (50 / 2)))
    gameDisplay.blit(textSurf, textRect)
    gameDisplay.blit(textSurf1, textRect1)
    gameDisplay.blit(textSurf2, textRect2)
    gameDisplay.blit(textSurf3, textRect3)

    gameDisplay.blit(bg, (0, 0))


    pygame.display.update()

pygame.quit()