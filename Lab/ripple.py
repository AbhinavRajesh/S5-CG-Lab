from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import sqrt
import sys

WINDOW_SIZE = 200
RADIUS = 7
OFFSET = 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

class Ripple:
    def __init__(self):
        self.radius = 30
        self.number_of_ripples = 1

    def display(self):
        self.create_ripple()
        glutSwapBuffers()

    def draw_circle(self, radius):
        points = []
        x = -radius
        target = radius
        increment_value = 1/50
        x += increment_value

        while x < target:
            offset = sqrt(radius**2 - x**2)
            points.append((x, offset))
            points.append((x, -offset))
            x += increment_value
        
        glColor3f(1, 0, 0)
        glBegin(GL_POINTS)
        for x, y in points:
            glVertex2f(x, y)
        glEnd()

    def create_ripple(self):
        for ripple in range(self.number_of_ripples):
            self.draw_circle(self.radius*(ripple+1))

    def update(self, value):
        self.number_of_ripples += 1
        glutPostRedisplay()
        glutTimerFunc(1000, self.update, 0)

def main():
    ripple = Ripple()
    print("Creating window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car | Abhinav Rajesh")
    glutDisplayFunc(ripple.display)
    glutTimerFunc(0, ripple.update, 0)
    glutIdleFunc(ripple.display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()