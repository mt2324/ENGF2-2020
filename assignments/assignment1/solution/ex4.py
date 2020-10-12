import random
print("Specify the number of iteration")
while True:
    num =input()
    try:
        num = int(num)
        break
    except ValueError:
        print("Type an integer")

inCircle = 0
for i in range (1, num):
    a = random.random()
    b = random.random()
    if (a**2 + b**2 <= 1):
        inCircle += 1
print("Approximate pi value for", num, "iteration is", inCircle*4/num)

    
