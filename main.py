from data import word_list
import random
from operations import Guess
blanks = []
word = random.choice(word_list)
start = Guess(word, blanks)


for letter in range(len(word)):
    blanks.append("_")

game_on = True
while game_on:
    start.guess_a_letter()
    if start.goal == len(word):
        print(f"You won! The word was {word}")
        game_on = False
    elif start.life == 0:
        print(f"You lost! The word was {word}")
        game_on = False








