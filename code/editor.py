#! usr/bin/env python
# Maze editor for Pacman
import sys
import pygame
import constants as c
import pickle as pk
import os
import vector as v
empty = ''
wall = 'Wall'
dot = 'Dot'
energizer = 'Energizer'
ghost = 'Ghost'
pacman = 'Pacman'
class Editor(object):
    def __init__(self):
        global empty
        self.screen = pygame.display.set_mode((c.width, c.height))
        self.clock = pygame.time.Clock()
        self.grid = []
        self.prepareGrid()
        self.currentTool = empty
    def prepareGrid(self):
        global empty
        for row in range(0, c.gridHeight):
            self.grid.append([empty]*c.gridWidth)
        return
    def start(self):
        global empty, wall, dot, energizer
        going = 1
        while going:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    going = False
                elif e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        going = False
                    elif e.key == pygame.K_1:
                        self.currentTool = empty
                    elif e.key == pygame.K_2:
                        self.currentTool = wall
                    elif e.key ==  pygame.K_3:
                        self.currentTool = dot
                    elif e.key == pygame.K_4:
                        self.currentTool = energizer
                    elif e.key == pygame.K_5:
                        self.currentTool = ghost
                    elif e.key == pygame.K_6:
                        self.currentTool = pacman
                    elif e.key == pygame.K_s:
                        self.saveMap()
            if pygame.mouse.get_pressed()[0]:
                pos = pygame.mouse.get_pos()
                cell = pos[0]/c.cellSize, pos[1]/c.cellSize
                self.grid[cell[1]][cell[0]] = self.currentTool
            self.screen.fill((0, 0, 0))
            pos = [0, 0]
            for row in self.grid:
                for cell in row:
                    if cell == empty:
                        pygame.draw.rect(self.screen, (30, 30, 30), (pos, (c.cellSize, c.cellSize)))
                        pygame.draw.rect(self.screen, (0, 0, 0), (pos, (c.cellSize, c.cellSize)), 1)
                    elif cell == wall:
                        pygame.draw.rect(self.screen, (0, 0, 255), (pos, (c.cellSize, c.cellSize)))
                        pygame.draw.rect(self.screen, (0, 0, 0), (pos, (c.cellSize, c.cellSize)), 1)
                    elif cell == dot:
                        pygame.draw.rect(self.screen, (255, 255, 255), (pos, (c.cellSize, c.cellSize)))
                        pygame.draw.rect(self.screen, (0, 0, 0), (pos, (c.cellSize, c.cellSize)), 1)
                    if cell == energizer:
                        pygame.draw.rect(self.screen, (100, 100, 100), (pos, (c.cellSize, c.cellSize)))
                        pygame.draw.rect(self.screen, (0, 0, 0), (pos, (c.cellSize, c.cellSize)), 1)
                    pos[0] += c.cellSize
                pos[1] += c.cellSize
                pos[0] = 0
            #
            self.clock.tick(c.fps)
            pygame.display.flip()
        return
    def saveMap(self):
        mapFile = os.path.join(os.path.join(os.getcwd(), 'mazes'), raw_input('Enter a name for the map: '))
        mapFile = open(mapFile, 'w')
        pk.dump(self.grid, mapFile)
        mapFile.close()
        return
def main():
    pygame.init()
    editor = Editor()
    editor.start()
    pygame.quit()
    sys.exit()
if __name__ == '__main__':
    main()
