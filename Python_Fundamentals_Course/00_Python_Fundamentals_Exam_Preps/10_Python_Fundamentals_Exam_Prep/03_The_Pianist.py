#

number_of_pieces = int(input())

all_pieces = {}

for _ in range(number_of_pieces):
    piece, composer, key = input().split("|")
    all_pieces[piece] = {'composer': composer, 'key': key}

command = input()

while not command == "Stop":
    split_command = command.split("|")
    real_command = split_command[0]
    if real_command == "Add":
        piece, composer, key = split_command[1:]
        if piece not in all_pieces:
            all_pieces[piece] = {'composer': composer, 'key': key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif real_command == "Remove":
        piece = split_command[1]
        if piece not in all_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            all_pieces.pop(piece)
            print(f"Successfully removed {piece}!")
    elif real_command == "ChangeKey":
        piece, new_key = split_command[1:]
        if piece not in all_pieces:
            print(f"Invalid operation! {piece} does not exist in the collection.")
        else:
            all_pieces[piece]['key'] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
    command = input()

# for curr_piece in sorted(all_pieces):
for curr_piece in all_pieces:
    print(f"{curr_piece} -> Composer: {all_pieces[curr_piece]['composer']}, Key: {all_pieces[curr_piece]['key']}")
