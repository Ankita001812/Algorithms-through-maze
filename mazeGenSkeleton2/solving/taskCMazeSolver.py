# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Task C solver.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------



from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D
from collections import deque

class TaskCMazeSolver(MazeSolver):
    """
    Task C solver implementation. You'll need to complete its implementation for task C.
    """

    def __init__(self):
        super().__init__()
        self.m_name = "taskC"
        self.dfs_path = []  # to keep track of the cells in dfs search
        self.bfs_path = []   # to keep track of the cells in dfs search
        self.visit_c_dfs = 0  # Counter for the number of cells visited by DFS
        self.visit_c_bfs = 0  # Counter for the number of cells visited by BFS
        self.dfs_back_count = 0

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D = None):
        # we call the the solve maze call without the entrance.
        # DO NOT CHANGE THIS METHOD
        self.solveMazeTaskC(maze)

    def solveMazeTaskC(self, maze: Maze3D):
        """       
        solve the maze, used by Task C.
        This version of solveMaze does not provide a starting entrance, and as part of the solution, the method should
        to find the entrance and exit pair (see project specs for requirements of this task).
        TODO: Please complete this implementation for task C.  You should call maze.solved(...) to update which entrance
        and exit you used for task C.

        @param maze: Instance of maze to solve.

        """
        entrances = set(maze.getEntrances())

        # definiting Deapth-first search

        def dfs(curr_c, prev_c):
            
            visited.add(curr_c)
            self.dfs_path.append(curr_c)
            
            self.visit_c_dfs += 1  # Increment the cell visit counter

            # Check if the current cell is an exit (boundary but not an entrance)
            if maze.isBoundary(curr_c) and curr_c not in entrances:
                self.solved(prev_c, curr_c)
                return True

            # Explore neighs
            for neigh in maze.neighbours(curr_c):
                if neigh not in visited and not maze.hasWall(curr_c, neigh):
                    if dfs(neigh, curr_c):
                        return True

            # backtrack if no unvisited neighs are found
            self.dfs_path.pop()
            self.dfs_back_count += 1
            #in dfs backtraking does get added in solver exploration cell count thats why counting to see the diff          
            return False
        
        #defining Breadth-first search

        def bfs(start_cell):

            # initializing a deque initialized with the starting cell and None as the previous cell
            queue = deque([(start_cell, None)])
            visited.add(start_cell)

            while queue:
                curr_c, prev_c = queue.popleft()
                self.bfs_path.append(curr_c)
                
                self.visit_c_bfs += 1  # Increment the cell visit counter

                # If current cell is an exit  but not an entrance
                if maze.isBoundary(curr_c) and curr_c not in entrances:
                    self.solved(prev_c, curr_c)
                    return True

                # Explore neighbours
                for neigh in maze.neighbours(curr_c):
                    if neigh not in visited and not maze.hasWall(curr_c, neigh):
                        visited.add(neigh)
                        queue.append((neigh, curr_c))

            return False

        # Run DFS
        visited = set()
        
        for entrance in entrances:
            if entrance not in visited and dfs(entrance, entrance):

                break

        dfs_v = self.visit_c_dfs
        print(f"Total number of cells visited by DFS (including backtracking): {dfs_v}")
        print(f"DFS backtracked {self.dfs_back_count} ")
        # Run BFS
        visited = set()
        
        for entrance in entrances:
            if entrance not in visited and bfs(entrance):
                break

        bfs_v = self.visit_c_bfs
        print(f"Total number of cells visited by BFS (including backtracking): {bfs_v}")

        # Compare and choose the better approach
        if bfs_v < dfs_v:
            print(f"BFS covered the SHORTEST path with {bfs_v} cells visited.")
            for i in self.bfs_path:
                self.solverPathAppend(i, False)
            self.solved(self.bfs_path[0], self.bfs_path[-1])
        else:
            print(f"DFS covered the SHORTEST path with {dfs_v} cells visited.")
            for i in self.dfs_path:
                self.solverPathAppend(i, False)
            self.solved(self.dfs_path[0], self.dfs_path[-1])








