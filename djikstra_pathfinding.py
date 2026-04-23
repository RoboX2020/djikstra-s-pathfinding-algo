import heapq
import numpy as np
from math import inf


class DijkstraPathfinder:
    """
    Finds the minimum-cost path through a warehouse grid using Dijkstra's algorithm.

    Grid cell meanings:
        'S' -> start cell
        'D' -> destination cell
        '.' -> normal traversable cell with cost 1
        'P' -> priority pathway cell with lower cost 0.5
        'X' -> obstacle cell that cannot be traversed

    Design note:
        This implementation models the warehouse as a graph where each cell is a node
        and edges connect adjacent cells (up, down, left, right). Dijkstra's algorithm
        is used because all edge weights are non-negative.
    """

    def __init__(self,grid):
        """
        Initialize the pathfinder with a 2D warehouse grid.

        Args:
            grid (list[list[str]]): 2D grid representing the warehouse layout.
        """
        # Store the grid and precompute dimensions for boundary checks
        self.grid=np.array(grid)
        self.rows=len(grid)
        self.cols=len(grid[0]) if self.rows>0 else 0

    def get_cost(self,cell):
        """
        Return the traversal cost for entering a given cell.

        Args:
            cell (str): A single grid character.

        Returns:
            float: The movement cost for that cell.
                   Returns inf for obstacles or invalid cells.

        Design note:
            Cost is based on ENTERING a cell (not leaving the current one),
            which is standard in grid-based pathfinding.
        """
        if cell=='P':
            return 0.5  # Priority paths are cheaper to encourage their use
        if cell in ('S','D','.'):
            return 1  # Normal traversal cost
        return inf  # Obstacles or invalid cells are effectively unreachable

    def get_neighbors(self,row,col):
        """
        Get all valid non-obstacle neighbors in the four cardinal directions.

        Movement is allowed only up, down, left, and right.

        Args:
            row (int): Current row index.
            col (int): Current column index.

        Returns:
            list[tuple[int, int]]: List of reachable neighboring coordinates.

        Design note:
            Diagonal movement is intentionally excluded to match problem constraints.
        """
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        neighbors=[]

        for dr, dc in directions:
            nr,nc=row+dr,col+dc

            # Check grid boundaries first to avoid index errors
            if 0<=nr<self.rows and 0<=nc<self.cols:
                # Skip obstacle cells since they are not traversable
                if self.grid[nr][nc]!='X':
                    neighbors.append((nr,nc))

        return neighbors

    def dijkstra(self,start,destination):
        """
        Compute the minimum-cost path from start to destination using Dijkstra's algorithm.

        The algorithm expands the cheapest reachable cell first and keeps track
        of the best known cost to each cell. It reconstructs the path once the
        destination is reached.

        Args:
            start (tuple[int, int]): (row, col) for the start cell.
            destination (tuple[int, int]): (row, col) for the destination cell.

        Returns:
            tuple[float, list[tuple[int, int]]]:
                - total_cost: minimum travel cost to reach the destination
                - path: list of coordinates from start to destination

            If no valid path exists, returns:
                (float('inf'), [])

        Design note:
            A priority queue (min-heap) is used to always expand the lowest-cost node first,
            which is the key idea behind Dijkstra's algorithm.
        """
        # Handle empty grid edge case
        if self.rows==0 or self.cols==0:
            return float('inf'),[]

        sr,sc=start
        dr,dc=destination

        # Validate start and destination coordinates are within bounds
        if not (0<=sr<self.rows and 0<=sc<self.cols):
            return float('inf'),[]
        if not (0<=dr<self.rows and 0<=dc<self.cols):
            return float('inf'),[]

        # Start or destination cannot be obstacles
        if self.grid[sr][sc]=='X' or self.grid[dr][dc]=='X':
            return float('inf'),[]

        # dist stores the best known cost to each cell
        dist={(sr, sc):0}

        # parent stores how we reached each cell, used later to rebuild the path
        parent={(sr, sc):None}

        # Priority queue stores (current_cost, row, col)
        pq=[(0,sr,sc)]

        # Track visited cells so we do not process the same cell multiple times
        # This ensures efficiency and correctness once the shortest path is finalized
        visited=set()

        while pq:
            current_cost,row,col=heapq.heappop(pq)

            # Skip cells already finalized (their shortest path is already known)
            if (row,col) in visited:
                continue
            visited.add((row,col))

            # If destination is reached, reconstruct and return the path
            if (row,col)==(dr,dc):
                path=[]
                node=(dr, dc)

                # Reconstruct path by backtracking from destination using parent pointers
                while node is not None:
                    path.append(node)
                    node=parent[node]

                path.reverse()  # Reverse to get path from start to destination
                return current_cost,path

            # Explore each valid neighbor
            for nr, nc in self.get_neighbors(row,col):
                if (nr,nc) in visited:
                    continue

                # Cost to enter the neighboring cell
                step_cost=self.get_cost(self.grid[nr][nc])
                new_cost=current_cost+step_cost

                # Relaxation step: update if we found a cheaper path
                # This is the core of Dijkstra's algorithm
                if new_cost<dist.get((nr,nc),inf):
                    dist[(nr,nc)]=new_cost
                    parent[(nr,nc)]=(row, col)
                    heapq.heappush(pq,(new_cost,nr,nc))

        # If we exit the loop, no path was found to the destination
        return float('inf'),[]
