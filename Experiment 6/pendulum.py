from typing import Tuple
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import pi, sqrt, cos, radians, sin
import numpy

WINDOW_SIZE = 1000
TARGET_FPS = 60

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def get_details() -> Tuple[float, float, float, float]:
    pendulum_length = float(input("Enter Pendulum Length: "))
    bob_radius = float(input("Enter Bob Radius: "))
    max_displacement_angle = float(input("Enter Max Displacement Angle: "))
    speed_multiplier = float(input("Enter Speed Multiplier: "))
    return pendulum_length, bob_radius, max_displacement_angle, speed_multiplier

def draw_circle(x: float, y: float, bob_radius: float):
    i = 0.0        
    glBegin(GL_TRIANGLE_FAN)    
    glVertex2f(x, y);
    for i in numpy.arange(0, 360.0, 1.0):
        glVertex2f(bob_radius*cos(pi * i / 180.0) + x, bob_radius*sin(pi * i / 180.0) + y)
    glEnd();

def draw_pendulum(global_x: float, global_y: float, bob_radius: float):
    glClear(GL_COLOR_BUFFER_BIT) 
    glColor3f(1.0,0.0,0.0) 
    glLineWidth(5)
    glBegin(GL_LINES)
    glVertex2f(0,0)
    glVertex2f(global_x, global_y)
    glEnd()
    draw_circle(global_x, global_y, bob_radius)
    glutSwapBuffers()

def update(state: int, theta: float, max_theta: float, theta_increment: float, pendulum_length: float, speed_multiplier: float, global_x: float, global_y: float):
    glutPostRedisplay()
    glutTimerFunc(int(1000/TARGET_FPS),update,int(0))
    if(state == 1):
        if(theta<max_theta):
            theta = theta + theta_increment
        else:
            state =-1
    elif(state == -1):
        if(theta >= -max_theta):
            theta = theta - theta_increment

        else:
            state=1
    global_x = pendulum_length * sin(radians(theta))
    global_y = - (pendulum_length * cos(radians(theta)))
    theta_increment =  (cos(radians(theta))*speed_multiplier)-(cos(radians(MAX_THETA))*(SPEED_MULTIPLIER*0.9))

def display_window(theta: float, max_theta: float, theta_increment: float, pendulum_length: float, speed_multiplier: float, bob_radius: float):
    global_x = global_y = 0
    state = 1
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(WINDOW_SIZE/2, WINDOW_SIZE/2)
    glutInitWindowPosition(0,0)
    glutCreateWindow("Pendulum")
    glutDisplayFunc(lambda: draw_pendulum(global_x, global_y, bob_radius))
    glutTimerFunc(0, lambda: update(state, theta, max_theta, theta_increment, pendulum_length, speed_multiplier, global_x, global_y), 0)
    glutIdleFunc(lambda: draw_pendulum(global_x, global_y, bob_radius))
    init()
    glutMainLoop()

def main():
    pendulum_length, bob_radius, max_theta, speed_multiplier = get_details()
    theta = max_theta
    theta_increment = cos(radians(theta))*speed_multiplier - cos(radians(max_theta))*speed_multiplier*0.9
    display_window(theta, max_theta, theta_increment, pendulum_length, speed_multiplier, bob_radius)

if __name__ == "__main__":
    main()