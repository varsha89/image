__author__ = 'Serge'


from Smatrix import *

import pygame

def DrawSamt(smat):   ## PUT MATRIX HERE AS INPUT !!!!
    pygame.init()
    screen = pygame.display.set_mode((smat.size, smat.size))
    for i in xrange(smat.size):
        for j in xrange(smat.size):
             pygame.draw.lines(screen, (smat.getCont()[i][j], smat.getCont()[i][j], smat.getCont()[i][j]), False, [(i, j), (i, j)], 1 )
    pygame.display.update()

