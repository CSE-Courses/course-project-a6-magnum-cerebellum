import pygame
import config
import math
pygame.init()
first_time = pygame.time.get_ticks()


def setup(intermediate):
    intermediate_surface = intermediate.get_rect()
    first = config.red

    wid, hei = intermediate.get_width() , intermediate.get_height()

    #creates the starting y position and ending y position for the panel
    y_coord = intermediate_surface[1]
    end_y_coord = intermediate_surface[3] +y_coord
    end_y_coord = end_y_coord - y_coord

    #creates the starting x position and ending x position for the panel
    x_coord = intermediate_surface[0]
    end_x_coord = intermediate_surface[2] + x_coord

    second = config.black

    #calculates the rate of change for the color so transitions look nice
    change_of_color = (float((second[0]-first[0])/end_y_coord), (float(second[1]-first[1])/end_y_coord),
                      (float(second[2]-first[2])/end_y_coord))
    #implements the color change to every 'line'
    for line in range(y_coord,end_y_coord):
         color = (min (max(first[0]+(change_of_color[0]*line),0),255), min(max(first[1]+(change_of_color[1]*line),0),255),
                  min(max(first[2]+(change_of_color[2]*line),0),255))
         pygame.draw.line(intermediate, color, (x_coord, line),(end_x_coord, line))


def iterate_over_input(intermediate,y):
    #iterates over all 7 values of the input text and displays them onto the actviites panel
    holding_time = 3
    global first_time #626
    for elems in config.text1:
        # if pygame.time.get_ticks() - first_time >= holding_time:
        if(type(elems) == tuple):
            intermediate.blit(config.SPOOKY_SMALLER_FONT.render("Current location:" + str(elems), True, config.white), (10, y))
        elif(type(elems) != tuple):
            intermediate.blit(config.SPOOKY_SMALLER_FONT.render("You have " + str(elems), True, config.white), (10, y))

        y += 40
        config.storage.append([elems])
            # first_time = pygame.time.get_ticks()
        if (y > 300 and len(config.text1) >= 8 and config.counter == 1):
            setup(intermediate)
            config.text1 = config.text1[6:8]

