import numpy as np

def grid(n_rows:int, n_cols:int, num_obstacles:int, num_priorities:int):
    a = np.full((n_rows,n_cols), '.')
    b = list(range(0, n_rows))
    c = list(range(0, n_cols))
    
    start_index = (np.random.choice(b), np.random.choice(c))
    
    b.remove(start_index[0])
    c.remove(start_index[1])

    end_index = (np.random.choice(b), np.random.choice(c))

    b.remove(end_index[0])
    c.remove(end_index[1])

    a[start_index[0], start_index[1]] = 'S'
    a[end_index[0], end_index[1]] = 'D'

    for i in range(num_obstacles):
        point = (np.random.choice(b), np.random.choice(c))

        b.remove(point[0])
        c.remove(point[1])

        a[point[0], point[1]] = 'X'

    for i in range(num_priorities):
        point = (np.random.choice(b), np.random.choice(c))

        b.remove(point[0])
        c.remove(point[1])

        a[point[0], point[1]] = 'P'

    return a

print(grid(10, 10, 2, 1))