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