from random import randint

print("Start!")
goal = randint(1, 100)
repeat = True
t = 0

while repeat:
    t += 1
    print("\n")
    print("-------------------------------------------------")
    print("Trial #" + str(t))
    answer = int(input("Enter a number between 1 and 100: "))
    if answer == goal:
        print("\n")
        print("Yes!!")
        print("You reached the goal!", "(# of trials : " + str(t) + ")")
        repeat = False
    elif answer < goal:
        print("\n")
        print("Unfortunately the goal is bigger ):")
        print("Try again!")
    elif answer > goal:
        print("\n")
        print("Unfortunately the goal is smaller ):")
        print("Try again!")
print("The End!")
