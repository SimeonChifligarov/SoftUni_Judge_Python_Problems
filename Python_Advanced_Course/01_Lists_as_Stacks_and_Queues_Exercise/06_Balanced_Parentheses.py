OPENING_PARENTHESIS = ["(", "[", "{"]
CLOSING_PARENTHESIS = [")", "]", "}"]

parenthesis_mapper = {OPENING_PARENTHESIS[i]: CLOSING_PARENTHESIS[i] for i in range(len(OPENING_PARENTHESIS))}

sequence_of_parentheses = input()

stack_of_opening_parenthesis = []

is_balanced = "YES"

for symbol in sequence_of_parentheses:
    if symbol in OPENING_PARENTHESIS:
        stack_of_opening_parenthesis.append(symbol)
    elif symbol in CLOSING_PARENTHESIS:
        if not stack_of_opening_parenthesis:
            is_balanced = "NO"
            break
        if not symbol == parenthesis_mapper[stack_of_opening_parenthesis.pop()]:
            is_balanced = "NO"
            break

print(is_balanced)
