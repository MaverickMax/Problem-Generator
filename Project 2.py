from numpy import random

g = 9.8
while g == 9.8:



    x = random.randint(20)
    y = random.randint(1,20)

    add = x + y
    sub = x - y
    mul = x * y
    div = x / y

    operations = [add,sub,mul,div]
    operator = ["+",'-','*','/']
    answer = random.randint(3)
    solution = operations[answer]

    print("Answer the following:", x , operator[answer], y)

    t = float(input())

    if t != solution:
        print("Incorrect! The solution is", solution)
    else: print("Correct!")
    a = str(input("Do you wish to try again? Y/N:", ))
    if a == "Y":
        print("Okay!")
    else:break
else:input("press enter to exit.")
input("press enter to exit.")