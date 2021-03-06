#! usr/bin/env python
import pygame
from .vector import Vec2d

fps = 60
gridWidth = 28
gridHeight = 36
cellSize = 14
width, height = gridWidth*cellSize, gridHeight*cellSize
up = Vec2d(0, -1)
right = Vec2d(1, 0)
down = Vec2d(0, 1)
left = Vec2d(-1, 0)
pacmanStart = width/2, int(height-cellSize*9.5)
pacmanSpeed = 2
rightKey = pygame.K_RIGHT
downKey = pygame.K_DOWN
leftKey = pygame.K_LEFT
upKey = pygame.K_UP
dotSize = 3
energizerSize = 6
ghostSpeed = 4
