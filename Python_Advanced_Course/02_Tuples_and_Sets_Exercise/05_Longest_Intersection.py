number_of_inputs = int(input())

all_intersections = []

for _ in range(number_of_inputs):
    first_set_attr, second_set_attr = input().split("-")

    first_set_start, first_set_end = [int(el) for el in first_set_attr.split(",")]
    second_set_start, second_set_end = [int(el) for el in second_set_attr.split(",")]

    first_set = set([num for num in range(first_set_start, first_set_end + 1)])
    second_set = set([num for num in range(second_set_start, second_set_end + 1)])

    current_intersection = first_set.intersection(second_set)

    all_intersections.append(current_intersection)

sorted_intersections = sorted(all_intersections, key=lambda x: -len(x))

longest_intersection = list(sorted_intersections[0])

print(
    f"Longest intersection is [{', '.join([str(el) for el in longest_intersection])}] with length {len(longest_intersection)}")
