import random

num = random.randint(1, 30)
guess = int(input("Type your #: "))

tries = 5
i = 1

while i < tries:
    if guess == num:
        print("Great!")
        break
    elif guess < num:
        print("Too Low")
    else:
        print("Too High")
    guess = int(input("Type your # again: "))
    if guess == num and i == tries: print("Great!")
    i = i + 1

print(f"THe number was {num}")
