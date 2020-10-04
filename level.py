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
    pygame.display.update()

pygame.quit()