# Phase 1, Lesson 1: Linear Algebra Intuition, Build it, step 2.
# Matrix x vector from scratch, then a tiny "neural network layer".


def mat_vec(matrix, vector):
    # Each output number = one row of the matrix dotted with the vector.
    return [sum(m * v for m, v in zip(row, vector)) for row in matrix]


rotation_90 = [[0, -1],
               [1,  0]]
point = [3, 1]
print(f"rotate {point} by 90 degrees -> {mat_vec(rotation_90, point)}")

# A neural network layer: weights (2 rows x 3 columns) times a 3-number input.
weights = [[0.1, -0.2,  0.3],
           [0.4,  0.5, -0.1]]
x = [1.0, 0.5, -0.3]
out = mat_vec(weights, x)
print(f"input  has {len(x)} numbers: {x}")
print(f"output has {len(out)} numbers: {[round(v, 2) for v in out]}")
