# Matrix Layer Rotator
"""
You are given a 2D matrix of integers. Your task is to rotate
each concentric rectangular layer of the matrix counter-
clockwise a specified number of times. A layer is defined as
the set of elements forming a rectangle from the border of the
matrix towards the center. The outermost layer is layer 1, the
next one is layer 2, and so on.
For example, in a 4x4 matrix, the outermost layer consists of
the elements on the first and last rows and columns. Atter
removing the outermost layer, the remaining 2x2 matrix forms
the next layer.
You need to perform a specified number of counter-clockwise
rotations on each of these layers independently and print the
resulting matrix.
Input:
The first line contains three space-separated integers: M
(number of rows), N (number of columns), and R (the number
of rotations), where (2 ≤ M, N ≤ 100) and (1 ≤ R ≤
1,000,000,000).
The next M lines each contain N space-separated integers,
representing the matrix elements. Each element will be
between 1 and 100, inclusive.
Output:
Print the rotated matrix. The output should consist of M lines,
with each line containing N space-separated integers. Each
number should be followed by a space.
"""


def rotate_matrix():
    # --- Input Handling ---
    # No \n at the end, so the user types on the same line as the prompt
    m_n_r = input("Enter matrix dimensions (M N) and rotations (R): ")
    M, N, R = map(int, m_n_r.split())
    
    print("Enter matrix elements:")
    matrix = []
    for _ in range(M):
        row = list(map(int, input().split()))
        matrix.append(row)

    # Number of layers (rings) in the matrix
    num_layers = min(M, N) // 2

    # Process each layer independently
    for layer in range(num_layers):
        top = layer
        left = layer
        bottom = M - 1 - layer
        right = N - 1 - layer
        
        # 1. Extract the current layer's elements into a 1D list (Clockwise)
        elements = []
        for j in range(left, right + 1):
            elements.append(matrix[top][j])
        for i in range(top + 1, bottom + 1):
            elements.append(matrix[i][right])
        for j in range(right - 1, left - 1, -1):
            elements.append(matrix[bottom][j])
        for i in range(bottom - 1, top, -1):
            elements.append(matrix[i][left])
            
        # 2. Calculate effective rotations (using modulo)
        eff_rotations = R % len(elements)
        
        # 3. Rotate the 1D list counter-clockwise
        rotated_elements = elements[eff_rotations:] + elements[:eff_rotations]
        
        # 4. Put the rotated elements back into the matrix
        idx = 0
        for j in range(left, right + 1):
            matrix[top][j] = rotated_elements[idx]
            idx += 1
        for i in range(top + 1, bottom + 1):
            matrix[i][right] = rotated_elements[idx]
            idx += 1
        for j in range(right - 1, left - 1, -1):
            matrix[bottom][j] = rotated_elements[idx]
            idx += 1
        for i in range(bottom - 1, top, -1):
            matrix[i][left] = rotated_elements[idx]
            idx += 1

    # --- Output ---
    print("\nRotated Matrix:")
    for row in matrix:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    rotate_matrix()