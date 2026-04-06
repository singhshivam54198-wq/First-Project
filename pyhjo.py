import random

def gameWin(comp, you):
    # If it's a tie
    if comp == you:
        return None
    # Check all non-tie conditions
    elif comp == 's':  # Computer chose Snake
        if you == 'w':
            return False  # You lose (Water loses to Snake)
        elif you == 'g':
            return True   # You win (Gun beats Snake)
    elif comp == 'w':  # Computer chose Water
        if you == 'g':
            return False  # You lose (Gun loses to Water)
        elif you == 's':
            return True   # You win (Snake beats Water)
    elif comp == 'g':  # Computer chose Gun
        if you == 's':
            return False  # You lose (Snake loses to Gun)
        elif you == 'w':
            return True   # You win (Water beats Gun)

print("Welcome to Snake, Water, Gun!")
print("Computer's turn: Snake(s) Water(w) or Gun(g)?")

# Computer's choice
randNo = random.randint(1, 3)
if randNo == 1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

# Player's choice
you = input("Your Turn: Snake(s), Water(w), or Gun(g)? ").lower()

print(f"Computer chose {comp}")
print(f"You chose {you}")

a = gameWin(comp, you)

if a is None:
    print("The game is a tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")