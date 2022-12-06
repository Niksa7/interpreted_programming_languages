import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

import math


def drawRect(fromX, toX, fromY, toY):
    glBegin(GL_QUADS)
    glVertex2f(fromX, fromY)
    glVertex2f(toX, fromY)
    glVertex2f(toX, toY)
    glVertex2f(fromX, toY)
    glEnd()


def drawCube(w, h, z):
    z = -z
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, z)
    glVertex3f(-w, h, z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, -h, -z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(-w, h, -z)
    glVertex3f(-w, h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(w, -h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(w, -h, z)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex3f(-w, -h, -z)
    glVertex3f(w, -h, -z)
    glVertex3f(w, -h, z)
    glVertex3f(-w, -h, z)
    glEnd()
    glBegin(GL_POLYGON)
    glVertex3f(-w, h, -z)
    glVertex3f(w, h, -z)
    glVertex3f(w, h, z)
    glVertex3f(-w, h, z)
    glEnd()




def drawCar():
    # кузов
    glColor3f(255, 0, 0)
    glTranslatef(0, 0, 0.5)
    drawCube(1, 0.5, 0.5)
    glTranslatef(0, 0, -0.5)

    # лобовая часть
    glColor3f(0.0, 0.5, 1.0)
    glTranslatef(1.5, 0, 0.4)
    drawCube(0.5, 0.4, 0.4)
    glTranslatef(-1.5, 0, -0.4)


    # колесо 1
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(-0.75, 0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(0.75, -0.25, 0)

    # колесо 2
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(-0.75, -0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(0.75, 0.25, 0)

    # колесо 3
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(-0.2, -0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(0.2, 0.25, 0)

    # колесо 4
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(-0.2, 0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(0.2, -0.25, 0)

    # колесо 5
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(1.5, 0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(-1.5, -0.25, 0)

    # колесо 6
    glColor3f(0.1, 0.1, 0.1)
    glTranslatef(1.5, -0.25, 0)
    drawCube(0.175, 0.1, 0.2)
    glTranslatef(-1.5, 0.25, 0)

    # диск 1
    glColor3f(1, 1, 1)
    glTranslatef(-0.75, 0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(0.75, -0.27, 0)

    # диск 2
    glColor3f(1, 1, 1)
    glTranslatef(-0.75, -0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(0.75, 0.27, 0)

    # диск 3
    glColor3f(1, 1, 1)
    glTranslatef(-0.2, -0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(0.2, 0.27, 0)

    # диск 4
    glColor3f(1, 1, 1)
    glTranslatef(-0.2, 0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(0.2, -0.27, 0)

    # диск 5
    glColor3f(1, 1, 1)
    glTranslatef(1.5, 0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(-1.5, -0.27, 0)

    # диск 6
    glColor3f(1, 1, 1)
    glTranslatef(1.5, -0.27, 0)
    drawCube(0.12, 0.1, 0.12)
    glTranslatef(-1.5, 0.27, 0)

    #фара 1
    glColor4f(1, 0.5, 0, 0)
    glTranslatef(1.95, 0.2, 0.2)
    drawCube(-0.075, 0.1, -0.04)
    glTranslatef(-1.95, -0.2, -0.2)

    # фара 2
    glTranslatef(1.95, -0.2, 0.2)
    drawCube(-0.075, 0.1, -0.04)
    glTranslatef(-1.95, 0.2, -0.2)

    # Лобовое стекло
    glColor4f(1, 1, 1, 0)
    glTranslatef(1.61, 0, 0.55)
    drawCube(0.4, 0.3, 0.15)
    glTranslatef(-1.61, 0, -0.55)

    # Ручка 1
    glColor4f(0.1, 0.1, 0.1, 0)
    glTranslatef(1.5, -0.31, 0.3)
    drawCube(0.05, 0.1, 0.02)
    glTranslatef(-1.5, 0.31, -0.3)

    # Ручка 2
    glColor4f(0.1, 0.1, 0.1, 0)
    glTranslatef(1.5, 0.31, 0.3)
    drawCube(0.05, 0.1, 0.02)
    glTranslatef(-1.5, -0.31, -0.3)

    # Боковое 1
    glColor4f(1, 1, 1, 0)
    glTranslatef(1.5, 0.31, 0.55)
    drawCube(0.3, 0.1, 0.15)
    glTranslatef(-1.5, -0.31, -0.55)

    # Боковое 2
    glColor4f(1, 1, 1, 0)
    glTranslatef(1.5, -0.31, 0.55)
    drawCube(0.3, 0.1, 0.15)
    glTranslatef(-1.5, 0.31, -0.55)


pygame.init()
display = (1200, 900)
scree = pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

glEnable(GL_DEPTH_TEST)
glEnable(GL_LIGHTING)
glShadeModel(GL_SMOOTH)
glEnable(GL_COLOR_MATERIAL)
glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

glEnable(GL_LIGHT0)
glLightfv(GL_LIGHT0, GL_AMBIENT, [0.5, 0.5, 0.5, 1])
glLightfv(GL_LIGHT0, GL_DIFFUSE, [1.0, 1.0, 1.0, 1])

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

glMatrixMode(GL_MODELVIEW)
gluLookAt(0, -8, 0, 0, 0, 0, 0, 0, 1)
viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
glLoadIdentity()

# init mouse movement and center mouse on screen
displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
mouseMove = [0, 0]
pygame.mouse.set_pos(displayCenter)

pygame.mouse.set_visible(False)
up_down_angle = 0.0
paused = False
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE or event.key == pygame.K_RETURN:
                run = False
            if event.key == pygame.K_PAUSE or event.key == pygame.K_p:
                paused = not paused
                pygame.mouse.set_pos(displayCenter)
        if not paused:
            if event.type == pygame.MOUSEMOTION:
                mouseMove = [event.pos[i] - displayCenter[i] for i in range(2)]
            pygame.mouse.set_pos(displayCenter)

    if not paused:
        # get keys
        keypress = pygame.key.get_pressed()
        # mouseMove = pygame.mouse.get_rel()

        # init model view matrix
        glLoadIdentity()

        # apply the look up and down
        up_down_angle += mouseMove[1] * 0.1
        glRotatef(up_down_angle, 1.0, 0.0, 0.0)

        # init the view matrix
        glPushMatrix()
        glLoadIdentity()
        ms = 0.06
        # apply the movement
        if keypress[pygame.K_w]:
            glTranslatef(0, 0, ms)
        if keypress[pygame.K_s]:
            glTranslatef(0, 0, -ms)
        if keypress[pygame.K_d]:
            glTranslatef(-ms, 0, 0)
        if keypress[pygame.K_a]:
            glTranslatef(ms, 0, 0)

        # apply the left and right rotation
        glRotatef(mouseMove[0] * 0.1, 0.0, 1.0, 0.0)

        # multiply the current matrix by the get the new view matrix and store the final vie matrix
        glMultMatrixf(viewMatrix)
        viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)

        # apply view matrix
        glPopMatrix()
        glMultMatrixf(viewMatrix)

        glLightfv(GL_LIGHT0, GL_POSITION, [1, -1, 1, 0])

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()

        drawCar()

        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)

pygame.quit()
