from random import randrange


class game:
    def __init__(self, game_name, user_name):
        self.game_name = game_name
        self.user_name = user_name


class hangman(game):
    words = ["apple", "banana", "owl", "controller", "helipad", "semiconductor"]

    def __init__(self, no_of_stages, game_name, user_name):
        self.no_of_stages = no_of_stages
        game.__init__(self, game_name, user_name)

    def details(self):
        return f"Game name is {self.game_name}, Game stages are {self.no_of_stages}, Username is {self.user_name}"


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
        # print(stage_number)
        word_length = len(secret_word)
        update_chars = ''

        for x in range(word_length):
            update_chars += '_'
        # print(secret_word)
        

        deaths = 0  #7
        print(hangman_pics[0])
        while deaths < 7:
            print("\nYour String: "+update_chars+'\n')
            char = input("Please Enter character\n")
            if char.replace(" ", "").isalpha() and len(char) == 1:

                # check char in actaul word
                # if word match put it in the position in __
                # if word not match warn the user and put hangman to near \
                #  death situation
                # if all words match tell user he hadt \
                #  won and print next round if multiple stages
                # at the end ask user if wants to play again
                position = []
                if char in update_chars:
                    print("You have already selected this char, try again \n")
                else:
                    if char in secret_word:
                        for index in range(word_length):
                            if secret_word[index] == char:
                                position.append(index)
                            # else:
                            #     print("Not the required char")
                        # print(position)
                        # Now set positions in _ string
                        for set_char in position:
                            update_chars = update_chars[:set_char] \
                                + char + update_chars[set_char+1:]
                        # print(update_chars+'\n')
                        if update_chars == secret_word:
                            print(secret_word+'\n')
                            print("Congratulations, You have won this stage\n")
                            if self.no_of_stages != stage_number:
                                print("Loading next stage\n")
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
                            print("The String was: "+secret_word+'\n')
                            if(self.no_of_stages != stage_number):
                                print("Loading next stage\n")
                                break
                            else:                               
                                print("Well, Hang Man is dead and it's on you :(\n")
                                # Death comes one step closer at this point
                                # won is set to true for now to avoid other loop
                                # won = True
            else:
                print("Kindly enter single alphabet character\n")

    def start_game(self):
        # win = False
        # valid_Answer = 0
        # Invalid_Answers = 0
        # select a random secret word from list
        # remove from list and make count words and make _

        for stage_number in range(0, self.no_of_stages):
            secret_word = hangman.words.pop(randrange(len(hangman.words)))
            hangman.show_secret_word(self, secret_word, stage_number+1)
            # remove break later to run all stages
            # break


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
hang_man = hangman(total_stages, "Hang Man", name)
# print(hang_man.details())
hang_man.start_game()