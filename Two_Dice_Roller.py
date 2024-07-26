import random

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)


def dice_roll(dice1, dice2):
  print("Dice 1 = " + str(dice1))
  print("Dice 2 = " + str(dice2))
  result = dice1 + dice2
  return "Result: " + str(result)


print(dice_roll(dice1, dice2))