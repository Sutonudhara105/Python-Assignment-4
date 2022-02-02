string = input("Enter a string: ")
last_char = string[-1]
string = string.replace(last_char, '*')
string = string[:-1] + last_char
print(string)
