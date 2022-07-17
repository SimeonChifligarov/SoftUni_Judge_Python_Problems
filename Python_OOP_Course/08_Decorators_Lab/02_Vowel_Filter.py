def vowel_filter(function):
    def wrapper():
        vowels = ['a', 'e', 'i', 'o', 'u']
        res = function()
        filtered = [x for x in res if x.lower() in vowels]
        return filtered

    return wrapper

# @vowel_filter
# def get_letters():
#     return ["a", "b", "c", "d", "e"]
#
#
# print(get_letters())
