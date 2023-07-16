from random import randrange

class game:
    def __init__(self,game_name,user_name):
        self.game_name = game_name
        self.user_name = user_name


class hangman(game):
    words =["apple","banana","owl","controller","helipad","semiconductor"]

    def __init__(self,no_of_stages,game_name,user_name):
        self.no_of_stages = no_of_stages
        game.__init__(self,game_name,user_name)

    def details(self):
        return f"Game name is {self.game_name}, Game stages are {self.no_of_stages}, Username is {self.user_name}"

    def start_game(self):
        print(f"Total stages are {self.no_of_stages}")
        win = False
        valid_Answer = 0
        Invalid_Answers = 0
        # select a random secret word from list
        # remove from list and make count words and make _

        for stage_number in range(0,self.no_of_stages):
            word = hangman.words.pop(randrange(len(hangman.words)))
            print(hangman.words)

def name_validation():
    while True:
        name = input("Please Enter Name\n")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print ("Name is invalid, Kindly enter characters between A - Z\n")

print("***** Welcome to Hang Man *****\n")
name = name_validation()
hang_man = hangman(6,"Hang Man",name)
print(hang_man.details())
hang_man.start_game()