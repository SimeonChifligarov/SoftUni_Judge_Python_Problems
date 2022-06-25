current_year = int(input())

next_year = current_year + 1
while True:
    next_year_as_list = list(str(next_year))
    if len(set(next_year_as_list)) == len(next_year_as_list):
        print(next_year)
        break

    next_year += 1
