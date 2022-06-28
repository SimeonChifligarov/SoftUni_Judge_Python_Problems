vowels_list = ['a', 'o', 'u', 'e', 'i']

received_text = input()
no_vowels_text = ''.join([ch for ch in received_text if ch.lower() not in vowels_list])

print(no_vowels_text)
