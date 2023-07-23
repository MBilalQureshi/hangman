# Hangman
Hangman is a classic game that was actually introduced in 1894 called Birds, Beasts, and Fishes. At that time, it lacks the image of the hangman which was later introduced in 1902.

This is a mind and logic game. This game can be easy but very challenging at the same time but in any case it helps the players to learn new words and add new set of vocabulary they can use in their daily life routine. The player has 7 tries and after that the hangman gets well hanged. For users learning purpose the word will be shown after last try.

Click [here](https://hangman-frenzy-4d545907a764.herokuapp.com/) to see the live website.

![Hangman website mockup](/documentation/readme_img/p3-mockup.png)

## How to play
 1. The computer thinks of a word and show dashes in length equal to that of a word.
 2. The player than guesses a character.
 3. One of the dash is replaced by actual character if it exists inside the word that computer had thought.
 4. Player cannot select the character that was selected previously.
 5. If the character is invalid, it puts hangman to near death situation by 1. Hangman has only 7 lives.
 6. If all words are found. the players is being congratulated.
 7. If player fails to find all words, hangman dies but the player will be show what the actual word was for learning purpose.

## User stories
- I can understand the purpose of this game.
- I can learn new words.
- I can use new learned words in normal routine life.
- I can challenge myself to see how good is my vocabulary.
- I can navigate through application without any issue.
- I get a mixture of old and new words when I play game again.
- I can see the number of stages, total wins and losses in last three entries.
- I can easily predict remaining tries by viewing the ASCII images of hangman.
- I can see the actual word in the end if I fails to guess the correct word.
- I can see the actual word if I failed the stage.

## Features
### Header
- On top of the console header is clearly visible to players and it can tell by its name what the game is about.
- The ASCII art of word "Hangman" is there to enhance the user experience.

![Hangman header](/documentation/readme_img/header.png)

### Username and main menu
- The username must be given before proceeding towards options.
- Once username is set, player had three options as following:
    - He/She can press Y to start game
    - He/She can press L to see last three players
    - He/She can exit game by pressing any other button

![username and options](/documentation/readme_img/username.png)

### Stages selection
- On pressing Y user have the option to select stages between 1 and 5.
- The game will keep running even after first stage till the option user had selected.

![Stages Selection](/documentation/readme_img/stages-selection.png)

### Main game flow
- Soon after selecting the stage which is "3" in below image the game will start.
- The initial state of ASCII art of Hangman will be shown.
-  Characters used till now will be empty right now which will be filled later.
- In front of Your Guess, there are dashes to show number of characters in word.
- At this point player is asked to enter a character.

![Start Game](/documentation/readme_img/after-stage-selection.png)

- Once player starts giving characters the ASCII art of hangman also starts to get filled based on invalid answers.
- Characters used till now string will start showing used up characters.
- Dashes in front of your guess string will also start filling with proper characters.

![Start Game](/documentation/readme_img/game-play.png)

### Stage failed
- On failing seven times the stage is lost and hangman is dead message appears on screen.
- The word is also printed so that user can play and learn at the same time.
- Game ends here if player had only one stage selected or he/she is on last stage. The user can select from three options mentioned in "Username and main menu" section once again. The username will remain same for the player's feasibility.

![stage failed](/documentation/readme_img/hangman-is-dead.png)

### Stage cleared
- The stage is cleared once player find all characters and congratulations message appears on the screen.
- Game ends here if player had only one stage selected or he/she is on last stage. The user can select from three options mentioned in "Username and main menu" section once again. The username will remain same for the player's feasibility.

![stage cleared](/documentation/readme_img/stage-won.png)

### Loading next stage
- Loading next stage only appears when user selects more than one stage in the beginning.

![stage cleared](/documentation/readme_img/loading.png)

### View last three players data
- Now after completing game we are back at main menu and we have selected "L". Now Player can see last three players following data:
    - Date and Time
    - Username
    - Game name
    - Total stages
    - Total wins
    - Total loses
- This game doesn’t require leaderboard as it has multiple stages options and user can select how many he/she would love to play.

![last three players](/documentation/readme_img/last-three-users.png)

- The data is fetched from a Google spread sheet available on google drive.

![last three players spread sheet data](/documentation/readme_img/spreadsheet-data.png)

### Warning messages
Following are the warning messages on invalid data entry:
1. Message on invalid username.

![message 1](/documentation/readme_img/invalid-username.png)

2. Message on invalid stage number.

![message 2](/documentation/readme_img/invalid-stage-entry.png)

3. Message when invalid or more than one character is given.

![message 3](/documentation/readme_img/invalid-alpha-char.png)

### Exit message
- A good bye message is shown when player wants to exit.

![exit](/documentation/readme_img/exit.png)

## Testing
To see complete testing section, kindly click [here](/TESTING.md).

## Libraries and Technologies Used
### Python Libraries
- [time](https://docs.python.org/3/library/time.html) is used for putting normal game flow to sleep.
- [randrange](https://docs.python.org/3/library/random.html) is used to select a random word for list of words.
- [datetime](https://pypi.org/project/DateTime/) is used to get current date and time for the last three players entry.
- [gspread](https://pypi.org/project/gspread/) is used for communication with Google Sheets.
- [google.oauth2.service_account](https://google-auth.readthedocs.io/en/stable/index.html) is used to validate credentials and grant access to google service accounts.

### Programs Used
- [GitHub](https://github.com/) used to host repository.
- [GitPod](https://gitpod.io/) used to develop project and organize version control.
- [Heroku](https://www.heroku.com/) used to deploy the live project.
- [PEP8 Online](https://pep8ci.herokuapp.com/#) used to validate all the Python code.

## Deployment
### Heroku
The site was deployed using Heroku and the live link can be found here: [Hangman](https://hangman-frenzy-4d545907a764.herokuapp.com/).
1. Before actual deployment use "Heroku pip3 freeze > requirements.txt" on Gitpod console. This will add all the dependencies in requirements.txt file which will be needed by Heroku later during deployment.
2. Log in to [Heroku](https://www.heroku.com/).
3. On main page there is an option to create new app, click it.
4. Enter a unique application name and select your region.
5. Click on create app button.
6. Click settings and select Config Vars.
7. Click Reveal Config Vars and enter Key as "PORT" and Value as "8000" and press add button.
8. Input CREDS and the content of your Google Sheet API creds file as another config var and click add.
9. Scoll down on same page and add build packs, select "python" and click save.
10. Add another build pack "NodeJs" and click save.
11. Make sure python build pack is on top of NodeJs.
12. Go to top of page and select deploy option.
13. Select Github as deployment method.
14. Confirm to connect with github and auotherize Heroku from Github.
15. In search bar type repository name and click the connect button.
16. Scroll to the bottom of the deploy page and either click Enable Automatic Deploys for automatic deploys or Deploy Branch to deploy manually. Manually deployed branches will need re-deploying each time the repo is updated.
17. Click View to view the deployed site.


### Forking the GitHub Repository
With Forking one can make a copy of a repository and to view or make changes in it without affecting the original repository. Following are the steps to do this.
1. Log in to GitHub and locate [Hangman](https://github.com/MBilalQureshi/hangman) repository.
2. At the top right side of the page just below the navigation bar, locate the fork button.
3. You will now have a copy of the repository.

### Making a Local Clone
1. Log in to GitHub and locate [Hangman](https://github.com/MBilalQureshi/hangman) repository.
2. Just below the repository name, click "Code".
3. There is an option to copy HTTPS link. Press copy icon.
5. Open Git Bash on local machine.
4. Change the current working directory to the location where we want the cloned directory to be made.
5. Type git clone on bash and paste the HTTPS URL we copied earlier.
6. Press Enter. local clone will be created.

## Credits
### Extra Help
- Basic concepts of using google APIs, managing credentials, deployment in Heroku is taken and understood from Code Institute's [Love Sandwiches](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode) project.
- The concept of validating if character is alphabet is understood from [this](https://docs.python.org/2/library/stdtypes.html#str.isalpha) link.
- The concept of using randrange is understood from [this](https://bobbyhadz.com/blog/python-remove-random-element-from-list) link.
- The code for replacing a character is taken from [this](https://pythonexamples.org/python-string-replace-character-at-specific-position/) link.
- The hangman ASCII art is taken from [this github](https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c) link.
- Learned date and time in different formats is learned from [this](https://www.programiz.com/python-programming/datetime/current-datetime) link.
- Hangman word ASCII art is taken from [this](https://ascii.co.uk/art/hangman) link.
- Hangman ASCII arts were causing "W605 invalid escape sequence '\ '" in PEP8 CI validation, to suppress it #noqa is used at three points which is learned from [this stackoverflow](https://stackoverflow.com/questions/18444840/how-to-disable-a-pep8-error-in-a-specific-file) link.
- Words bank for Hangman game is taken from [this](https://github.com/YungNewton/HangMan/blob/master/hangMan.py) link.
### Acknowledgements
- My Mentor Antonio Rodriguez for helpful feedbacks during project development.
- Code Institute team for pointing in right direction.