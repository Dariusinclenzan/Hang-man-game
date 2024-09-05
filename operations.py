class Guess:

    def __init__(self, chosen_word, blanks):
        self.goal = 0
        self.life = 6
        self.chosen_word = chosen_word
        self.blanks = blanks

    def guess_a_letter(self):
        print(self.blanks)
        guess_letter = input("Guess a letter: ")
        for index, letter in enumerate(self.chosen_word):
            if letter in guess_letter:
                self.blanks[index] = letter
                self.goal += 1
        if guess_letter not in self.chosen_word:
            self.life -= 1
            print(f"You got {self.life} tries left")

