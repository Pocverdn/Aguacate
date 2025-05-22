import numpy as np

def parse_matrix(text):
    lines = [
        [float(num) for num in line.strip().split()]
        for line in text.strip().splitlines()
        if line.strip()
    ]

    if len(lines) == 1:
        return np.array(lines[0])  # Vector 1D
    else:
        return np.array(lines)     # Matriz 2D
