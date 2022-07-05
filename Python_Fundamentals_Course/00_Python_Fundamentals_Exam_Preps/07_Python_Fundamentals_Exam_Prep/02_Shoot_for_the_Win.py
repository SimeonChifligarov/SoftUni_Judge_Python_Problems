# •	On the first line of input you will receive a sequence of integers, separated by a single space – the targets sequence.
# •	On the next lines, until the "End" command you be receiving integers each on a single line – the index of the target to be shot.

target_sequence = [int(el) for el in input().split()]
shot_targets = 0

index_of_shoot = input()

while not index_of_shoot == "End":
    index_of_shoot = int(index_of_shoot)
    if index_of_shoot in range(len(target_sequence)) and not target_sequence[index_of_shoot] == -1:
        for index in range(len(target_sequence)):
            if index == index_of_shoot:
                continue
            if target_sequence[index] > target_sequence[index_of_shoot] and not target_sequence[index] == -1:
                target_sequence[index] -= target_sequence[index_of_shoot]
            elif target_sequence[index] <= target_sequence[index_of_shoot] and not target_sequence[index] == -1:
                target_sequence[index] += target_sequence[index_of_shoot]
        target_sequence[index_of_shoot] = -1
        shot_targets += 1

    index_of_shoot = input()

print(f'Shot targets: {shot_targets} -> ', end="")
print(*target_sequence, sep=" ")
