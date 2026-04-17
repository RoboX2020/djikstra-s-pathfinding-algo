import numpy as np

def grid(n_rows:int, n_cols:int, num_obstacles:int, num_priorities:int):
    a = np.zeros((n_rows,n_cols))
    start_index = (np.random.randint(0, n_rows-1),np.random.randint(0, n_rows-1))

    end_index = start_index
    while end_index == start_index:
        end_index = (np.random.randint(0, n_rows-1),np.random.randint(0, n_rows-1))
    
    