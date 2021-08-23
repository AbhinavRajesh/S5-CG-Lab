import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)            # Set Background Color
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)            # Set the Range of coordinate system

def plotpoints():
    glClear(GL_COLOR_BUFFER_BIT)                # Clear the entire window (Like clrscr() in C++)
    glColor3f(1.0, 0.0, 0.0)                    # Set color of the drawing
    glPointSize(10.0)                           # Set size of Pixels
    glBegin(GL_POINTS)
    glVertex2f(0.0, 0.0)                        # Plot the vertex
    glEnd()
    glFlush()                                   # Push the pixels to display


def main():
    glutInit(sys.argv)                          # Initializing the toolkit
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)   # Set the display mode
    glutInitWindowSize(500, 500)                # Specify the window size
    glutInitWindowPosition(50, 50)              # Set the position of window
    glutCreateWindow("Plot Origin")             # Title in windows
    glutDisplayFunc(plotpoints)                 # 
    init()
    glutMainLoop()


main()