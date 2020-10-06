import pygame
import config
from player import Player
gameDisplay = pygame.display.set_mode((config.display_width, config.display_height))

pygame.init()

health = 100
score = 0
clock = pygame.time.Clock()
lead_x = 300
lead_y = 300

# for actions = (115, 545)

def text_objects(text, font):
    textSurface = font.render(text, True, (0,0,0))
    return textSurface, textSurface.get_rect()

score_font = pygame.font.SysFont('comicsans',30, True)

def message_to_screen(msg, color):
    w, h = pygame.display.get_surface().get_size()
    screen_text = font.render(msg,True,color)
    textSurf, textRect = text_objects(msg, color)
    textRect.center = ((w/2), (h/2))
    gameDisplay.blit(textSurf,textRect)

def pause():
    paused = True
    font = config.SPOOKY_INVENTORY_FONT
    text = font.render('Pause', True, (0,255,0), (0,0,128))
    textRect = text.get_rect()
    textRect.center = (config.display_width/2, config.display_height/2)
    img = pygame.image.load("pause_menu.jpg")
    gameDisplay.fill((42,4,1))
    gameDisplay.blit(img, (1024/4,768/4))
    # gameDisplay.fill((255, 255, 255))
    # gameDisplay.blit(text, textRect)

    while(paused):
        for event in pygame.event.get():
            # if event.type == pygame.QUIT:
            #     pygame.quit()
            #     quit()
            if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_c:
            #         paused = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()
        pygame.display.update()
        clock.tick(5)

def health_func():
    text = score_font.render('Health: ' + str(health), 1, (0, 255, 0))
    gameDisplay.blit(text, (config.display_width/1.422222,config.display_height/2.69473684211))
    pygame.display.update()

def score_func():
    text = score_font.render('Score: ' + str(score), 1, (255,0,0))
    gameDisplay.blit(text, (config.display_width/1.422222,config.display_height/2.4380952381))
    pygame.display.update()


def left():
    # gameDisplay.fill((0,0,0))
    lef = pygame.image.load("left_arrow.jpg")
    pygame.draw.rect(gameDisplay, (0, 150, 0), (710, 490, 70, 70))
    gameDisplay.blit(lef, (715,495))


def right():
    rig = pygame.image.load("right_arrow.jpg")
    pygame.draw.rect(gameDisplay, (0, 150, 0), (890, 490, 70, 70))
    gameDisplay.blit(rig, (895,495))


def up():
    u = pygame.image.load("up_arrow.jpg")
    pygame.draw.rect(gameDisplay, (0, 150, 0), (800, 400, 70, 70))
    gameDisplay.blit(u, (805, 405))

def down():
    dow = pygame.image.load("down_arrow.jpg")
    pygame.draw.rect(gameDisplay, (0, 150, 0), (800, 490, 70, 70))
    gameDisplay.blit(dow, (805, 495))


# a = Player((50,50), 100, None, None, None )

# def start_main():
#     left()
#     while True:
#         pygame.display.update


def start_main():
    usr_text = ''
    bg = pygame.image.load("Mockup1.jpg")
    x = 50
    y = 50
    player_width = 40
    player_height = 60
    velocity = 25

    run = True


    while(run):
        mouse = pygame.mouse.get_pos()

        w, h = pygame.display.get_surface().get_size()
        pygame.time.delay(10)
        gameDisplay.blit(bg, (0, 0))


        # jesse = pygame.image.load("jesse.jpg")
        # gameDisplay.blit(jesse, (100,100))
        gameDisplay.fill((0, 0, 0), rect = [0,0,670,485])
        pygame.draw.rect(gameDisplay, (255, 0, 0), (x, y, player_width, player_height))

        left()
        right()
        up()
        down()
        health_func()
        score_func()



        keys = pygame.key.get_pressed()
        if (keys[pygame.K_LEFT] and x > velocity):
            gameDisplay.fill((255, 255, 255))
            # font = config.SPOOKY_SMALL_FONT
            # text = font.render('Pause', True, (0, 255, 0), (0, 0, 128))
            # textRect = text.get_rect()
            # textRect.center = (300, 800)
            # gameDisplay.blit(text, textRect)
            x = x - velocity

        if keys[pygame.K_RIGHT] and x < 670 - player_width - velocity:
            x = x + velocity
        if keys[pygame.K_UP] and y > velocity:
            y = y - velocity
        if keys[pygame.K_DOWN] and y < 485 - player_height - velocity:
            # gameDisplay.fill((255,255,255))
            # d = pygame.image.load("dark_down_arrow.jpg")
            # gameDisplay.blit(d, (805, 495))
            y = y + velocity

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pause()
                if(event.key == pygame.K_BACKSPACE):
                    usr_text = usr_text[0:-1]
                else:
                    usr_text += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN and 715 + 70 > mouse[0] > 715 and 495 + 70 > mouse[1] > 495 and x > velocity: #left
                gameDisplay.fill((0,0,0))
                font = config.SPOOKY_SMALL_FONT
                text = font.render('Pause', True, (0, 255, 0), (0, 0, 128))
                textRect = text.get_rect()
                textRect.center = (300, 800)
                gameDisplay.blit(text, textRect)
                x = x - velocity

            if event.type == pygame.MOUSEBUTTONDOWN and 895 + 70 > mouse[0] > 895 and 495 + 70 > mouse[1] > 495 and x < 670 - player_width - velocity: #right
                x = x + velocity
            if event.type == pygame.MOUSEBUTTONDOWN and 805 + 70 > mouse[0] > 805 and 495 + 70 > mouse[1] > 495 and y < 485 - player_height - velocity:#down
                y = y + velocity
            if event.type == pygame.MOUSEBUTTONDOWN and 805 + 70 > mouse[0] > 805 and 405 + 70 > mouse[1] > 405 and y > velocity:#up
                y = y - velocity
            text_surf = config.SPOOKY_SMALL_FONT.render(usr_text, True ,(0,0,0))
            gameDisplay.blit(text_surf,(0,0))

        # if 100+100 > mouse[0] > 100 and 650 + 50 > mouse [1] > 650 :
        # pygame.draw.rect(gameDisplay, (0, 255, 0), (100, 650, 100, 50))
        # pygame.draw.rect(gameDisplay, (0, 150, 0), (240, 650, 100, 50))
        # pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 580, 100, 50))
        # pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 715, 100, 50))
        # if 240 + 100 > mouse[0] > 240 and 650 + 50 > mouse[1] > 650:
        #     pygame.draw.rect(gameDisplay, (0, 150, 0), (100, 650, 100, 50))
        #     pygame.draw.rect(gameDisplay, (0, 255, 0), (240, 650, 100, 50))
        #     pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 580, 100, 50))
        #     pygame.draw.rect(gameDisplay, (0, 255, 0), (170, 715, 100, 50))
        #
        # else:
        #
        #
        #
        #



        # gameDisplay.blit(textSurf, textRect)
        # gameDisplay.blit(textSurf1, textRect1)
        # gameDisplay.blit(textSurf2, textRect2)
        # gameDisplay.blit(textSurf3, textRect3)

    pygame.display.update()

start_main()
pygame.quit()
quit()