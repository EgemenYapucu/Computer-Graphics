# Egemen Yapucu 18120205027
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys

X_AXIS = 0
Y_AXIS = 0
Z_AXIS = 0
DIRECTION = 1
# 0 Anında küpün baktığı yer
rangle = 1
# Teapotun başlangıçtaki dönme açısı
zoom = 1


# Küpü ve çaydanlığı çizip döndürür(3 boyutlu oldukları farkedilsin diye)
def draw():
    global X_AXIS, Y_AXIS, Z_AXIS
    global DIRECTION
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glEnable(GL_DEPTH_TEST)
    glViewport(0, 0, 250, 250)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    glColor3f(0, 0, 1)
    gluPerspective(45.0, float(500) / float(500), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glScale(zoom, zoom, zoom)

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -6.0)

    # Küpü döndürür
    glRotatef(X_AXIS, 1.0, 0.0, 0.0)
    glRotatef(Y_AXIS, 0.0, 1.0, 0.0)
    glRotatef(Z_AXIS, 0.0, 0.0, 1.0)

    # Küpü çizdirir
    glBegin(GL_QUADS)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(1.0, 1.0, 1.0)

    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, -1.0)

    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(-1.0, 1.0, 1.0)
    glVertex3f(-1.0, 1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glColor3f(1.0, 0.0, 1.0)
    glVertex3f(1.0, 1.0, -1.0)
    glVertex3f(1.0, 1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glEnd()

    X_AXIS = X_AXIS - 0.01
    Z_AXIS = Z_AXIS - 0.01

    global rangle
    glViewport(250, 0, 250, 250)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glColor3f(0, 0, 1)  # Mavi renk
    glRotatef(rangle, 1, 1, 0)
    glutWireTeapot(0.2)
    glPopMatrix()
    rangle += 0.05

    glutSwapBuffers()
    glFlush()


# Mouse tekerleğiyle zoomu ayarlar.
def mousewheel(*args):
    global zoom
    print(args)
    if args[1] == -1:
        zoom -= 0.05
    elif args[1] == 1:
        zoom += 0.05
    else:
        pass
    glutPostRedisplay()


# A ve D tuşları ile hareketi sağlar.
def leftright(*args):
    global X_AXIS
    if args[1] == 'a':
        X_AXIS += 1
    elif args[1] == 'd':
        X_AXIS -= 1
    else:
        pass
    glutPostRedisplay()


# Gerekli fonksiyonları çağırır.
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow(b"3D Cube and Teapot")
    glutDisplayFunc(draw)
    glutIdleFunc(draw)
    glutMouseWheelFunc(mousewheel)
    glutKeyboardFunc(leftright)
    glutMainLoop()


if __name__ == "__main__":
    main()
