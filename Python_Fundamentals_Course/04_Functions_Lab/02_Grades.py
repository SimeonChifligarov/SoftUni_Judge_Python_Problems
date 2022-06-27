# Write a function that receives a grade between 2.00 and 6.00 and prints the corresponding grade in words
# •	2.00 – 2.99 - "Fail"
# •	3.00 – 3.49 - "Poor"
# •	3.50 – 4.49 - "Good"
# •	4.50 – 5.49 - "Very Good"
# •	5.50 – 6.00 - "Excellent"

def grade_to_words(grade):
    result = None
    if 2.00 <= grade <= 2.99:  # grade < 3
        result = "Fail"
    elif 3.00 <= grade <= 3.49:
        result = "Poor"
    elif 3.50 <= grade <= 4.49:
        result = "Good"
    elif 4.50 <= grade <= 5.49:
        result = "Very Good"
    elif 5.50 <= grade <= 6.00:
        result = "Excellent"
    return result


grade_data = float(input())
print(grade_to_words(grade_data))
