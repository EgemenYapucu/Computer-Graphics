#Egemen Yapucu 18120205027
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *
import sys

p = 0
j = 0


#initialaze the axis
def init():
    glClearColor(1.0, 1.0, 1.0, 1.0)
    gluOrtho2D(-60.0, 60.0, -60.0, 60.0)

# draws the picture
def drawing():
    global p
    global j
    glClear(GL_COLOR_BUFFER_BIT)
    glPointSize(3.0)

    # Car draw
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(-60.0, -39.0)
    glVertex2f(60.0, -39.0)
    glVertex2f(60.0, -60.0)
    glVertex2f(-60, -60)

    glColor3f(0.3, 0.0, 0.3)
    glVertex2f(-50 + p, -30)
    glVertex2f(-30 + p, -30)
    glVertex2f(-30 + p, -35)
    glVertex2f(-50 + p, -35)

    glColor3f(0, 0, 1)
    glVertex2f(-45 + p, -25)
    glVertex2f(-35 + p, -25)
    glVertex2f(-35 + p, -30)
    glVertex2f(-45 + p, -30)

    glColor3f(0.7, 0.5, 0.0)
    glVertex2f(30, -15)
    glVertex2f(40, -15)
    glVertex2f(40, -39)
    glVertex2f(30, -39)

    glEnd()
    glBegin(GL_TRIANGLES)

    glColor3f(0.0, 0.3, 0.0)
    glVertex2f(15, -15)
    glVertex2f(55, -15)
    glVertex2f(35, 40)

    glEnd()
    glBegin(GL_POLYGON)

    #Sun and the car's wheels
    for i in range(60):
        a = 4 * cos(i * pi / 10) + p
        b = 2 * sin(i * pi / 10)

        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(a-35, b-37)

    glEnd()
    glBegin(GL_POLYGON)

    for i in range(60):
        a = 4 * cos(i * pi / 10) + p
        b = 2 * sin(i * pi / 10)
        glColor3f(0.0, 0.0, 0.0)
        glVertex2f(a - 45, b - 37)

    glEnd()
    glBegin(GL_POLYGON)


    for i in range(60):
        x = 4 * cos(i * pi / 10)
        y = 2 * sin(i * pi / 10)
        glColor3f(1.0, 0.5, 0.0)
        glVertex2f(x - 35 + j, y + 37)

    glEnd()
    glFlush()


#Suns rotations
    w = 1

    if j <= 55 and w == 1:
        j += 0.06
        if j > 53:
            w = 0
    else:
        j -= 0.06
        if j == 0:
            w = 1
    glutPostRedisplay()


def keyPressed(*args):
    global p
    if args[0] == b"d":
        if p <= 55:
            p += 1
    elif args[0] == b"a":
        if p>= -10:
            p -= 1
    glutPostRedisplay()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(60, 60)
    glutCreateWindow(b"Drawing")
    glutDisplayFunc(drawing)
    glutKeyboardFunc(keyPressed)
    init()
    glutMainLoop()


main()