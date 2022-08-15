words = input().split()
filtered_words = [w for w in words if len(w) % 2 == 0]

print(*filtered_words, sep='\n')
