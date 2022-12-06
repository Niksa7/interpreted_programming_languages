import math
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def func():

    glutInit()
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
    displayCenter = [scree.get_size()[i] // 2 for i in range(2)]
    mouseMove = [0, 0]
    pygame.mouse.set_pos(displayCenter)

    pygame.mouse.set_visible(False)
    up_down_angle = 0.0
    paused = False
    run = True

    ambient = (0, 0, 0, 1)
    lightpos = (2, 2, 2)
    coef = 0

    # Lighting
    glLightModelfv(GL_LIGHT_MODEL_AMBIENT, ambient)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

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
            # apply the movment
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

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # Clear the screen
        lightpos = (-1.5 ** math.cos(coef), -1.5 ** math.cos(coef), 2.0)
        coef += 0.1

        # glPushMatrix()

        glLightfv(GL_LIGHT0, GL_POSITION, lightpos)

        # # Clear the color and depth buffers
        glClearColor(0.6, 0.6, 0.6, 1.0)  # Тут цвет фона

        glPushMatrix()  # перед акс
        glColor3ub(236, 151, 4)
        glTranslated(0, 0.1, -0.54)
        glutSolidCube(0.05)
        glTranslated(0.3, 0, 0)
        glutSolidCube(0.05)

        glColor3ub(234, 234, 234)
        glTranslated(-0.15, -0.08, 0)
        glutSolidCube(0.05)
        glTranslated(-0.05, 0, 0)
        glutSolidCube(0.05)
        glTranslated(0.1, 0, 0)
        glutSolidCube(0.05)
        glPopMatrix()

        glPushMatrix()  # зад акс
        glColor3ub(255, 0, 0)
        glTranslated(0, 0.1, 0.04)
        glutSolidCube(0.05)
        glTranslated(0.05, 0, 0)
        glutSolidCube(0.05)
        glTranslated(0.2, 0, 0)
        glutSolidCube(0.05)
        glTranslated(0.05, 0, 0)
        glutSolidCube(0.05)

        glColor3ub(234, 234, 234)
        glTranslated(-0.15, -0.08, 0)
        glutSolidCube(0.05)
        glTranslated(-0.05, 0, 0)
        glutSolidCube(0.05)
        glTranslated(0.1, 0, 0)
        glutSolidCube(0.05)
        glPopMatrix()

        for i in range(4):
            glPushMatrix()
            glColor3ub(0, 0, 0)
            glTranslated(0.32 * (i % 2), 0, -0.1 - 0.3 * int(i / 2))
            glutSolidSphere(0.1, 20, 20)
            glPopMatrix()
        for i in range(24):
            glPushMatrix()
            glColor3ub(0, 0, 150)
            glTranslated(0.1 * (i % 4), 0, -0.1 * int(i / 4))
            glutSolidCube(0.1)
            glPopMatrix()
        for i in range(24):
            glPushMatrix()
            glColor3ub(0, 0, 150)
            glTranslated(0.1 * (i % 4), 0.1, -0.1 * int(i / 4))
            glutSolidCube(0.1)
            glPopMatrix()

        for i in range(12):
            glPushMatrix()
            glColor3ub(201, 220, 226)
            glTranslated(0.1 * (i % 4), 0.2, -0.1 - 0.1 * int(i / 4))
            glutSolidCube(0.1)
            glPopMatrix()

        pygame.display.flip()  # Update the screen
        pygame.time.wait(10)

    pygame.quit()


if __name__ == '__main__':
    func()

