import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

def drawCar():

    glutInit()

    glClearColor(0.6, 0.6, 0.6, 1.0)  # Тут цвет фона

    glPushMatrix()

    glColor3ub(236, 151, 4)
    glTranslated(0, 0, 0)
    glutSolidCube(0.5)

    glColor3ub(236, 0, 0)
    glTranslated(-0.6, 0, 0.125)
    glutSolidCube(0.75)
    glTranslated(0.6, 0, -0.125)
    glutSolidCube(0.05)
    glTranslated(-1, 0, 0.125)
    glutSolidCube(0.75)
    glTranslated(1, 0, -0.125)
    glutSolidCube(0.05)

    glColor3ub(0, 0, 0)
    glTranslated(-1, -0.3, -0.3)
    glutSolidSphere(0.1, 20, 20)
    glTranslated(0, 0.6, 0)
    glutSolidSphere(0.1, 20, 20)
    glTranslated(1, -0.1, 0)
    glutSolidSphere(0.1, 20, 20)
    glTranslated(0, -0.4, 0)
    glutSolidSphere(0.1, 20, 20)
    glPopMatrix()

    glPushMatrix()

    glColor3ub(0, 0, 0)
    glTranslated(0.22, -0.1, 0.05)
    glutSolidCube(0.1)
    glColor3ub(0, 0, 0)
    glTranslated(0, 0.2, 0)
    glutSolidCube(0.1)
    glColor3ub(240, 0, 230)
    glTranslated(0, -0.1, -0.1)
    glutSolidCube(0.2)

    glPopMatrix()


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
