# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Wilson's algorithm maze generator.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------



from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from generation.mazeGenerator import MazeGenerator
import random


class WilsonMazeGenerator(MazeGenerator):
    """
    Wilson algorithm maze generator.
    TODO: Complete the implementation (Task A)
    """

    def __init__(self):
        self.maze = None
        self.m_mazeGenerated = False

    def generateMaze(self, maze: Maze3D):
        # TODO: Implement this method for task A.

        print("Wilson's algorithm for generating...")
        self.maze = maze
        self.maze.initCells(True)  
        # to store the cells taht have been visited
        visited = set()  
          
        total_c = sum(maze.rowNum(l) * maze.colNum(l) for l in range(maze.levelNum()))

        # Randomly select a starting cell
        s_level = random.randint(0, maze.levelNum() - 1)
        s_cell = Coordinates3D(s_level,
                                   random.randint(0, maze.rowNum(s_level) - 1),
                                   random.randint(0, maze.colNum(s_level) - 1))
        visited.add(s_cell)

        while len(visited) < total_c:
            curr_c = random.choice(list(visited))  # Choose a random visited cell
            path = [curr_c]

            # perform a loop-erased random walk
            while True:
                # finding neighbours that are not visted yet
                neigh = [n for n in self.maze.neighbours(curr_c) if n not in visited]
                # break from the loop if there is no neighbours 
                if not neigh:
                    break
                # randomly choosing next cell
                next_c = random.choice(neigh)
                path.append(next_c)
                curr_c = next_c
                visited.add(curr_c)

            # carving the way by removing the wall in the length of the path
            for i in range(len(path) - 1):
                # in each iteration assigning cell and next cell
                cell, next_c = path[i], path[i + 1]
                self.maze.removeWall(cell, next_c)
                visited.add(next_c)  

        # Mark all boundary cells with walls
        bound = set(cell for cell in maze.allCells() if maze.isBoundary(cell))
        for cell in bound:
            for neighbor in maze.neighbours(cell):
                    # Add walls between boundary and its neigh
                    self.maze.addWall(cell, neighbor)

        self.m_mazeGenerated = True
        print("Maze generation completed with WILSON")

    def isMazeGenerated(self):
        return self.m_mazeGenerated
