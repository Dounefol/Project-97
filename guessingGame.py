from curses import can_change_color
import random
x = random.randint(1,9)
print(x)

while chances < 5:

if guess == number:
    print("Congratulation YOU WON!!!")
    break

if not chances < 5: 
    print("YOU LOSE!!! The number 1s", number)