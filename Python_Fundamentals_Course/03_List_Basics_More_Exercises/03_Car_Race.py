track_race = [int(el) for el in input().split()]
# print(track_race)
middle_index = int((len(track_race) - 1) / 2)
# print(middle_index)

left_car_track = track_race[:middle_index]
right_car_track = track_race[middle_index + 1:][::-1]
# print(left_car_track)
# print(right_car_track)

left_car_time = 0
for segment in left_car_track:
    if segment == 0:
        left_car_time *= 0.8
    else:
        left_car_time += segment

right_car_time = 0
for segment in right_car_track:
    if segment == 0:
        right_car_time *= 0.8
    else:
        right_car_time += segment

if left_car_time <= right_car_time:
    print(f'The winner is left with total time: {left_car_time:.1f}')
else:
    print(f'The winner is right with total time: {right_car_time:.1f}')
