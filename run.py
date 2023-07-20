from random import randrange
from datetime import datetime
import time


class Game:
    """
    Purpose of this class is to manage the game data and push the data to the
    spread sheet.
    As parent game class, this will also handle multiple games in future
    other than hangman.
    """
    def __init__(self, game_name, user_name, no_of_stages, total_wins, total_loses):
        self.game_name = game_name
        self.user_name = user_name
        self.no_of_stages = no_of_stages
        self.total_wins = total_wins
        self.total_loses = total_loses

    def details(self):
        now = datetime.now()
        return f"Game name is {self.game_name}, Game stages are {self.no_of_stages}, Username is {self.user_name}, data and time is:{now.strftime('%d/%m/%Y %H:%M:%S')}, total won{self.total_wins}, total loose{self.total_loses}"


class Hangman(Game):
    """
    This class handles operations of hangman man, random selection of
    words, asking which word is it, calculate false and correct
    answers and handle multiple stages from 1 - 5 mentioned by user.
    """
    words = ["apple", "banana", "owl", "controller", "helipad", "semiconductor", "laptop"]
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

    def __init__(self, user_name, no_of_stages):
        Game.__init__(self, "Hang Man", user_name, no_of_stages, 0, 0)

    def calculate_invalid_answers(self, deaths, secret_word, stage_number):
        """
        This function calculates the invalid answers
        and generate hangman images based on it.
        It also tells on 7th try that user had failed and
        check if there is next stage or not
        """
        if deaths == 1:
            print(Hangman.hangman_pics[1])
        elif deaths == 2:
            print(Hangman.hangman_pics[2])
        elif deaths == 3:
            print(Hangman.hangman_pics[3])
        elif deaths == 4:
            print(Hangman.hangman_pics[4])
        elif deaths == 5:
            print(Hangman.hangman_pics[5])
        elif deaths == 6:
            print(Hangman.hangman_pics[6])
        else:
            print(Hangman.hangman_pics[7])
            self.total_loses += 1
            print("The word was: "+secret_word.upper()+'\n')
            print("Well, Hang Man is dead and it's on you :(\n")
            time.sleep(1.5)
            if self.no_of_stages != stage_number:
                print("Loading next stage...\n")
                time.sleep(1.5)
                # break

    def start_hangman(self, secret_word, stage_number):
        """
        The Hangman game start from here user give a character
        the algorithm checks if character was already given, if not
        it checks if it matches the one that was randomly generated,
        if it does, user is closer to save hangman, if this is also
        not the situation, this function puts hangman to near death by call
        another function
        """
        word_length = len(secret_word)
        update_chars = ''

        for x in range(word_length):
            update_chars += '_'
        deaths = 0
        print(Hangman.hangman_pics[0])
        while deaths < 7:
            print("\nYour Word: "+update_chars.upper()+'\n')
            char = input("Please enter character\n").lower()
            if char.replace(" ", "").isalpha() and len(char) == 1:
                position = []
                if char in update_chars:
                    print("You have already selected this character, try again \n")
                else:
                    if char in secret_word:
                        for index in range(word_length):
                            if secret_word[index] == char:
                                position.append(index)
                        for set_char in position:
                            update_chars = update_chars[:set_char] \
                                + char + update_chars[set_char+1:]
                        if update_chars == secret_word:
                            print(secret_word.upper()+'\n')
                            print("Congratulations, You have won this stage\n")
                            self.total_wins += 1
                            if self.no_of_stages != stage_number:
                                print("Loading next stage...\n")
                                time.sleep(1.5)
                            else:
                                time.sleep(1.5)
                            break
                    else:
                        deaths += 1
                        Hangman.calculate_invalid_answers(self, deaths, secret_word, stage_number)
            else:
                print("Kindly enter single alphabet character\n")

    def start_game(self):
        """
        This functions just fetch random word from words list and move it
        to another function along with total stages
        """
        for stage_number in range(0, self.no_of_stages):
            secret_word = Hangman.words.pop(randrange(len(Hangman.words)))
            Hangman.start_hangman(self, secret_word, stage_number+1)


def name_validation():
    """
    This function validates the username
    entered by the user
    """
    while True:
        name = input("Please Enter Name\n")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("Name is invalid. Kindly enter characters between A - Z\n")


def stages_count_validation():
    """
    This function sets the number of stages entered
    by the user from 1 to 5 and validates the data
    entered by the user.
    """
    while True:
        stages = input("Please Enter number of stages between 1 and 5\n")
        try:
            if not int(stages):
                raise ValueError(
                    print("Kinldy enter stages between 1 and 5\n")
                )
        except ValueError:
            print("Kinldy enter stages between 1 and 5\n")
        else:
            if int(stages) >= 1 and int(stages) <= 5:
                return int(stages)
            else:
                print("Kinldy enter stages between 1 and 5\n")


def main():
    """
    This is the main function, The hangman logo is here, The
    username is asked in the begining so that if user wants to
    keep playing he/she dosen't have to enter username again and
    again.
    the user is asked if he/she want to keep playing or not once
    they had played every stage.
    """
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")
    print("                    __/ |                      ")
    print("                   |___/                       ")
    name = name_validation()
    while True:
        set_game = input("\nDo you want to start the game? Press y for yes or any other button for no.\n").lower()
        if set_game == 'y':
            total_stages = stages_count_validation()
            hang_man = Hangman(name, total_stages)
            hang_man.start_game()
            x = hang_man.details()
            print(x)
        else:
            print("Have a nice day. Good Bye! :)\n")
            time.sleep(1.5)
            break


if __name__ == "__main__":
    main()
