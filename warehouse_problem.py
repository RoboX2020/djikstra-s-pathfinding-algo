import heapq
import numpy as np
from math import inf
import copy

'''
DIJKSTRA CLASS (teammate version)
'''
class DijkstraPathfinder:

    def __init__(self, grid):
        '''
        Initialize the pathfinder with the given grid.
        '''
        self.grid = np.array(grid)
        self.rows = len(grid)
        self.cols = len(grid[0]) if self.rows > 0 else 0

    def get_cost(self, cell):
        '''
        Return traversal cost of a cell.
        '''
        if cell == 'P':
            return 0.5
        if cell in ('S', 'D', '.'):
            return 1
        return inf

    def get_neighbors(self, row, col):
        '''
        Return valid neighboring cells (up, down, left, right).
        '''
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        neighbors = []

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < self.rows and 0 <= nc < self.cols:
                if self.grid[nr][nc] != 'X':
                    neighbors.append((nr, nc))

        return neighbors

    def dijkstra(self, start, destination):
        '''
        Compute shortest path using Dijkstra’s algorithm.
        Returns (cost, path).
        '''
        if self.rows == 0 or self.cols == 0:
            return float('inf'), []

        sr, sc = start
        dr, dc = destination

        if not (0 <= sr < self.rows and 0 <= sc < self.cols):
            return float('inf'), []
        if not (0 <= dr < self.rows and 0 <= dc < self.cols):
            return float('inf'), []

        if self.grid[sr][sc] == 'X' or self.grid[dr][dc] == 'X':
            return float('inf'), []

        dist = {(sr, sc): 0}
        parent = {(sr, sc): None}
        pq = [(0, sr, sc)]
        visited = set()

        while pq:
            current_cost, row, col = heapq.heappop(pq)

            if (row, col) in visited:
                continue
            visited.add((row, col))

            if (row, col) == (dr, dc):
                path = []
                node = (dr, dc)

                while node is not None:
                    path.append(node)
                    node = parent[node]

                path.reverse()
                return current_cost, path

            for nr, nc in self.get_neighbors(row, col):
                if (nr, nc) in visited:
                    continue

                step_cost = self.get_cost(self.grid[nr][nc])
                new_cost = current_cost + step_cost

                if new_cost < dist.get((nr, nc), inf):
                    dist[(nr, nc)] = new_cost
                    parent[(nr, nc)] = (row, col)
                    heapq.heappush(pq, (new_cost, nr, nc))

        return float('inf'), []


'''
HELPER FUNCTIONS
'''
def print_grid(grid):
    '''
    Print grid in readable format.
    '''
    for row in grid:
        print(" ".join(row))
    print()

def mark_path(grid, path):
    '''
    Mark path on grid using *.
    '''
    new_grid = copy.deepcopy(grid)
    for r, c in path:
        if new_grid[r][c] not in ('S', 'D'):
            new_grid[r][c] = '*'
    return new_grid


'''
DRIVER CODE
'''
my_map = [
    ['S', '.', '.', '.', '.'],
    ['X', 'X', '.', 'X', '.'],
    ['.', 'P', 'P', '.', '.'],
    ['.', 'X', '.', '.', 'D'],
    ['.', '.', '.', 'X', '.']
]

start_node = (0, 0)
dest_node = (3, 4)

print("Testing warehouse map...\n")

print("Original Grid:")
print_grid(my_map)

pf = DijkstraPathfinder(my_map)
cost, path = pf.dijkstra(start_node, dest_node)

print("Start:", start_node)
print("Destination:", dest_node)

if len(path) > 0:
    print("\nOptimal path coordinates:")
    print(path)
    print("Total cost =", cost)

    print("\nPath Grid:")
    print_grid(mark_path(my_map, path))
else:
    print("Couldn't find a path")

print("\n")