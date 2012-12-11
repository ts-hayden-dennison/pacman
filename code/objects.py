#! usr/bin/env python
import pygame
from . import constants as c
from .vector import Vec2d as vec
import random

class Pacman(object):
    def __init__(self, x, y):
        self.screenPos = vec(x, y)
        self.cellPos = vec(int(x/c.cellSize), int(y/c.cellSize))
        self.lastCellPos = vec(0, 0)
        self.dead = False
        self.currentDirection = c.left
        self.desiredDirection = c.left
        self.target = self.cellPos+self.currentDirection
        self.positions = []
    def update(self, game):
        self.updateKeyboardEvents(game)
        self.updateDirection(game)
        self.move(game)
        self.updateCollisions(game)
        return
    def updateCollisions(self, game):
        currentCell = game.getCell(self.cellPos)
        for s in currentCell:
            if isinstance(s, Dot):
                game.remove(s)
    def updateDirection(self, game):
        nextCell = self.cellPos+self.desiredDirection
        walls = game.checkForWalls(nextCell)
        if not walls:
            self.currentDirection = self.desiredDirection
        
        return
    def updateKeyboardEvents(self, game):
        for e in game.events:
            if e.type == pygame.KEYDOWN:
                if e.key == c.rightKey:
                    self.desiredDirection = c.right
                elif e.key == c.leftKey:
                    self.desiredDirection = c.left
                elif e.key == c.upKey:
                    self.desiredDirection = c.up
                elif e.key == c.downKey:
                    self.desiredDirection = c.down
        return
    def move(self, game):
        self.positions.append(self.screenPos.integerized())
        vec = self.target-self.screenPos
        vec = vec.normalized()
        self.screenPos += self.currentDirection*c.pacmanSpeed
        self.screenPos = self.screenPos.integerized()
        self.cellPos = self.screenPos.integerized()/c.cellSize
        return
    def draw(self, game):
        pygame.draw.circle(game.screen, (255, 255, 0), self.screenPos.int_tuple, c.cellSize/2)
        #pygame.draw.rect(game.screen, (255, 0, 255), ((self.cellPos*c.cellSize).int_tuple, (c.cellSize, c.cellSize)))
        #pygame.draw.circle(game.screen, (255, 0, 0), self.screenPos.int_tuple, 1)
        if len(self.positions) > 10:
            self.positions = self.positions[1:-1]
        if len(self.positions) > 2:
            for i in self.positions[1:]:
                pygame.draw.line(game.screen, (255, 0, 0), i, self.positions[self.positions.index(i)-1], 2)
        return

class Ghost(object):
    def __init__(self, x, y):
        self.screenPos = vec(x, y)
        self.cellPos = vec(int(x/c.cellSize), int(y/c.cellSize))
        self.dead = False
        self.target = vec(10, 10)
        self.direction = c.left
        self.speed = c.ghostSpeed
        self.nextDirection = c.left
    def update(self, game):
        self.findTarget(game)
        self.screenPos += self.direction*self.speed*game.time
        self.cellPos = (self.screenPos/c.cellSize).integerized()
        #pygame.draw.circle(game.screen, (255, 255, 255), self.target.int_tuple, 10)
        return
    def draw(self, game):
        pygame.draw.circle(game.screen, (255, 0, 0), self.screenPos.int_tuple, 3)
        return
    def findTarget(self, game):
        return

class Blinky(Ghost):
    def findTarget(self, game):
        '''# find the next cell we will encounter
        nextCell = self.cellPos+self.direction
        # find the three cells around it
        forward = nextCell+self.direction
        pygame.draw.circle(game.screen, (255, 255, 255), forward*c.cellSize+c.cellSize/2, 4)
        perpendicular = vec(self.direction.y, self.direction.x)
        right = nextCell+perpendicular
        left = nextCell+perpendicular*-1
        # assemble list of choices
        choices = [forward, right, left]
        # remove choices that lead to nowhere
        for choice in choices:
            if game.checkForWalls(choice):
                choices.remove(choice)
        print choices
        # find choice closest to target
        self.nextDirection = random.choice(choices)
        if (self.screenPos-(self.cellPos*c.cellSize+c.cellSize/2)).length < c.cellSize/2:
            self.direction = self.nextDirection'''
        return

class Dot(object):
    def __init__(self, x, y):
        self.cellPos = vec(int(x/c.cellSize), int(y/c.cellSize))
    def update(self, game):
        return
    def draw(self, game):
        screenCell = (self.cellPos[0]*c.cellSize+c.cellSize/2, self.cellPos[1]*c.cellSize+c.cellSize/2)
        pygame.draw.circle(game.screen, (255, 255, 255), screenCell, c.dotSize)
        return

class Energizer(Dot):
    def update(self, game):
        return
    def draw(self, game):
        screenCell = (self.cellPos[0]*c.cellSize+c.cellSize/2, self.cellPos[1]*c.cellSize+c.cellSize/2)
        pygame.draw.circle(game.screen, (100, 100, 100), screenCell, c.dotSize)
        return

class Wall(object):
    def __init__(self, x, y):
        self.cellPos = vec(int(x/c.cellSize), int(y/c.cellSize))
    def update(self, game):
        return
    def draw(self, game):
        screenCell = self.cellPos*c.cellSize
        
        pygame.draw.rect(game.screen, (0, 0, 255), (screenCell, (c.cellSize, c.cellSize)))
        return

'''def checkCellCollisions(self, cell, game):
        cellContents = game.getCell(cell)
        #pygame.draw.rect(game.screen, (255, 255, 255), (nextCell*c.cellSize, (c.cellSize, c.cellSize)))
        wall = False
        sprite = None
        for s in cellContents:
            if isinstance(sprite, Wall):
                wall = True
                sprite = s
        if wall:
            spriteCenter = sprite.cellPos*c.cellSize+c.cellSize/2
            pygame.draw.circle(game.screen, (255, 255, 255), spriteCenter.int_tuple, 3)
            newpos = self.screenPos
            pygame.draw.circle(game.screen, (255, 54, 255), newpos.int_tuple, 2)
            x, y = abs(self.screenPos.x-spriteCenter.x), abs(self.screenPos.y-spriteCenter.y)
            if x >= y:
                if newpos.x >= spriteCenter.x:
                    if newpos.x-spriteCenter.x < c.cellSize:
                        self.screenPos.x = self.cellPos.x*c.cellSize+c.cellSize/2
                elif newpos.x < spriteCenter.x:
                    if spriteCenter.x-newpos.x < c.cellSize:
                        self.screenPos.x = self.cellPos.x*c.cellSize+c.cellSize/2
            else:
                if newpos.y >= spriteCenter.y:
                    if newpos.y-spriteCenter.y < c.cellSize:
                        self.screenPos.y = self.cellPos.y*c.cellSize+c.cellSize/2
                elif newpos.y < spriteCenter.y:
                    if spriteCenter.y-newpos.y < c.cellSize:
                       self.screenPos.y = self.cellPos.y*c.cellSize+c.cellSize/2
        if wall:
            return True
        else:
            return False
        return'''
