with open('text') as file:
    lines = [line.strip() for line in file.readlines()]

output = []
for index, line in enumerate(lines):

    letter_count = sum([len(word) for word in line.split()])
    punctuation_marks_count = (sum([1 for word in line.split() for letter in word if letter in r"[\?,\!\.-]"]))

    output.append(f'Line {index+1}: {line} ({letter_count - punctuation_marks_count})({punctuation_marks_count})\n')

with open('output.txt', 'a') as out_file:
    out_file.writelines(output)
