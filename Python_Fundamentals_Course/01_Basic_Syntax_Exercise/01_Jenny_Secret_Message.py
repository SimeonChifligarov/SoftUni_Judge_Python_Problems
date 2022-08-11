# Jenny studies programming with Python and wants to create a program that greets a user when he/she gives his/her name.
# Jenny however is in love with Johnny, and would like to greet him differently. Can you help her

name = input()

if not name == "Johnny":
    print(f'Hello, {name}!')
else:
    print('Hello, my love!')
