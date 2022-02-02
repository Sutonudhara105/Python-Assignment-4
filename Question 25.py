
'''Write a program to get all substrings of a given string.'''

s = input("Enter a string: ")
substrings = []
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.append(s[i:j])
print(substrings)
