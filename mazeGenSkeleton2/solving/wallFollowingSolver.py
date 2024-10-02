# # -------------------------------------------------------------------
# # PLEASE UPDATE THIS FILE.
# # Wall following maze solver.
# #
# # __author__ = 'Jeffrey Chan'
# # __copyright__ = 'Copyright 2024, RMIT University'
# # -------------------------------------------------------------------


from maze.maze3D import Maze3D
from solving.mazeSolver import MazeSolver
from maze.util import Coordinates3D


class WallFollowingMazeSolver(MazeSolver):
    """
    Wall following solver implementation. You'll need to complete its implementation for task B.
    """

    def __init__(self):
        super().__init__()
        self.m_name = "wall"
        self.path = []
        self.explored_cells = 0
        self.entrance = None
        self.exit = None

    def solveMaze(self, maze: Maze3D, entrance: Coordinates3D):
        # TODO: Implement this for task B!

        
        start_coord: Coordinates3D = entrance
        print("Solving maze...")
        
        current_cell: Coordinates3D = start_coord
        visited = set()
        self.entrance = entrance
        print("Starting at:", self.entrance)
        self.path.append(self.entrance)
        self.solverPathAppend(self.entrance, False)


        while current_cell not in maze.getExits():

            visited.add(current_cell)
            self.explored_cells += 1

            # all neighboring cells
            neighb = maze.neighbours(current_cell)

            # to exclude visited cells and cells with walls
            valid_nei = [neighbor for neighbor in neighb if neighbor not in visited and not maze.hasWall(
                current_cell, neighbor)]

            # finding the right-side neighbor according to the right-hand rule if it exists
            right_neighbor = None
            for nei in valid_nei:
                if nei.getCol() == current_cell.getCol() + 1:
                    right_neighbor = nei
                    break

            # finding anti-lock directioned cell as per wall follower which is the left-side neighbour if no right-side neighbour exists
            left_neighbor = None
            if not right_neighbor:
                for nei in valid_nei:
                    if nei.getCol() == current_cell.getCol() - 1:
                        left_neighbor = nei
                        break

            if right_neighbor:
                # move to the right-side neighbor
                current_cell = right_neighbor
                print("Moved to the right side:", current_cell)
                self.path.append(current_cell)
                self.solverPathAppend(current_cell, False)
            elif left_neighbor:
                # Move to the left-side neighbor
                current_cell = left_neighbor
                print("Moved to the left side:", current_cell)
                self.path.append(current_cell)
                self.solverPathAppend(current_cell, False)
            else:
                # if no right or left-side neighbor move up or down or forword
                if valid_nei:
                    current_cell = valid_nei[0]
                    print("Moved to:", current_cell)
                    self.path.append(current_cell)
                    self.solverPathAppend(current_cell, False)
                else:
                    # Backtrack if the current cell is visited and there are cells in the path
                    if current_cell in visited and len(self.path) > 0:
                        current_cell = self.path.pop()
                        print("Backtracked to:", current_cell)
                        continue
                    else:
                        # If all paths are explored, exit
                        print("No unexplored paths found.")
                        # break
            # Update path
            self.path.append(current_cell)

        self.exit = current_cell
        print("Maze solved with WALL FOLLOWER")

        if current_cell in maze.getExits():
            self.solved(entrance, current_cell)
