import numpy as np
from math import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame
def circlePoly(r,xc,yc,red,g,b):
    glBegin(GL_POLYGON)
    glColor3f(red, g, b)
    for i in np.arange(0, 0.5 * pi, 0.001):
        x = r * cos(i)
        y = r * sin(i)

        glVertex(xc + x, y + yc)
        glVertex(xc + x, yc - y)
        glVertex(xc - x, yc - y)
        glVertex(xc - x, yc + y)
    glEnd()

def circlePoints(r,xc,yc,red,g,b):
    glBegin(GL_POINTS)
    glColor3f(red, g, b)
    for i in np.arange(0, 0.5 * pi, 0.001):

        x = r * cos(i)
        y = r * sin(i)

        glVertex(xc+x, y+yc)
        glVertex(xc+x, yc-y)
        glVertex(xc-x, yc-y)
        glVertex(xc-x, yc+y)
    glEnd()

def FistStroke(sx):
    p0x = sx *2.5/12
    p0y = -1+(2/12)
    p1x = sx *1/12
    p1y = -1 +(1.25/12)
    p2x = sx *0
    p2y = -1+(2/12)
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0,0,0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()
    glBegin(GL_LINES)
    glColor(0, 0, 0)
    glVertex(p0x, p0y)
    glVertex(sx *2.8/12, -1+1.49/12)
    glEnd()
    circlePoints(0.5 / 12, sx *3.2 / 12, -1 + 1.9 / 12, 0, 0, 0)
    circlePoints(0.6 / 12, sx *3.7 / 12, -1 + 3 / 12, 0, 0, 0)
    circlePoints(0.65 / 12, sx *4 / 12, -1 + 4.5 / 12, 0, 0, 0)
    circlePoints(0.6 / 12, sx *3.7 / 12, -1 + 6 / 12, 0, 0, 0)
    #between fingers
    #1
    glBegin(GL_LINES)
    v1x=sx *2.8/12
    v1y=-1+2.5/12
    glColor(0, 0, 0)
    glVertex(v1x, v1y)
    glVertex(sx *3.2 / 12, -1 + 2.4 / 12)

    glVertex(v1x, v1y)
    glVertex(sx *3.5 / 12, -1 + 2.45 / 12)
    #2
    v2x = sx *3 / 12
    v2y = -1 + 3.8 / 12

    glVertex(v2x, v2y)
    glVertex(sx *4 / 12, -1 + 3.55 / 12)

    glVertex(v2x, v2y)
    glVertex(sx *4.2 / 12, -1 + 3.85 / 12)
    #3
    v3x = sx *2.8 / 12
    v3y = -1 + 5 / 12

    glVertex(v3x, v3y)
    glVertex(sx *3.75 / 12, -1 + 5.4 / 12)

    glVertex(v3x, v3y)
    glVertex(sx *4 / 12, -1 + 5.15 / 12)
    glEnd()

    #upper curve
    p0x = sx *2 / 12
    p0y = -1 + (6.5 / 12)
    p1x = sx *2.8 / 12
    p1y = -1 + (6.6 / 12)
    p2x = sx *3.45 / 12
    p2y = -1 + 6.5 / 12
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0, 0, 0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

    #mid curve
    p0x = sx *1.6 / 12
    p0y = -1 + (6.05 / 12)
    p1x = sx *1.4 / 12
    p1y = -1 + (5.3 / 12)
    p2x = sx *1 / 12
    p2y = -1 + 5.5 / 12
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0, 0, 0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

    # finger above
    p0x = sx *2 / 12
    p0y = -1 + (6.5 / 12)
    p1x = sx *1 / 12
    p1y = -1 + (8.5 / 12)
    p2x = sx *0
    p2y = -1 + 5 / 12
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0, 0, 0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

# inside finger above
    p0x = sx *2 / 12
    p0y = -1 + (6.5 / 12)
    p1x = sx *1.4 / 12
    p1y = -1 + (5.8 / 12)
    p2x = sx *1/12
    p2y = -1 + 6.35 / 12
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0, 0, 0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()


    #curves in middle of the fist
    p0x = sx *2 / 12
    p0y = -1 + (5.85 / 12)
    p1x = sx *2.6 / 12
    p1y = -1 + (4.3 / 12)
    p2x = sx *1.3 / 12
    p2y = -1 + 2.5 / 12
    glBegin(GL_POINTS)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        glColor(0, 0, 0)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def FistSolid(sx):    #looks the same but solid
    p0x = sx*2.5 / 12
    p0y = -1 + (2 / 12)
    p1x = sx*1 / 12
    p1y = -1 + (1.25 / 12)
    p2x = sx*0
    p2y = -1 + (2 / 12)
    glBegin(GL_POLYGON)
    glColor(1, 1, 1)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(p0x, p0y)
    glVertex(sx*(2.8 / 12), -1 + 1.49 / 12)

    # between fingers
    # 1

    glVertex(sx*(3.2 / 12), -1 + 2.4 / 12)


    glVertex(sx*(3.25 / 12), -1 + 2.5 / 12)

    # 2

    glVertex(sx*(4 / 12), -1 + 3.55 / 12)


    glVertex(sx*(4 / 12), -1 + 4 / 12)
    # 3

    glVertex(sx*(3.75 / 12), -1 + 5.4 / 12)

    # upper curve
    p0x = sx*2 / 12
    p0y = -1 + (6.5 / 12)
    p1x = sx*2.8 / 12
    p1y = -1 + (6.6 / 12)
    p2x = sx*3.45 / 12
    p2y = -1 + 6.5 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t

        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)

        # finger above
    p0x = sx*2 / 12
    p0y = -1 + (6.5 / 12)
    p1x = sx*1 / 12
    p1y = -1 + (8.5 / 12)
    p2x = sx*0
    p2y = -1 + 5 / 12
    glColor(0.7, 0.7, 0.7)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glColor(1,1,1)
    glVertex(sx*0, -1 + (2 / 12))
    glEnd()

    circlePoly( 0.5 / 12, sx *3.2 / 12, -1 + 1.9 / 12, 1, 1, 1)
    circlePoly(0.6 / 12,sx * 3.7 / 12, -1 + 3 / 12, 1, 1, 1)
    circlePoly( 0.65 / 12, sx *4 / 12, -1 + 4.5 / 12, 1, 1, 1)
    circlePoly( 0.6 / 12, sx *3.7 / 12, -1 + 6 / 12, 1, 1, 1)


def background():
    glColor3f(0, 0, 1)
    glBegin(GL_LINES)
    for i in np.arange(0, 90, 0.01):
        glColor(0.6 + i % 90 / 180, 0.6 + i % 90 / 180, 1)
        glVertex(0, 0)
        glVertex(2 * cos(i * pi / 180), 2 * sin(i * pi / 180))

        glVertex(0, 0)
        glVertex(-2 * cos(i * pi / 180), -2 * sin(i * pi / 180))

        glVertex(0, 0)
        glVertex(-2 * cos(i * pi / 180), 2 * sin(i * pi / 180))

        glVertex(0, 0)
        glVertex(2 * cos(i * pi / 180), -2 * sin(i * pi / 180))


    glEnd()

def rec(ox,oy,x,y,r,g,b):
    glBegin(GL_LINES)
    for i in np.arange(0, x, 0.001):
        pxi = ox + i
        nxi = ox - i
        c=i*3
        glColor(r - c, g - c, b - c)
        glVertex(pxi, oy)
        glVertex(pxi, oy+y)

        glColor(r - c, g - c, b - c)
        glVertex(nxi, oy)
        glVertex(nxi, oy+y)
    glColor(0,0, 0)   #making black stroke
    glVertex(pxi, oy)
    glVertex(pxi, oy + y)

    glVertex(nxi, oy)
    glVertex(nxi, oy + y)

    glVertex(nxi, oy)
    glVertex(pxi, oy)

    glVertex(nxi, oy + y)
    glVertex(pxi, oy + y)
    glEnd()

def eye(sx): #right eye is the default
    glBegin(GL_QUADS)
    glColor(1, 1, 1)
    glVertex(sx * 0.9/12, -1+11.1/12)
    glVertex(sx * 0.85/12, -1+11.3/12)
    glColor(0.4, 0.4, 0.4)
    glVertex(sx * 2.6/12, 0.5/12)
    glVertex(sx * 2.4/12, -1+11.5/12)

    glColor(0.8, 0.8, 1)
    glVertex(sx * 0.8/12, -1+11.2/12)
    glVertex(sx * 0.75/12, -1+11.4/12)
    glColor(0, 0, 1)
    glVertex(sx * 2.8/12, 1/12)
    glVertex(sx * 3/12, 0.8/12)
    glEnd()
    #stroke

    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0)
    glVertex(sx * 0.9 / 12, -1 + 11.1 / 12)
    glVertex(sx * 0.85 / 12, -1 + 11.3 / 12)
    glColor(0, 0, 0)
    glVertex(sx * 2.6 / 12, 0.5 / 12)
    glVertex(sx * 2.4 / 12, -1 + 11.5 / 12)
    glEnd()

    glBegin(GL_LINE_LOOP)
    glColor(0, 0, 0)
    glVertex(sx * 0.8 / 12, -1 + 11.2 / 12)
    glVertex(sx * 0.75 / 12, -1 + 11.4 / 12)
    glColor(0, 0, 0)
    glVertex(sx * 2.8 / 12, 1 / 12)
    glVertex(sx * 3 / 12, 0.8 / 12)

    glEnd()

def faceStroke(sx):
    p0x =sx* 0
    p0y = 2 / 12
    p1x =sx* 2.5/12
    p1y = 5 / 12
    p2x = sx*3.5/12
    p2y = 2 / 12
    glBegin(GL_POINTS)
    glColor(0,0,0)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()
    glBegin(GL_LINES)
    glVertex(x, y)
    glVertex(sx * 2.5 / 12, p2y)

    glVertex(sx * 2.5 / 12, p2y)
    glVertex(sx*3.5 / 12, p2y-(1/12))
    glEnd()
    p0x = 0
    p0y = -5.5 / 12
    p1x = sx*3 / 12
    p1y = -4.5 / 12
    p2x = sx*3.5 / 12
    p2y = 1 / 12
    glBegin(GL_POINTS)
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def faceSolid(sx):
    p0x =sx* 0
    p0y = 2 / 12
    p1x =sx* 2.5/12
    p1y = 5 / 12
    p2x = sx*3.5/12
    p2y = 2 / 12
    glBegin(GL_POLYGON)
    glColor(250/255, 220 / 255, 156 / 255)
    glVertex(p0x, p0y)

    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(sx*2.5/12, p2y)
    glVertex(sx*3.5 / 12, p2y-(1/12))
    p0x = 0
    p0y = -5.5 / 12
    p1x = sx*3 / 12
    p1y = -4.5 / 12
    p2x = sx*3.5 / 12
    p2y = 1 / 12

    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def mouthSolid(sx):
    # Lower mouth
    glBegin(GL_POLYGON)
    a = 1 / 12
    glColor(1, 1, 1)
    glVertex(0, -a - 2.38 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.38 / 12)

    p0x = sx * 0.5 / 12
    p0y = -a - 2.38 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.68 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 3.48 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(0, -a - 3.48 / 12)
    glEnd()

    # inside
    glBegin(GL_POLYGON)
    a = 1 / 12
    glColor(173 / 255, 1 / 255, 1 / 255)
    glVertex(0, -a - 2.2 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.2 / 12)

    p0x = sx * 0.5 / 12
    p0y = -a - 2.2 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.5 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 3.3 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(0, -a - 3.3 / 12)
    glEnd()

    #upper teeth
    glBegin(GL_POLYGON)
    a = 1 / 12
    glColor(1, 1, 1)
    glVertex(0, -a - 2.2 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.2 / 12)

    p0x = sx * 0.5 / 12
    p0y = -a - 2.2 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.35 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 2.5 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(0, -a - 2.5 / 12)
    glEnd()

def mouthStoke(sx):
    # Lower mouth
    glBegin(GL_POINTS)
    a = 1 / 12
    glColor(0, 0, 0)
    glVertex(0, -a - 2.38 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.38 / 12)

    p0x = sx * 0.5 / 12
    p0y = -a - 2.38 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.68 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 3.48 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()
    glBegin(GL_LINES)
    glVertex(x, y)
    glVertex(0, -a - 3.48 / 12)
    glEnd()

    # inside
    glBegin(GL_POINTS)
    a = 1 / 12
    glColor(0, 0, 0)
    glVertex(0, -a - 2.2 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.2 / 12)

    p0x = sx * 0.5 / 12
    p0y = -a - 2.2 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.5 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 3.3 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(0, -a - 3.3 / 12)
    glEnd()
    glBegin(GL_LINES)
    glVertex(x, y)
    glVertex(0, -a - 3.48 / 12)
    glEnd()

    #upper teeth

    a = 1 / 12
    glColor(0, 0, 0)
    glBegin(GL_LINES)
    glVertex(0, -a - 2.2 / 12)
    glVertex(sx * 0.5 / 12, -a - 2.2 / 12)
    glEnd()
    glBegin(GL_POINTS)
    p0x = sx * 0.5 / 12
    p0y = -a - 2.2 / 12
    p1x = sx * 1 / 12
    p1y = -a - 2.35 / 12
    p2x = sx * 0.5 / 12
    p2y = -a - 2.5 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glVertex(0, -a - 2.5 / 12)
    glEnd()


def bluebodySolid(sx):

    glBegin(GL_POLYGON)
    glColor(0,0,1)
    p0x = 0
    p0y = 1.5/ 12
    p1x = sx* 13 / 12
    p1y = - 4.5/ 12
    p2x = -sx*1/12
    p2y = -11.5/ 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        factor = mt * 0.3
        glColor((58 / 255) - factor, (125 / 255) - factor, (228 / 255) - factor)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def bluebodyStoke(sx):

    glBegin(GL_POINTS)
    glColor(0,0,0)
    p0x = 0
    p0y = 1.5/ 12
    p1x = sx* 13 / 12
    p1y = - 4.5/ 12
    p2x = -sx*1/12
    p2y = -11.5 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def yellowbodysolid(sx):
    glBegin(GL_QUADS)
    glColor(252 / 255, 1, 186 / 255)
    glVertex(sx * 2 / 12, -6 / 12)
    glVertex(sx * 3.5 / 12, -0.5 / 12)
    glVertex(sx * 2.5 / 12, 0.5 / 12)
    glVertex(0 / 12, -5 / 12)
    glEnd()
def yellowbodystroke(sx):
    glBegin(GL_LINES)
    glColor(0, 0, 0)
    glVertex(sx * 2 / 12, -6 / 12)
    glVertex(sx * 3.5 / 12, -0.5 / 12)

    glVertex(sx * 2.5 / 12, 0.5 / 12)
    glVertex(0 / 12, -5 / 12)
    glEnd()

def fireball(r,xc,yc):                                               #fireball
    glColor3f(0, 0, 1)
    glBegin(GL_POLYGON)

    for i in np.arange(0, 0.5 * pi, 0.01):
        glColor3f(0.5-i, i, 1-i)
        x = r * cos(i)
        y = r * sin(i)

        glVertex(xc+x, y+yc)
        glVertex(xc+x, yc-y)
        glVertex(xc-x, yc-y)
        glVertex(xc-x, yc+y)

def makehair():

    glTranslatef(0,0.09,0)
    #3
    l = 0.9
    for i in range(3):
        glRotatef((i+1)  * 22.5, 0, 0, 1)
        hair(0, 0, 0.1, l)
        glRotatef(-2*(i+1) * 22.5, 0, 0, 1)
        hair(0, 0, 0.1, l)
        glRotatef((i+1)  * 22.5, 0, 0, 1)
    hair(0, 0, 0.1, l)

    #2
    l = 0.8
    for i in range(3):
        glRotatef((i + 1) * 11.25, 0, 0, 1)
        hair(0, 0, 0.1, l)
        glRotatef(-2 * (i + 1) * 11.25, 0, 0, 1)
        hair(0, 0, 0.1, l)
        glRotatef((i+ 1) * 11.25, 0, 0, 1)
    #hair(0, 0, 0.1, l)

    #1

    for i in range(4):
        glRotatef((i+1)  * 22.5, 0, 0, 1)
        hair(0, 0, 0.1, 0.7)
        glRotatef(-2*(i+1) * 22.5, 0, 0, 1)
        hair(0, 0, 0.1, 0.7)
        glRotatef((i+1)  * 22.5, 0, 0, 1)
    hair(0, 0, 0.1, 0.7)
    glTranslatef(0, -0.09, 0)

def glovesSolid(sx):

    glBegin(GL_POLYGON)
    glColor(1,1,1)
    p0x = sx*3/12
    p0y = -5.5/ 12
    p1x = sx* 10 / 12
    p1y = - 8.5/ 12
    p2x = -sx * 3.5 / 12
    p2y = -10/ 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        factor = mt * 0.3
        glColor(1 - factor, 1 - factor, 1 - factor)
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def glovesStoke(sx):

    glBegin(GL_POINTS)
    glColor(0,0,0)
    p0x = sx * 3 / 12
    p0y = -5.5 / 12
    p1x = sx * 10 / 12
    p1y = - 8.5 / 12
    p2x = -sx * 3.5 / 12
    p2y = -10 / 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()


def nose():
    glBegin(GL_POINTS)
    glColor(0,0,0)
    p0x = 0
    p0y = -1.5/ 12
    p1x = - 1 / 12
    p1y = - 2.35 / 12
    p2x = 0
    p2y = -2.5/ 12
    for t in np.arange(0, 1, 0.001):
        mt = 1 - t
        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))  # quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))
        glVertex(x, y)
    glEnd()

def hair(ox,oy,w,h):
    p0x =w
    p0y=oy
    p1x=w*0.8
    p1y=h*0.6
    p2x=ox
    p2y=h

    for t in np.arange(0, 1, 0.001):
        mt=1-t

        x = (p0x * (mt ** 2)) + (2 * mt * t * p1x) + (p2x * (t ** 2))   #quadratic bezier curve
        y = (p0y * (mt ** 2)) + (2 * mt * t * p1y) + (p2y * (t ** 2))

        factor=mt * 0.3
        glBegin(GL_LINES)
        glColor((58 / 255) - factor, (125 / 255) - factor, (228 / 255) - factor)
        glVertex(x, y)
        glVertex(ox, oy)

        glColor((98 / 255) - factor, (216 / 255) - factor, (252 / 255) - factor)
        glVertex(-x, y)
        glVertex(ox, oy)
        glEnd()

        glBegin(GL_POINTS) #making stroke
        glColor(0,0,0)
        zz=0.003
        glVertex(x+zz, y)
        glVertex(-x-zz, y)
        glEnd()

    glBegin(GL_LINES) #still making stroke
    glColor(0, 0, 0)
    glVertex(w+zz, oy-zz)
    glVertex(-w-zz,oy-zz)
    glEnd()


def draw():

    glClearColor(0,0.5,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0,1,1)
    glLineWidth(1)
    background()

    bluebodySolid(1)
    bluebodySolid(-1)
    bluebodyStoke(1)
    bluebodyStoke(-1)

    yellowbodysolid(1)
    yellowbodysolid(-1)
    yellowbodystroke(1)
    yellowbodystroke(-1)

    makehair()
    rec(0,-1,2.8/12,2/12,1,1,1)
    rec(0, -1, 1.5 / 12, 0.5 / 12, 252/255, 1, 186/255)
    rec(0, -1+(1 / 12), 1.5 / 12, 0.5 / 12, 252 / 255, 1, 186 / 255)
    rec(0, -1 + (1.5 / 12), 1.5 / 12, 0.5 / 12, 252 / 255, 1, 186 / 255)
    rec(0, -1 + (0.5 / 12), 1.5 / 12, 0.5 / 12, 252 / 255, 1, 186 / 255)

    faceSolid(1)
    faceSolid(-1)
    faceStroke(1)
    faceStroke(-1)
    eye(1)
    eye(-1)
    mouthSolid(1)
    mouthSolid(-1)
    mouthStoke(1)
    mouthStoke(-1)
    nose()

    glovesSolid(1)
    glovesSolid(-1)
    glovesStoke(1)
    glovesStoke(-1)

    FistSolid(-1)
    FistStroke(-1)
    FistSolid(1)
    FistStroke(1)
    #fireball(0.3, -0.6, -0.6)
    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(650, 650)
glutCreateWindow(b"vegeta")
glutDisplayFunc(draw)
glutMainLoop()