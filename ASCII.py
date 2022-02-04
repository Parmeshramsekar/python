print("enter the string:", end="")
text = input()
textlength = len(text)
for char in text:
    ascii = ord(char)
    print(char , "\t" , ascii )