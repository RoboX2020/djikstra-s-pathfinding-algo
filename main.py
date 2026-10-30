# ============================================================================
# main.py - the smallest possible demo of the pathfinder.
#
# WHAT THIS PROJECT IS: an implementation of Dijkstra's algorithm (a classic
# method for finding the cheapest route through a map) applied to a
# warehouse floor: a robot starts at 'S', wants to reach 'D', cannot cross
# shelves marked 'X', and prefers the faster conveyor lanes marked 'P'.
#
# THE FILES IN THIS REPO:
#   main.py                <- YOU ARE HERE. Builds one example map, runs the
#                             pathfinder once, prints the answer.
#   djikstra_pathfinding.py  the real pathfinder (the actual algorithm).
#   warehouse_problem.py     an older teammate version of the same algorithm,
#                             kept for reference, plus a demo that draws the
#                             found path on the map with '*' characters.
#   inp.py                   a helper that invents random maps for testing.
#
# RUN IT WITH:  python main.py
# ============================================================================

from djikstra_pathfinding import DijkstraPathfinder

# the map from the assignment document
my_map = [
    ['S', '.', '.', '.', '.'],
    ['X', 'X', '.', 'X', '.'],
    ['.', 'P', 'P', '.', '.'],
    ['.', 'X', '.', '.', 'D'],
    ['.', '.', '.', 'X', '.']
]

# S is at 0,0 and D is at 3,4
start_node = (0, 0)
dest_node = (3, 4)

print("testing warehouse map...")

# create the pathfinder obj
pf = DijkstraPathfinder(my_map)

# run dijkstra
cost, path = pf.dijkstra(start_node, dest_node)

print("start:", start_node)
print("destination:", dest_node)

# check if we actually found a path
if len(path) > 0:
    print("optimal path coordinates:")
    print(path)
    print("total cost = " + str(cost))
else:
    print("couldnt find a path")

# space for other tests if needed later
print("\n")