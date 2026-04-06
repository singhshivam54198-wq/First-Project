import random

n = random.randint(1, 100)
guess = -1
guesses = 0

while (guess != n):
    guesses += 1
    guess = int(input("guess the number"))
    if (guess > n):
        print("lower number please")
    elif (guess < n):
        print("higher number please")
print(f"you have guessed the number correctly in {guesses}attempts")