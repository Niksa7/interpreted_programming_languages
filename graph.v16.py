import pygame
from pygame.locals import *

GREEN = (34, 102, 2)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 215, 0)
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
    display_height = 768
    screen = pygame.display.set_mode((display_width, display_height), pygame.RESIZABLE)
    pygame.display.set_caption('Флаг')

    pygame.draw.rect(screen, GREEN, pygame.Rect(0, 0, 305, 768))
    pygame.draw.rect(screen, RED, pygame.Rect(305, 0, 715, 768))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(715, 0, 1024, 768))
    pygame.draw.polygon(screen, YELLOW, [[510, 245], [480, 350], [370, 350], [460, 415], [425, 520], [510, 450], [600, 520], [565, 415], [660, 350], [545, 350], [510, 245]])


    while True:
        event_handler()

main()
