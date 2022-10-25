import pygame
from pygame.locals import *

GREEN = (34, 102, 2)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 165, 0)
BLUE = (0, 0, 205)
BLACK = (0, 0, 0)

def event_handler():
    for event in pygame.event.get():
        """print(event)"""
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()
        if event.type == VIDEORESIZE:
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    pygame.display.update()

def main():

    display_width = 1024
    display_height = 595
    screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    pygame.display.set_caption('Флаг')

    pygame.draw.rect(screen, WHITE, pygame.Rect(0, 0, 1024, 595))
    pygame.draw.rect(screen, RED, pygame.Rect(440, 0, 584, 200))
    pygame.draw.rect(screen, BLUE, pygame.Rect(440, 400, 584, 200))
    pygame.draw.polygon(screen, BLUE, [[245, 595], [440, 595], [440, 399]])
    pygame.draw.polygon(screen, RED, [[245, 0], [440, 199], [440, 0]])
    pygame.draw.polygon(screen, GREEN, [[0, 0], [210, 0], [430, 215], [430, 380], [210, 595], [0, 595]])
    pygame.draw.polygon(screen, GREEN, [[430, 215], [430, 380], [1024, 380], [1024, 215]])
    pygame.draw.polygon(screen, YELLOW, [[0, 0], [0, 595], [300, 300]])
    pygame.draw.polygon(screen, BLACK, [[0, 40], [0, 555], [260, 300]])

    while True:
        event_handler()

main()
