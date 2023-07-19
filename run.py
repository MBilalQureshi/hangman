from random import randrange
from datetime import datetime
import time


class game:
    def __init__(self, game_name, user_name, no_of_stages, total_win, total_loose):
        self.game_name = game_name
        self.user_name = user_name
        self.no_of_stages = no_of_stages
        self.total_win = total_win
        self.total_loose = total_loose

    def details(self):
        now = datetime.now()
        return f"Game name is {self.game_name}, Game stages are {self.no_of_stages}, Username is {self.user_name}, data and time is:{now.strftime('%d/%m/%Y %H:%M:%S')}, total won{self.total_win}, total loose{self.total_loose}"

class hangman(game):
    words = ["apple", "banana", "owl", "controller", "helipad", "semiconductor"]

    def __init__(self, user_name, no_of_stages):
        game.__init__(self, "Hang Man", user_name, no_of_stages, 0, 0)


    def show_secret_word(self, secret_word, stage_number):
        hangman_pics = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
        word_length = len(secret_word)
        update_chars = ''

        for x in range(word_length):
            update_chars += '_'
        deaths = 0
        print(hangman_pics[0])
        while deaths < 7:
            print("\nYour String: "+update_chars.upper()+'\n')
            char = input("Please Enter character\n").lower()
            if char.replace(" ", "").isalpha() and len(char) == 1:
                position = []
                if char in update_chars:
                    print("You have already selected this char, try again \n")
                else:
                    if char in secret_word:
                        for index in range(word_length):
                            if secret_word[index] == char:
                                position.append(index)
                        for set_char in position:
                            update_chars = update_chars[:set_char] \
                                + char + update_chars[set_char+1:]
                        # print(update_chars+'\n')
                        if update_chars == secret_word:
                            print(secret_word.upper()+'\n')
                            print("Congratulations, You have won this stage\n")
                            if self.no_of_stages != stage_number:
                                time.sleep(1.5)
                                print("Loading next stage...\n")
                            else:
                                print("The End\n")
                            break
                    else:
                        # count deaths
                        deaths += 1
                        if deaths == 1:
                            print(hangman_pics[1])
                        elif deaths == 2:
                            print(hangman_pics[2])
                        elif deaths == 3:
                            print(hangman_pics[3])
                        elif deaths == 4:
                            print(hangman_pics[4])
                        elif deaths == 5:
                            print(hangman_pics[5])
                        elif deaths == 6:
                            print(hangman_pics[6])
                        else:
                            print(hangman_pics[7])
                            print("The String was: "+secret_word.upper()+'\n')
                            print("Well, Hang Man is dead and it's on you :(\n")
                            if self.no_of_stages != stage_number:
                                print("Loading next stage...\n")
                                time.sleep(1.5)
                                break
            else:
                print("Kindly enter single alphabet character\n")

    def start_game(self):
        for stage_number in range(0, self.no_of_stages):
            secret_word = hangman.words.pop(randrange(len(hangman.words)))
            hangman.show_secret_word(self, secret_word, stage_number+1)

def name_validation():
    while True:
        name = input("Please Enter Name\n")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Name is invalid, Kindly enter characters between A - Z\n")


def stages_count_validation():
    while True:
        stages = input("Pleas Enter number of stages between 1 and 5\n")
        try:
            if not int(stages):
                raise ValueError(
                    print("Kinldy Enter intger value")
                )
        except ValueError as e:
            print(f"Invalid data: {e}, please try again.\n")
        else:
            if int(stages) >= 1 and int(stages) <= 5:
                return int(stages)
            else:
                print("Kinldy enter stages between 1 and 5\n")


print("***** Welcome to Hang Man *****\n")
name = name_validation()
total_stages = stages_count_validation()
hang_man = hangman(name, total_stages)
hang_man.start_game()
x = hang_man.details()
print(x)
