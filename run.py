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
    def __init__(self, game_name, user_name, no_of_stages, total_wins,
                 total_loses):
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
        update_data.append_row([now.strftime('%d/%m/%Y %H:%M:%S'),
                                self.user_name, self.game_name,
                                self.no_of_stages,
                                self.total_wins, self.total_loses])

    def fetch_players_data():
        """
        This function fetches the data of last 3 players
        who have played the game and present it to the user
        """
        fetch_data = SHEET.worksheet("Players data")
        rows = []
        counter = 0
        get_data_length = \
            len(fetch_data.get_all_values())
        for index in range(get_data_length, 0, -1):
            row = fetch_data.row_values(index)
            rows.append(row)
            counter += 1
            if counter == 3:
                break
        if get_data_length < 4:
            rows.pop()
        if len(rows) == 0:
            print(" ---- Currently no data available ----")
        else:
            for data in rows:
                print(f"Date and time: {data[0]} | Username: {data[1]} | "
                      f"Game name: {data[2]} | Total stages: {data[3]} | "
                      f"Total wins: {data[4]} | Total loses: {data[5]}\n")


class Hangman(Game):
    """
    This class handles operations of hangman man, random selection of
    words, asking which word is it, calculate false and correct
    answers and handle multiple stages from 1 - 5 mentioned by user.
    """
    words = ('able about account acid across act addition adjustment'
             'advertisement after again against agreement '
             'air all almost among amount amusement and angle angry animal '
             'answer ant any apparatus apple approval '
             'arch argument arm army art as at attack attempt attention '
             'attraction authority automatic awake '
             'baby back bad bag balance ball band basebasin basket bath be '
             'beautiful because bed bee before behaviour '
             'belief bell bent berry between bird birth bit bite bitter '
             'black blade blood blow blue board boat body '
             'boiling bone book boot bottle box boy brain brake branch brass '
             'bread breath brick bridge bright broken '
             'brother brown brush bucket building bulb burn burst business '
             'but butter button by '
             'cake camera canva card care carriage cart cat cause certain '
             'chain chalk chance change cheap cheese chemical '
             'chest chief chin church circle clean clear clock cloth cloud '
             'coal coat cold collar colour comb come comfort '
             'committee common company comparison competition complete '
             'complex condition connection conscious control cook '
             'copper copy cord cork cotton cough country cover cow crack '
             'credit crime cruel crush cry cup cup current curtain '
             'curve cushion damage danger dark daughter day  dead dear death '
             'debt decision deep degree delicate dependent '
             'design desire destruction detail development different '
             'digestion direction dirty discovery discussion disease '
             'disgust distance distribution division do dog door doubt down '
             'drain drawer dress drink driving drop dry dust '
             'ear early earth east edge education effect egg elastic '
             'electric end engine enough equal error even event ever '
             'every example exchange existence expansion experience  expert '
             'eye face fact fall false family far farm fat '
             'father fear feather feeble feeling female fertile fiction '
             'field fight finger fire first  fish fixed flag '
             'flame flat flight floor flower fly fold food foolish foot for '
             'force fork form forward fowl frame free  frequent '
             'friend from front fruit full future garden general get girl '
             'give glass glove go goat gold good government grain '
             'grass great green grey grip group growth  guide gun hair  '
             'hammer hand hanging happy harbour hard harmony hat hate '
             'have he head healthy hear hearing heart heat help high history '
             'hole hollow hookhope horn horse hospital hour house '
             'how humour I ice idea if ill important impulse in increase '
             'industry ink insect instrument insurance interest invention '
             'iron island jelly jewel join journey judge jump keep kettle '
             'key kick kind kiss knee knife knot knowledge land language '
             'last late laugh law  lead leaf learning leather left leg let '
             'letter level library lift light like limit line '
             'linen lip liquid list little living lock long look loose loss '
             'loud love low machine  make male man manager map mark '
             'market married  mass match material may meal measure meat '
             'medical meeting memory metal middle military milk mind '
             'mine minute mist mixed money monkey month moon morning mother '
             'motion mountain mouth move much muscle music nail '
             'name narrow nation natural near necessary neck need needle '
             'nerve net new news night no noise normal north nose not '
             'note now number nut observation of off offer office oil old on '
             'only open operation opinion opposite or orange order '
             'organization ornament other out oven over owner page pain '
             'paint paper parallel parcel part past paste payment peace '
             'pen pencil person physical picture pin pipe place plane '
             'plant plate play please pleasure plough pocket point '
             'poison polish political poor porter position possible pot '
             'potato powder power present price print prison private pump'
             'probable process produce profit property prose protest public'
             'pull punishment purpose push put quality question quick quiet '
             'quite rail rain range rat rate ray reaction reading ready '
             'reason receipt record red regret regular relation religion '
             'representative request respect responsible rest reward rhythm '
             'rice right ring river road rod roll roof room root '
             'rough round rub rule run sad safe sail salt same sand say '
             'scale school science scissors screw sea seat second '
             'secret secretary see seed seem selection self send sense '
             'separate serious servant shade shake shame sharp sheep '
             'shelf ship shirt shock shoe short shut side sign silk silver '
             'simple sister size skin  skirt sky sleep slip slope '
             'slow small smash smell smile smoke smooth snake sneeze snow so '
             'soap society sock soft solid some son song sort '
             'sound soup south space spade special sponge spoon spring '
             'square stage stamp star start statement station steam '
             'steel stem step stick sticky stiff still stitch stocking '
             'stomach stone stop store story straight strange street '
             'stretch strong structure substance such sudden sugar '
             'suggestion summer sun support surprise sweet swim system '
             'table tail take talk tall taste tax teaching tendency test '
             'than that the then theory there thick thin thing this '
             'thought thread throat through through thumb thunder ticket '
             'tight till time tin tired to toe together tomorrow tongue '
             'tooth top touch town trade train transport tray tree trick '
             'trouble trousers true turn twist umbrella '
             'under unit up use value verse very vessel view violent voice '
             'waiting walk wall war warm wash waste watch water wave wax '
             'way weather week weight well west wet wheel when where while '
             'whip whistle white who why wide will wind '
             'window wine wing winter wire wise with woman wood wool word '
             'work worm wound writing wrong year yellow yes yesterday '
             'ant baboon badger bat bear beaver camel cat clam cobra cougar '
             'coyote crow deer dog donkey duck eagle ferret fox frog goat '
             'goose hawk lion lizard llama mole monkey moose mouse mule newt '
             'otter owl panda parrot pigeon python rabbit ram rat raven '
             'rhino salmon seal shark sheep skunk sloth snake spider '
             'stork swan tiger toad trout turkey turtle weasel whale wolf '
             'wombat zebra '
             'you young Android ').split()
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
=========''']  # noqa

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
            print(f"The word was: {secret_word.upper()}")
            print("\n==============================================")
            print("Well, Hang Man is dead and it's on you :(")
            print("==============================================\n")
            time.sleep(2)
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
        tried_chars = ''
        all_chars = ''
        for value in range(word_length):
            update_chars += '_'
        deaths = 0
        print(Hangman.hangman_pics[0]+"\n")
        while deaths < 7:
            print("\n------------------------------------------------------")
            print(f"Characters used till now: {all_chars}")
            print("------------------------------------------------------\n")
            print("Your Guess: "+" ".join(update_chars.upper())+'\n')
            char = input("Please enter character\n").lower()
            if char.replace(" ", "").isalpha() and len(char) == 1:
                if char.upper() not in all_chars:
                    all_chars += f"{char.upper()} "
                position = []
                if char in update_chars or char in tried_chars:
                    print("\n==============================================")
                    print("Character was already used, Please try again")
                    print("==============================================")
                else:
                    tried_chars += char
                    if char in secret_word:
                        for index in range(word_length):
                            if secret_word[index] == char:
                                position.append(index)
                        for set_char in position:
                            update_chars = update_chars[:set_char] \
                                + char + update_chars[set_char+1:]
                        if update_chars == secret_word:
                            print(secret_word.upper()+'\n')
                            print("\n========================================")
                            print("Congratulations, You have won this stage")
                            print("========================================\n")
                            self.total_wins += 1
                            if self.no_of_stages != stage_number:
                                print("Loading next stage...\n")
                                time.sleep(1.5)
                            else:
                                time.sleep(1.5)
                            break
                    else:
                        deaths += 1
                        Hangman.calculate_invalid_answers(self, deaths,
                                                          secret_word,
                                                          stage_number)
            else:
                print("\n=======================================")
                print("Kindly enter single alphabet character")
                print("=======================================\n")

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
        name = input("Please Enter Your Name:\n")
        if name.replace(" ", "").isalpha():
            return name
        else:
            print("\n======================================================")
            print("Name is invalid. Kindly enter characters between A - Z")
            print("======================================================\n")


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
                    print("Kindly enter stages between 1 and 5")
                )
        except ValueError:
            print("\n=======================================")
            print("Kindly enter stages between 1 and 5")
            print("=======================================\n")
        else:
            if int(stages) >= 1 and int(stages) <= 5:
                return int(stages)
            else:
                print("\n=======================================")
                print("Kindly enter stages between 1 and 5")
                print("=======================================\n")


def main():
    """
    This is the main function, The hangman logo is here, The
    username is asked in the beginning so that if user wants to
    keep playing he/she doesn’t have to enter username again and
    again.
    the user is asked if he/she want to keep playing or not once
    they had played every stage.
    """
    print(" _                                             ")
    print("| |                                            ")
    print("| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  ")
    print("| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ ")  # noqa
    print("| | | | (_| | | | | (_| | | | | | | (_| | | | |")
    print("|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|")  # noqa
    print("                    __/ |                      ")
    print("                   |___/                       ")
    print("\n")
    name = name_validation()
    while True:
        set_game = input("\nPress 'Y' to start game\nPress 'L' to see last 3 "
                         "players scores\nPress any other button to "
                         "exit.\n").lower()
        if set_game == 'y':
            total_stages = stages_count_validation()
            hang_man = Hangman(name, total_stages)
            hang_man.start_game()
            hang_man.update_player_data()
        elif set_game == 'l':
            Game.fetch_players_data()
        else:
            print("Have a nice day. Good Bye! :)\n")
            time.sleep(1.5)
            break


if __name__ == "__main__":
    main()
