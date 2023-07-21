# Hangman
Hangman is a classic game that was actually introduced in 1894 called Birds, Beasts, and Fishes. At that time it lacks the image of the hangman which was later introduced in 1902.

This is a mind and logic game. This game can be easy but very challenging at the same time but in anycase it helps the players to learn new words and add new set of vocablury they can use in their daily life routine. The player has 7 tries and after that the hangman gets hunged. For users learning purpose the word will be shown after last try.

Click [here](https://hangman-frenzy-4d545907a764.herokuapp.com/) to see the live website.

![Hangman website mockup](/documentation/readme_img/p3-mockup.png)

## How to play
 1. The computer thinks of a word and show dashes in length eqaul to that of a word.
 2. The player than guesses a character.
 3. One of the dash is replaced by actual character if it exists in computer word.
 4. Player cannot select the character that was selected previously.
 5. If the character is invalid, it puts hangman to near death situation by 1. Hangman has only 7 lives.
 6. If all words are found,S the players is being congratulated.
 7. If player fails to find all words, hangman dies but the player will be show what the actual word was.

## User stories
- I can understand the purpose of this game.
- I can learn new words.
- I can use new learned words in normal routine life.
- I can challenge myself to see how good is my vocabulary.
- I can navigate through application without any issue.
- I get a mixture of old and new words when I play game again.
- I can see the number of stages, total wins and loses in last three entries.
- I can easily perdict remaing tries by viewing the ASCII images of hangman.
- I can see the actual word in the end if I fails to guess the correct word.
- I can see the characters that I have tried while playing game.

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
- At this point player is asked to enter a character .

![Start Game](/documentation/readme_img/after-stage-selection.png)

- Once player starts giving characters the ASCII art of hangman also starts to get filled based on invalid answers.
- Characters used till now string will start showing used up characters.
- Dashes infront of your guess string will also start filling with proper characters.

![Start Game](/documentation/readme_img/game-play.png)

### Stage failed
- On failing seven times the stage is lost and hangman is dead message appears on screen.
- The word is also printed so that user can play and learn at the same time.
- Game ends here if player had only one stage selected or he/she is on last stage. The user can select from three options mentioned in "Username and main menu" section once again. The username will remain same for the player's fesability.

![stage failed](/documentation/readme_img/hangman-is-dead.png)

### Stage cleared
- The stage is cleared once player find all characters and congratulations message appeares on the screen.
- Game ends here if player had only one stage selected or he/she is on last stage. The user can select from three options mentioned in "Username and main menu" section once again. The username will remain same for the player's fesability.

![stage cleared](/documentation/readme_img/stage-won.png)

### Loading next stage
- Loading next stage only appeares when user selects more than one stage in the begining.

![stage cleared](/documentation/readme_img/loading.png)

# Last three players scores
- Now after completing game we are back at main menu and we have selected "L". Now Player can see last three players following data:
    - Date and Time
    - Username
    - Game name
    - Total stages
    - Total wins
    - Total loses
- This game dosen't require leaderboard as it has multiple stages options and user can select how many he/she would love to play.

![last three players](/documentation/readme_img/last-three-users.png)

### Warning messages
Following are the warning messages on invalid data entery:
1. Message on invalid username.

![message 1](/documentation/readme_img/invalid-username.png)

2. Message on invalid stage number.

![message 2](/documentation/readme_img/invalid-stage-entry.png)

3. Message when invalid or more than one character is given.

![message 3](/documentation/readme_img/invalid-alpha-char.png)

### Exit message
- A good bye message is shown when player wants to exit.

![exit](/documentation/readme_img/exit.png)
