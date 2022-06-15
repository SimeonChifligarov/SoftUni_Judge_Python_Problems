size_of_square_matrix = int(input())

matrix = []

for _ in range(size_of_square_matrix):
    row = list(input())
    matrix.append(row)

searched_symbol = input()

searched_symbol_positions = []

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] == searched_symbol:
            current_symbol_position = (i, j)
            searched_symbol_positions.append(current_symbol_position)

if searched_symbol_positions:
    print(searched_symbol_positions[0])
else:
    print(f"{searched_symbol} does not occur in the matrix")
