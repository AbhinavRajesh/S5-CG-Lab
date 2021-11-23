from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

WINDOW_SIZE = 500


def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def display():
    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1, 1, 1)
    glVertex2f(10, 10)
    glEnd()

print("Creating window...")
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
glutCreateWindow("Ball Rolling | Abhinav Rajesh")
glutDisplayFunc(display)
init()
glutMainLoop()