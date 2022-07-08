""" For testing purposes only -> IGNORE THIS FILE """

import os
#
# created_file = open('my_first_file.txt', 'w')
# created_file.write('I just created my first file!')


# file_path = 'my_first_file.txt'
# if os.path.exists(file_path):
#     os.remove(file_path)


try:
    os.remove('my_first_file.txt')
except FileNotFoundError:
    print("File already deleted!")
