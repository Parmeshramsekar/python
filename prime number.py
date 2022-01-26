num = 407
num = int(input("enter the number:"))

if num > 1 :
    for i in range(2 , num) :
        if(num%i)==0:
            print(num,"is not prime num")
            print(i,"times", num//i "is",num)
            break
        else:
            print(num,"is a prime num")
    else:
        print(num,"is not a prime num")