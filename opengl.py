# pip install PyOpenGL PyOpenGL_accelerate
# pip install pygame
# pip install numpy

import pygame
import numpy as np

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

verticies = (
    (1, -1, -1),    # 0
    (1, 1, -1),     # 1
    (-1, 1, -1),    # 2
    (-1, -1, -1),   # 3
    (1, -1, 1),     # 4
    (1, 1, 1),      # 5
    (-1, -1, 1),    # 6
    (-1, 1, 1)      # 7
    )

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (2, 1),
    (2, 3),
    (2, 7),
    (6, 3),
    (6, 4),
    (6, 7),
    (5, 1),
    (5, 4),
    (5, 7)
    )

faces = (
    (1, 0, 4, 5),  # X positivo
    (2, 3, 6, 7),  # X negativo
    (2, 1, 5, 7),  # Y positivo
    (3, 0, 4, 6),  # Y negativo
    (5, 4, 6, 7),  # Z positivo
    (0, 1, 2, 3)  # Z negativo
    )


def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def Cube2(p, l):
    glBegin(GL_QUADS)
    for face in faces:
        for vertex in face:
            v = (np.array(verticies[vertex]) + np.array(p)) * l
            glVertex3fv(v)
    glEnd()


def desenhoR():
    tamanhoDeLado = 0.04

    for i in range(-10, 10):
        Cube2((-7, i, 0), tamanhoDeLado)

    for k in range(-7, 7):
        Cube2((k,10,0), tamanhoDeLado)

    for i in range(-7, 7):
        Cube2((i,0,0), tamanhoDeLado)
    
    Cube2((7, 8, 0), tamanhoDeLado)
    Cube2((8, 7, 0), tamanhoDeLado)
    Cube2((9, 6, 0), tamanhoDeLado)
    Cube2((10,5,0), tamanhoDeLado)
    Cube2((9, 4, 0), tamanhoDeLado)
    Cube2((8, 3, 0), tamanhoDeLado)
    Cube2((7, 2, 0), tamanhoDeLado)
    Cube2((6, 1, 0), tamanhoDeLado)
        
    for i in range(11):
        Cube2((i,-i,0), tamanhoDeLado)


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        desenhoR()
        
        pygame.display.flip()
        pygame.time.wait(10)

main()
