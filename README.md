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

## User Stories
- I can understand the purpose of this game.
- I can learn new words.
- I can use new learned words in normal routine life.
- I can challenge myself to see how good is my vocabulary.
- I can navigate through application without any issue.
- I get a mixture of old and new words when I play game again.
- I can see the number of stages, total wins and loses in last three entries.
- I can see the ascii image of hangman and from it able to undestand remaining tries.
- I can see the actual word in the end if I fails to guess the correct word.
- I can see the characters that I have tried while playing game.

## Features
- Header
    - On top of the console header is clearly visible to players and it can tell by its name what the game is about.
    - The ASCII art of word "Hangman" is there to enhance the user experience.

    ![Hangman header](/documentation/readme_img/header.png)

- Username and options
    - The username must be given before proceeding towards options.
    - Once username is set, player had three options as following:
        - He/She can press Y to start game
        - He/She can press L to see last three players
        - He/She can exit game by pressing any other button

    ![username and options](/documentation/readme_img/username.png)

- Stages Selection
    - On pressing Y user have the option to select stages between 1 and 5.
    - The game will keep running even after first stage till the option user had selected.

    ![Stages Selection](/documentation/readme_img/stages-selection.png)

- Start Game
    - Soon after selecting the stage which is "3" in below image the game will start.
    - The initial state of ASCII art of Hangman will be shown.
    -  Characters used till now will be empty right now which will be filled later.
    - In front of Your Guess, there are dashes to show number of characters in word.
    - Player will be asked to enter a character at this point.

    ![Start Game](/documentation/readme_img/after-stage-selection.png)
