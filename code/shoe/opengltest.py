#! usr/bin/env python

import sys
import pygame
import OpenGL.GL as gl
import OpenGL.GLU as glu
width, height = 1024, 768
def setupgl():
    global width, height
    gl.glViewport(0, 0, width, height)
    gl.glMatrixMode(gl.GL_PROJECTION)
    gl.glLoadIdentity()
    glu.gluPerspective(60., float(width)/height, 1., 10000.)
    gl.glMatrixMode(gl.GL_MODELVIEW)
    gl.glLoadIdentity()
    gl.glEnable(gl.GL_DEPTH_TEST)
    gl.glClearColor(1.0, 1.0, 1.0, 0.0)
    gl.glShadeModel(gl.GL_FLAT)
    gl.glEnable(gl.GL_COLOR_MATERIAL)
    gl.glEnable(gl.GL_LIGHTING)
    gl.glEnable(gl.GL_LIGHT0)
    gl.glLight(gl.GL_LIGHT0, gl.GL_POSITION, (0, 1, 1, 0))
    return

def main():
    pygame.init()
    screen = pygame.display.set_mode((width, height), pygame.HWSURFACE|pygame.DOUBLEBUF|pygame.OPENGL)
    clock = pygame.time.Clock()
    setupgl()
    while 1:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
        gl.glBegin(gl.GL_QUADS)
        gl.glColor(1.0, 0.0, 0.0)
        
        gl.glVertex(100.0, 100.0, 0.0)
        gl.glVertex(200.0, 100.0, 0.0)
        gl.glVertex(200.0, 200.0, 0.0)
        gl.glVertex(100.0, 200.0, 0.0)
        
        gl.glEnd()
        
        clock.tick(60)
        pygame.display.flip()
    print 'hi?'
    return

if __name__ == '__main__':
    main()
