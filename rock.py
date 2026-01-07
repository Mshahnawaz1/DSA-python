# rock paper scissor

import random

data = {
    1: 'rock',
    2: 'paper',
    3: 'scissor'
}

win = [(1,3), (2,1), (3,2)]
draw = [(1,1), (2,2), (3,3)]

bot1 = random.randint(1,3)
# bot2 = random.randint(1,3)

print("1- rock, 2- paper, 3- scissor")
bot2 = int(input("Pick your choice(1-3): "))
if not bot2 in [1,2,3]:
    print("Enter valid input(1-3)")

print(f'Bot picked {data[bot1]}')
print(f'User picked {data[bot2]}')
print("=" * 60)
state = (bot1,bot2)
if state in win:
    print("bot1 is winner")
elif state in draw:
    print("Draw")
else:
    print("bot2 is winner")