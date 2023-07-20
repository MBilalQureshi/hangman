import gspread
from google.oauth2.service_account import Credentials
from random import randrange
from datetime import datetime
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Hangman')


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

    def update_player_data(self):
        """
        This function updates the players data after completing
        their number of selected stages
        """
        now = datetime.now()
        update_data = SHEET.worksheet("Players data")
        update_data.append_row([now.strftime('%d/%m/%Y %H:%M:%S'), self.user_name, self.game_name, self.no_of_stages, self.total_wins, self.total_loses])

    def fetch_players_data():
        """
        This function fetches the data of last 10 players
        who have played the game and present it to the user
        """
        fetch_data = SHEET.worksheet("Players data")
        rows = []
        counter = 0
        for index in range(len(fetch_data.get_all_values()), 0, -1):
            row = fetch_data.row_values(index)
            rows.append(row)
            counter += 1
            if counter == 10:
                break
        
        if len(rows) < 10:
            rows.pop(len(rows)-1)
        for data in rows:
            print(f"Date and time:{data[0]} Username: {data[1]} Game name: {data[2]} Total stages: {data[3]} Total wins: {data[4]} Total loses: {data[5]}\n")


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
                    print("You have already selected this character, try again\n")
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
        set_game = input("\nPress y to start game, press l to see last 10 players scores or any other button to exit.\n").lower()
        if set_game == 'y':
            total_stages = stages_count_validation()
            hang_man = Hangman(name, total_stages)
            hang_man.start_game()
            hang_man.update_player_data()
        elif (set_game == 'l'):
            # hang_man = Hangman()
            Game.fetch_players_data()
        else:
            print("Have a nice day. Good Bye! :)\n")
            time.sleep(1.5)
            break


if __name__ == "__main__":
    main()
