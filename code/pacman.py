#! usr/bin/env python
import sys
import pygame
import random
import os
import pickle as pk
from . import shoe as s
from . import constants as c
from . import objects as obs
from . import vector as v
from . import util as u

class GameScreen(object):
    def __init__(self, screen, clock, level):
        self.screen = screen
        self.clock = clock
        self.sprites = []
        self.prepareLevel(level)
        self.pacman = obs.Pacman(c.pacmanStart[0], c.pacmanStart[1])
        ghost = obs.Blinky(c.pacmanStart[0], c.pacmanStart[1])
        self.sprites.append(self.pacman)
        self.sprites.append(ghost)
        self.score = 0
    def update(self, time, events):
        self.events = events
        self.time = time
        for sprite in iter(self.sprites):
            sprite.update(self)
            sprite.draw(self)
        return
    def getCell(self, position):
        position = position.int_tuple
        sprites = []
        for sprite in self.sprites:
            if sprite.cellPos.int_tuple == position:
                sprites.append(sprite)
        return sprites
    def getNearbyCells(self, position):
        x, y = position
        allsprites = []
        allsprites.extend(self.getCell(x+1, y))
        allsprites.extend(self.getCell(x, y+1))
        allsprites.extend(self.getCell(x-1, y))
        allsprites.extend(self.getCell(x, y-1))
        return allsprites
    def checkForWalls(self, position):
        sprites = self.getCell(position)
        for s in sprites:
            if isinstance(s, obs.Wall):
                return True
        return False
    def prepareLevel(self, level):
        gridX = 0
        gridY = 0
        for row in level:
            for cell in row:
                if cell != '':
                    exec('ob = obs.'+cell+'(gridX*c.cellSize+c.cellSize/2, gridY*c.cellSize+c.cellSize/2)')
                    self.sprites.append(ob)
                gridX += 1
            gridY += 1
            gridX = 0
        return
    def remove(self, *args):
        self.sprites.remove(*args)
        return
    def add(self, *args):
        self.sprites.extend(*args)
        return
    def getPacman(self):
        return self.pacman
def main():
    pygame.init()
    screen = pygame.display.set_mode((c.width, c.height), pygame.HWSURFACE|pygame.DOUBLEBUF)
    clock = pygame.time.Clock()
    levelFile = open('./mazes/default.mze', 'r')
    level = pk.load(levelFile)
    levelFile.close()
    screens = [GameScreen(screen, clock, level)]
    time = 0
    going = 1
    while going:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                going = False
            elif e.type == pygame.KEYDOWN:
                if e.key == pygame.K_ESCAPE:
                    going = False
        screen.fill((0, 0, 0))
        time = clock.tick(c.fps)/1000.
        if len(screens) > 0:
            screens[-1].update(time, events)
        else:
            going = 0
        pygame.display.set_caption('fps: '+str(clock.get_fps()))
        pygame.display.flip()
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()
