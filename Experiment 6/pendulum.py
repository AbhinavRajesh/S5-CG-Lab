from typing import Tuple
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi, sqrt, cos, radians, sin
import numpy

WINDOW_SIZE = 1000
TARGET_FPS=60
GLOBAL_X = GLOBAL_Y = 0
STATE = 1
pendulum_length = float(input("Pendulum Length: "))
BOB_RADIUS = float(input("Bob Radius: "))
MAX_THETA = float(input("Max Displacement Angle: "))
THETA = MAX_THETA
SPEED_MULTIPLIER = float(input("Speed Multiplier: "))
THETA_INCREMENT = cos(radians(THETA))*SPEED_MULTIPLIER - cos(radians(MAX_THETA))*SPEED_MULTIPLIER*0.9
 
def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def draw_circle(x: float, y: float, bob_radius: float):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)    
    glVertex2f(x, y);
    for i in numpy.arange(0, 360.0, 1.0):
        glVertex2f(bob_radius*cos(pi * i / 180.0) + x, bob_radius*sin(pi * i / 180.0) + y)
    glEnd();

def draw_pendulum():
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,0.0,0.0) 
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(GLOBAL_X, GLOBAL_Y)
    glEnd()
    draw_circle(GLOBAL_X, GLOBAL_Y, BOB_RADIUS)
    glutSwapBuffers()

def update(value):
    global GLOBAL_X
    global GLOBAL_Y
    global STATE
    global THETA
    global MAX_THETA
    global THETA_INCREMENT
    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,int(0))
    if(STATE == 1):
        if(THETA < MAX_THETA):
            THETA = THETA + THETA_INCREMENT
        else:
            STATE = -1
    elif(STATE == -1):
        if(THETA >= -MAX_THETA):
            THETA = THETA - THETA_INCREMENT

        else:
            STATE = 1
    GLOBAL_X = pendulum_length * sin(radians(THETA))
    GLOBAL_Y = - (pendulum_length * cos(radians(THETA)))
    THETA_INCREMENT =  (cos(radians(THETA))*SPEED_MULTIPLIER)-(cos(radians(MAX_THETA))*(SPEED_MULTIPLIER*0.9))

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(draw_pendulum)
    glutTimerFunc(0, update, 0)
    glutIdleFunc(draw_pendulum)
    init()
    glutMainLoop()
if __name__ == "__main__":
    main()