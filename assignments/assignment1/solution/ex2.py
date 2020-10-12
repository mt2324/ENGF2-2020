

print("Enter an integer")
a = input()
try:
    b = int(a)
    if b%2 ==0:
        print(b, "is even")
    else:
        print(b, "is odd")
    
except ValueError:
    print("It is not an integer")

