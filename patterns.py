rows = int(input("enter the numbers of the rows:  "))
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i*2 -1), end="")
        j = j + 1
    i = i+1
    print()