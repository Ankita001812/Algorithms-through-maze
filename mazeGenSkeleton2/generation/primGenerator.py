# -------------------------------------------------------------------
# DON'T CHANGE THIS FILE.
# Prim's maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------



from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator

from random import choice, randint
from collections import deque


class PrimMazeGenerator(MazeGenerator):
    """
    Prim's algorithm maze generator.
    TODO: Complete the implementation (Task A)
    """

    def __init__(self):
        super().__init__()
        self.maze = None
        self.m_mazeGenerated = False

    def generateMaze(self, maze: Maze3D):
        # TODO: Implement this method for task A.

        print("Prims algorithm is generating the maze...")
        self.maze = maze
        maze.initCells(True)
        # initializeing an empty set to store visited cells
        visited = set()
        # initializing an empty deque to store frontier edges 
        frontier = deque()

        # start with a random row and column for the starting cell
        s_level = randint(0, maze.levelNum() - 1)
        s_coord = Coordinates3D(s_level, randint(0, maze.rowNum(
            s_level) - 1), randint(0, maze.colNum(s_level) - 1))

        visited.add(s_coord)
        self.addNeighToFront(maze, s_coord, visited, frontier)

        total_c = sum(maze.rowNum(l) * maze.colNum(l) for l in range(maze.levelNum()))

        while len(visited) < total_c:
            if frontier:
                # randomly selecting an edge from the frontier
                curr_c, new_c = choice(list(frontier))
                # remove the selected edge from the frontier
                frontier.remove((curr_c, new_c))

                if new_c not in visited:
                    # removing the wall between the cells
                    maze.removeWall(curr_c, new_c)
                    visited.add(new_c)  # marking the new cell as visited

                    # adding neighbors of the new cell to the frontier
                    self.addNeighToFront(
                        maze, new_c, visited, frontier)
            else:
                break  # If there are no more edges in the frontier, exit the loop
        print("Maze generated using PRIMS")
        self.m_mazeGenerated = True

    def addNeighToFront(self, maze, cell, visited, frontier):
        # getting the neighbours of the given cell
        neighbours = self.maze.neighbours(cell)
        for neigh in neighbours:
            # checking if the row/col of neigh is less than the row/col number of the level of the maze that the neigh belongs to 
            if neigh not in visited and \
                    0 <= neigh.getRow() < self.maze.rowNum(neigh.getLevel()) and \
                    0 <= neigh.getCol() < self.maze.colNum(neigh.getLevel()):
                # Add the edge between cell and its neighbor to the frontier
                frontier.append((cell, neigh))
