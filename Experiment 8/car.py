from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import tan, cos, pi, sin, radians
import sys
import playsound

WINDOW_SIZE = 200
RADIUS = 7
OFFSET = 0

def init():
    glClearColor(0, 0, 0, 1)
    gluOrtho2D(-WINDOW_SIZE, WINDOW_SIZE, -WINDOW_SIZE, WINDOW_SIZE)

def draw_circle(x, y):
    global OFFSET
    glBegin(GL_TRIANGLE_FAN)
    for i in range(361):
        # glColor3f(cos(i), 0, cos(i))
        if i < 180:
            glColor3f(1, 0, 0)
        else:
            glColor3f(0, 1, 0)
        glVertex2f(RADIUS * cos(OFFSET + pi * i / 180) + x, RADIUS * sin(OFFSET + pi * i / 180) + y)
    glEnd()

class Car:
    def __init__(self):
        self.speed = 1
        self.angle = float(input("Enter the angle of inclination: "))
        self.x1, self.y1 = -WINDOW_SIZE, -WINDOW_SIZE * tan(radians(self.angle))
        self.x2, self.y2 = WINDOW_SIZE, WINDOW_SIZE * tan(radians(self.angle))
        self.x = self.y = 0
        if self.angle > 0:
            self.to_right = False
        else:
            self.to_right = True
        self.start_point = [0, 0]

    # Function to calculate the rotated points
    def get_rotated_points(self, vertices):
        points = []
        for x, y in vertices:
            points.append([round(x * cos(radians(self.angle)) - y * sin(radians(self.angle))), round(x * sin(radians(self.angle)) + y * cos(radians(self.angle)))])        
        return points

    def draw_car(self, x, y):
        # x *= cos(radians(self.angle))
        # y *= sin(radians(self.angle))
        if self.to_right:
            vertices = [
                [x, y + RADIUS],
                [x, y + 10 + RADIUS],
                [x + 10 , y + 10 + RADIUS],
                [x + 20 , y + 20 + RADIUS],
                [x + 40 , y + 20 + RADIUS],
                [x + 50 , y + 10 + RADIUS],
                [x + 60 , y + 10 + RADIUS],
                [x + 70 , y + RADIUS],
            ]
        else:
            vertices = [
                [x, y + RADIUS],
                [x + 10, y + 10 + RADIUS],
                [x + 30 , y + 10 + RADIUS],
                [x + 30 , y + 20 + RADIUS],
                [x + 50 , y + 20 + RADIUS],
                [x + 60 , y + 10 + RADIUS],
                [x + 70 , y + 10 + RADIUS],
                [x + 70 , y + RADIUS],
            ]

        rotated_vertices = self.get_rotated_points(vertices)

        tyres = [
            [x + 10, y + RADIUS],
            [x + 60, y + RADIUS],
        ]

        rotated_tyres = self.get_rotated_points(tyres)

        glLineWidth(2)
        glBegin(GL_POLYGON)
        for vertex in rotated_vertices:
            glVertex2fv(vertex)
        glEnd()

        for tyre in rotated_tyres:
            draw_circle(tyre[0], tyre[1])


    def create_line(self):
        glClear(GL_COLOR_BUFFER_BIT)
        glColor3f(1, 1, 1)
        glLineWidth(5)
        glBegin(GL_LINES)
        glVertex2f(self.x1, self.y1)
        glVertex2f(self.x2, self.y2)
        glEnd()

    def display(self):
        x = (self.start_point[0] * cos(radians(self.angle)) - self.start_point[1] * sin(radians(self.angle)))
        y = (self.start_point[0] * sin(radians(self.angle)) + self.start_point[1] * cos(radians(self.angle)))
        self.create_line()
        self.draw_car(x, y)
        glutSwapBuffers()

    def update(self, value):
        global OFFSET
        x = self.start_point[0]
        y = self.start_point[1]
        if self.to_right:
            OFFSET -= 0.05 * self.speed
            x += self.speed * cos(radians(-self.angle))
            y += self.speed * sin(radians(-self.angle))
        else:
            OFFSET += 0.05 * self.speed
            x -= self.speed * cos(radians(-self.angle))
            y -= self.speed * sin(radians(-self.angle))
        if x > WINDOW_SIZE - 60:
            self.to_right = False
        elif x < -WINDOW_SIZE:
            self.to_right = True
        self.start_point[0] = x
        self.start_point[1] = y
        glutPostRedisplay()
        glutTimerFunc(int(1000/60), self.update, 0)

    def controls(self, key, x, y):
        if key == b"d":
            self.to_right = True
        elif key == b"a":
            self.to_right = False
        elif key == b"w":
            self.speed += 1
        elif key == b"s":
            self.speed -= 1
            if self.speed < 0:
                self.speed = 0 
        elif key == b"h":
            playsound.playsound("./horn.mpeg", block=False)

def main():
    car = Car()
    print("Creating window...")
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
    glutInitWindowSize(1000, 1000)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("Car | Abhinav Rajesh")
    glutDisplayFunc(car.display)
    glutKeyboardFunc(car.controls)
    glutTimerFunc(0, car.update, 0)
    glutIdleFunc(car.display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()