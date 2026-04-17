import numpy as np

def grid(n_rows: int, n_cols: int, num_obstacles: int, num_priorities: int):
    """
    Generate a 2D grid with labeled cells for start, destination, obstacles, and priority points.

    The grid is initialized with '.' representing empty cells, and then populated with:
        'S' → Start position
        'D' → Destination position
        'X' → Obstacles
        'P' → Priority points

    Parameters
    ----------
    n_rows : int
        Number of rows in the grid.
    n_cols : int
        Number of columns in the grid.
    num_obstacles : int
        Number of obstacle cells ('X') to place in the grid.
    num_priorities : int
        Number of priority cells ('P') to place in the grid.

    Returns
    -------
    numpy.ndarray
        A 2D NumPy array of shape (n_rows, n_cols) containing characters:
        '.', 'S', 'D', 'X', and 'P'.

    Notes
    -----
    - Rows and columns are sampled independently using separate lists.
    - Once a row or column is used, it is removed from selection.
    - This means:
        • Each row and column is used at most once.
        • The grid will NOT use all possible cells uniformly.
        • This does NOT guarantee true random unique cell selection.
    - If (num_obstacles + num_priorities + 2) exceeds min(n_rows, n_cols),
      this function will raise an error due to exhausted indices.

    Example
    -------
    >>> grid(5, 5, 2, 1)
    array([
        ['.', '.', '.', '.', '.'],
        ['.', 'S', '.', '.', '.'],
        ['.', '.', 'X', '.', '.'],
        ['.', '.', '.', 'P', '.'],
        ['.', '.', '.', '.', 'D']
    ])
    """

    a = np.full((n_rows, n_cols), '.')
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