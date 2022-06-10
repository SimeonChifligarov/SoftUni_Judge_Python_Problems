OPENING_PARENTHESIS_SYMBOL = "("
CLOSING_PARENTHESIS_SYMBOL = ")"

math_expr = input()
opening_parentheses_indexes = []

for i in range(len(math_expr)):
    if math_expr[i] == OPENING_PARENTHESIS_SYMBOL:
        opening_parentheses_indexes.append(i)
    elif math_expr[i] == CLOSING_PARENTHESIS_SYMBOL:
        start_index = opening_parentheses_indexes.pop()
        print(math_expr[start_index:i + 1])
