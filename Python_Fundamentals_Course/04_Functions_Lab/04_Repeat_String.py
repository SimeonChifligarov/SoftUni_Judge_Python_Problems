# Write a function that receives a string and a repeat count n.
# The function should return a new string (the old one repeated n times).

def repetition_of_string(text, num_of_reps):
    return text * num_of_reps


string = input()
repetition = int(input())
print(repetition_of_string(string, repetition))
