# -------------------------------------------------------------------
# PLEASE UPDATE THIS FILE.
# Pledge maze solver.
#
# __author__ = 'Jeffrey Chan'
# __copyright__ = 'Copyright 2024, RMIT University'
# -------------------------------------------------------------------


from maze.maze3D import Maze3D
from maze.util import Coordinates3D
from solving.mazeSolver import MazeSolver



class PledgeMazeSolver(MazeSolver):
    """
    Pledge solver implementation.  You'll need to complete its implementation for task B.
    """

    def __init__(self):
        super().__init__()
        self.m_name = "Pledge"
        self.path = []
        self.entrance = None
        self.exit = None

    @staticmethod
    def direction(from_coord: Coordinates3D, to_coord: Coordinates3D) -> str:

        if from_coord.getLevel() < to_coord.getLevel():
            return 'U'  # up
        elif from_coord.getLevel() > to_coord.getLevel():
            return 'D'  # down
        elif from_coord.getRow() < to_coord.getRow():
            return 'F'  # forward
        elif from_coord.getRow() > to_coord.getRow():
            return 'B'  # backward
        elif from_coord.getCol() < to_coord.getCol():
            return 'R'  # right
        elif from_coord.getCol() > to_coord.getCol():
            return 'L'  # left
        else:
            return 'X'  # same cell 

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        # TODO: Implement this for task B!
        
        curr_c = entrance
        print("Solving maze...")
        self.entrance = entrance
        print("Starting at:", self.entrance)
        # Keep track of visited cells and cells in the current path
        self.path.append(self.entrance)
        self.solverPathAppend(self.entrance, False)
        visited = set()

        # Initialize angle tracking
        total_angle = 0

        while curr_c not in maze.getExits():
            # Mark current cell as visited
            visited.add(curr_c)

            # Find all ning cells
            neighb = maze.neighbours(curr_c)

            # to exclude visited cells and cells with walls
            valid_neigh = [n for n in neighb
                           if n not in visited and not maze.hasWall(curr_c, n)]

            if valid_neigh:
                # choosing any direction as per pledge
                next_cell = valid_neigh[0]
                self.path.append(curr_c)
                self.solverPathAppend(curr_c, False)

                # Update angle if a turn is made
                direction = self.direction(curr_c, next_cell)
                if direction in ['L', 'R']:
                    total_angle += (-60 if direction == 'L' else 60)

                # check if completed a full rotation
                if total_angle == 0:
                    print("Completed rotation. Moving in initial direction.")
                    
                    total_angle = 0

                curr_c = next_cell
                print("Moving to:", curr_c)
            else:
                # If no valid neighb, backtrack
                if self.path:
                    curr_c = self.path.pop()
                    print("Backtracking to:", curr_c)
                else:
                    # If all paths are explored, exit
                    print("No solution found.")
                    return

        if curr_c in maze.getExits():
            self.solved(entrance, curr_c)

        self.exit = curr_c
        print("Maze solved with PLEDGE")
        print("Entrance:", self.entrance)
        print("Exit:", self.exit)
