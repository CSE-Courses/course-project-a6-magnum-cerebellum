import pygame
import config

clock = pygame.time.Clock()


def blit_text(display, text, text_block_size, pos, font, color):
    words = []
    lines = text.splitlines()
    for aline in lines:
        words.append(aline.split())
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = text_block_size
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            display.blit(word_surface, (x, y))
            pygame.display.update()
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

    
    pygame.display.update()



    