import pygame
from pygame.locals import *

GREEN = (0, 102, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 205, 13)
BLACK = (0, 0, 0)

def event_handler():
    for event in pygame.event.get():
        """print(event)"""
        if event.type == QUIT or (event.type == KEYDOWN and (event.key == K_ESCAPE or event.key == K_q)):
            pygame.quit()
            quit()
    pygame.display.update()

def main():

    display_width = 1024
    display_height = 720
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Флаг')

    pygame.draw.rect(screen, GREEN, pygame.Rect(0, 0, 1024, 720))
    pygame.draw.rect(screen, RED, pygame.Rect(612, 0, 512, 240))
    pygame.draw.rect(screen, RED, pygame.Rect(612, 480, 512, 240))
    pygame.draw.polygon(screen, (255, 0, 0), (612, 480, 512, 240), 0)

    while True:
        event_handler()

main()
