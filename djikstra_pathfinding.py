import heapq
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
    """

    def __init__(self,grid):
        """
        Initialize the pathfinder with a 2D warehouse grid.

        Args:
            grid (list[list[str]]): 2D grid representing the warehouse layout.
        """
        self.grid=grid
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
        """
        if cell=='P':
            return 0.5
        if cell in ('S','D','.'):
            return 1
        return inf

    def get_neighbors(self,row,col):
        """
        Get all valid non-obstacle neighbors in the four cardinal directions.

        Movement is allowed only up, down, left, and right.

        Args:
            row (int): Current row index.
            col (int): Current column index.

        Returns:
            list[tuple[int, int]]: List of reachable neighboring coordinates.
        """
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        neighbors=[]

        for dr, dc in directions:
            nr,nc=row+dr,col+dc

            # Check grid boundaries first
            if 0<=nr<self.rows and 0<=nc<self.cols:
                # Skip obstacle cells
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
        """
        # Handle empty grid
        if self.rows==0 or self.cols==0:
            return float('inf'),[]

        sr,sc=start
        dr,dc=destination

        # Validate start and destination coordinates
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

        # Track visited cells so we do not process the same cell twice
        visited=set()

        while pq:
            current_cost,row,col=heapq.heappop(pq)

            # Skip cells already finalized
            if (row,col) in visited:
                continue
            visited.add((row,col))

            # If destination is reached, reconstruct and return the path
            if (row,col)==(dr,dc):
                path=[]
                node=(dr, dc)

                while node is not None:
                    path.append(node)
                    node=parent[node]

                path.reverse()
                return current_cost,path

            # Explore each valid neighbor
            for nr, nc in self.get_neighbors(row,col):
                if (nr,nc) in visited:
                    continue

                # Cost to enter the neighboring cell
                step_cost=self.get_cost(self.grid[nr][nc])
                new_cost=current_cost+step_cost

                # Relaxation step: update if we found a cheaper path
                if new_cost<dist.get((nr,nc),inf):
                    dist[(nr,nc)]=new_cost
                    parent[(nr,nc)]=(row, col)
                    heapq.heappush(pq,(new_cost,nr,nc))

        # No path found
        return float('inf'),[]
