str2=input("Enter a string: ")
counts = dict()
words = str2.split()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1



print(counts)
