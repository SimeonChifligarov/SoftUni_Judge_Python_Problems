# You will receive a single integer number between 0 and 100 which is divided with 10
# without residue (0, 10, 20, 30...).
# Your task is to create a function that visualizes a loading bar depending on that number
# you have received in the input.

def loading_bar(num):
    num_dev_by_ten = num // 10
    loading_process = ['.'] * 10
    for index in range(num_dev_by_ten):
        loading_process[index] = "%"
    return "".join(loading_process)


number = int(input())
result = loading_bar(number)
if result.count("%") == 10:
    print("100% Complete!")
    print(f"[{result}]")
else:
    print(f"{number}% [{result}]")
    print("Still loading...")

# # Solution 2
# def loading_bar(num):
#     num_dev_by_ten = num // 10
#     loading_process = ['.'] * 10
#     for index in range(num_dev_by_ten):
#         loading_process[index] = "%"
#     if num_dev_by_ten == 10:
#         print('100% Complete!')
#         print(f'[{"".join(loading_process)}]')
#     else:
#         print(f'{num}% [{"".join(loading_process)}]')
#         print('Still loading...')
#
#
# number = int(input())
# loading_bar(number)
