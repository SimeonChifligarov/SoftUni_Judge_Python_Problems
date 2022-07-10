def get_magic_triangle(n):
    initial_matrix = [[1], [1, 1]]
    for row in range(2, n):
        current_row = [1]
        for num in range(len(initial_matrix[row - 1]) - 1):
            current_row.append(initial_matrix[row - 1][num] + initial_matrix[row - 1][num + 1])
        current_row.append(1)
        initial_matrix.append(current_row)
    return initial_matrix
