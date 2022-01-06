from random import randint

print("Start!")
goal = randint(1, 100)
repeat = True
t = 0

while repeat:
    t += 1
    print("Try:", t)
    answer = int(input("Enter a number between 1 and 100: "))
    if answer == goal:
        print("Yes!")
        print("You reached the goal!", "(Try: " + str(t) + ")")
        repeat = False
    elif answer < goal:
        print("No!")
        print("The goal is bigger!")
        print("Try again!")
    elif answer > goal:
        print("No!")
        print("The goal is smaller!")
        print("Try again!")
print("End!")
