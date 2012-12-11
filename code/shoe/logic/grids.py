#! usr/bin/env python
# some two dimensional array classes
class DictGrid():
    def __init__(self, widthortuple, height=None):
        self._grid = {}
        self.width = 0
        self.height = 0
        if height == None:
            self.width = widthortuple[0]
            self.height = widthortuple[1]
            for i in range(0, widthortuple[0]):
                self._grid[i] = [0]*widthortuple[1]
        else:
            self.width = widthortuple
            self.height = height
            for i in range(0, widthortuple):
                self._grid[i] = [0]*widthortuple
        self.wrap = True
    def __getitem__(self, *args):
        x, y = args[0]
        if self.wrap:
            if y >= self.height:
                y = y-self.height
            if y < 0:
                y = self.height-y
            if x >= self.width:
                x = x-self.width
            if x < 0:
                x = self.width+x
        return self._grid[x][y]
    def __setitem__(self, *args):
        x, y = args[0]
        item = args[1]
        if self.wrap:
            if y >= self.height:
                y = y-self.height
            if y < 0:
                y = self.height-y
            if x >= self.width:
                x = x-self.width
            if x < 0:
                x = self.width+x
        self._grid[x][y] = item
        return
    def __repr__(self):
        return self._grid.__repr__()
    def __len__(self):
        return self.width*self.height
    def __iter__(self):
        allitems = []
        for column in sorted(self._grid.keys()):
            allitems.extend(self._grid[column])
        return allitems.__iter__()

class Grid():
    def __init__(self, widthortuple, height=None):
        self._grid = []
        self.width = 0
        self.height = 0
        if height == None:
            self.width = widthortuple[0]
            self.height = widthortuple[1]
            for i in range(0, height):
                self._grid.append([0]*widthortuple[1])
        else:
            self.width = widthortuple
            self.height = height
            for i in range(0, height):
                self._grid.append([0]*widthortuple)
        self.wrap = True
    def __getitem__(self, *args):
        x, y = args[0]
        if self.wrap:
            if y >= self.height:
                y = y-self.height
            if y < 0:
                y = self.height+y
            if x >= self.width:
                x = x-self.width
            if x < 0:
                x = self.width+x
        else:
            if x >= self.width or y >= self.height:
                raise IndexError
        return self._grid[y][x]
    def __setitem__(self, *args):
        x, y = args[0]
        item = args[1]
        if self.wrap:
            if y >= self.height:
                y = y-self.height
            if y < 0:
                y = self.height-y
            if x >= self.width:
                x = x-self.width
            if x < 0:
                x = self.width+x
        else:
            if x >= self.width or y >= self.height:
                raise IndexError
        self._grid[y][x] = item
        return
    def __iter__(self):
        allitems = []
        for row in self._grid:
            allitems.extend(row)
        return iter(allitems)
    def __repr__(self):
        return self._grid.__repr__()
    def __len__(self):
        return self.width*self.height
    def rows(self):
        allrows = []
        for row in self._grid: allrows.append(row)
        return allrows
    def fill(self, function):
        for row in self.rows():
            for cell in row:
                row[row.index(cell)] = function()
        return
