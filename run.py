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
        print(stage_number)
        word_length = len(secret_word)
        update_chars = ''

        for x in range(word_length):
            update_chars += '_'
        print(secret_word)
        print(update_chars)

        won = False
        deaths = 0  #7

        while deaths < 7:
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
                if char in secret_word:
                    for index in range(word_length):
                        if secret_word[index] == char:
                            position.append(index)
                        # else:
                        #     print("Not the required char")
                    print(position)
                    # Now set positions in _ string
                    for set_char in position:
                        update_chars = update_chars[:set_char] \
                            + char + update_chars[set_char+1:]
                    print(update_chars)
                    if update_chars == secret_word:
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
                        print("death 1")
                    elif deaths == 2:
                        print("death 2")
                    elif deaths == 3:
                        print("death 3")
                    elif deaths == 4:
                        print("death 4")
                    elif deaths == 5:
                        print("death 5")
                    elif deaths == 6:
                        print("death 6")
                    else:
                        print("death 7")
                        if(self.no_of_stages != stage_number):
                            print("Loading next stage\n")
                            break
                        else:
                            print("The End")
                    # Death comes one step closer at this point
                # won is set to true for now to avoid other loop
                # won = True
            else:
                print("Kindly enter single alphabetic character")

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
    name = input("Please Enter Name\n")
    while True:
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
print(hang_man.details())
hang_man.start_game()