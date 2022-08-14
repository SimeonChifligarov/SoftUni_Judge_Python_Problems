# •	The length should be 6 - 10 characters (inclusive)
# •	It should consist only letters and digits
# •	It should have at least 2 digits

def if_password_is_valid(p_word):
    is_valid = True
    is_length = True
    is_only_let_and_dig = True
    is_at_least_two_dig = True
    dig_count = 0
    if 6 <= len(p_word) <= 10:
        pass
    else:
        is_length = False
        is_valid = False
    if p_word.isalnum():
        pass
    else:
        is_only_let_and_dig = False
        is_valid = False
    for char in p_word:
        if char.isnumeric():
            dig_count += 1
    if dig_count >= 2:
        pass
    else:
        is_at_least_two_dig = False
        is_valid = False
    return [is_valid, is_length, is_only_let_and_dig, is_at_least_two_dig]


password = input()
result = if_password_is_valid(password)
is_valid = result[0]
is_length = result[1]
is_only_let_and_dig = result[2]
is_at_least_two_dig = result[3]

if is_valid:
    print("Password is valid")
else:
    if not is_length:
        print("Password must be between 6 and 10 characters")
    if not is_only_let_and_dig:
        print("Password must consist only of letters and digits")
    if not is_at_least_two_dig:
        print("Password must have at least 2 digits")
