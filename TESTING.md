# Testing
- I confirmed that all input fields need a valid value.
- I confirmed that application will not crash on giving in invalid values such as space, special characters and digits or characters where they are not required.
- I confirmed that user is asked to enter valid input where he/she had given invalid input.
- I confirmed the application will not exit once game is over and will ask user if he/she wants to play again.
- I confirmed that user data will be updated on spread sheet once game is completed.
- I confirmed that user can see the last three player’s data via main menu by pressing L.
- I confirmed that game is easy to understand. The hangman ASCII art is also there to enhance the user experience and for better understanding.
- I confirmed that warning messages will appear on invalid inputs.
- I confirmed that user will be asked to enter new alphabet character when he/she inputs duplicate characters.
- I confirmed that total stages that user can select is between 1 and 5.
- I confirmed that on pressing Y, game will start.
- I confirmed that on main menu other than Y or L if any other character, space, digit, special characters or even simple enter is given the game will exit.

## Manual Testing
| Test | Expected | Outcome |
| --- | --- | --- |
| Open landing page | Series of print statements making word Hangman on console along with the enter username statement | As Expected |
| Enter Username with special characters/only spaces/digits | Invalid Input message should appear and user must try again | As Expected |
| Enter normal username | Main menu must be now visible to user | As Expected |
| Enter username without input | Invalid input message should appear | As Expected |
| Press any other button other than Y or L on main menu| Program should exit | As Expected |
| Press L on main menu | Should show last three game users data | As Expected |
| Press Y on main menu | stages between number 1 to 5 selection must be shown | As Expected |
| Input random character/digits/alphabets on stage selection | Should show invalid entry message and user must try again | As Expected |
| Enter stage selection without input | Should show invalid entry message and user must try again | As Expected |
| User enter digits between 1 and 5 during stage selection | The Hangman Initial ASCII must be printed showing the game had begun | As Expected |
| User enters an alphabet | The alphabet entered must be updated in used characters’ list and user can see it. | As Expected |
| User enters multiple characters/digits/alphabet | The warning message must appear and user can try again. | As Expected |
| User enters without input | The warning message must appear and user can try again | As Expected |
| User enters same character | Inform user that user had already used this letter he/she can try again | As Expected |
| Enter Invalid alphabets that does not match the word | The hang man ASCII art must be updated on each try. On last try user must be informed that hangman is dead | As Expected |
| Enter valid alphabets that matches the word | Congratulate user on completing the stage. | As Expected |
| On stage completion | If more than one stage exists loading next stage must appear and start the game once again. If only one stage is selected the main menu must appear. | As Expected |
| Input characters in lower and upper cases | This should not impact the game flow, The game will still accept lower or upper cases letter with no issue | As Expected |

## Validator Testing
### CI Python Linter
I used the recommended [CI Python Linter](https://pep8ci.herokuapp.com/#) to validate my python code.
| Page | PEP8 URL | Screenshot | Notes |
| --- | --- | --- | --- |
| run.py | [PEP8](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/readme_img/ci-python-lynter.png) | Pass: No Errors |
- <b>NOTE : </b> Hangman ASCII arts were causing "W605 invalid escape sequence '\ '" in PEP8 CI validation at three points. To suppress it #noqa is used on these points which is learned from [this stackoverflow](https://stackoverflow.com/questions/18444840/) link.

## List of bugs and issues
1. The header column was also fetched along with players data from spread sheet if data is less than four.
    #### Fix:
    - I used if statement if data is less than 4, simply pop the header column.

2. In case no data exist in spread sheet, there was no response from application for user which was confusing.
   #### Fix:
    - I checked if data length was equal to 0. If so inform user that there is no data available.

3. Hang man ASCII art was causing "W605 invalid escape sequence '\ '" in PEP8 CI validation at three points.
   #### Fix:
   - I used #noqa on these points which was learned from [this stackoverflow](https://stackoverflow.com/questions/18444840/) link.

4. The loading of new stage comment was pointless even though I wanted to give the user more feeling of a game.
   #### Fix:
   - I imported time and used sleep method on various points in code for more gaming feel.

5. As per discussion with my mentor, the player was only alerted if a character exits in a word and he/she selects that character once again but no alert was given if character was not doesn’t exist in a word and it was selected multiple times. In this case Hangman dies without alerting the player.
   #### Fix:
    - New check was added in code where the it checks both cases and alerts Player accordingly.

6. After deployment it was observed that the gap which was appearing between dashes on gitpod’s console, it disappeared on Heroku. No actual space was given in between dashes in code as it could be seen easily on gitpod’s console but on Heroku there was just as straight line.
   #### Fix:
    - Simply used " ".join() on the final output, so it became _ _ _ instead of ___.

7. The _ must be replaced with the actual word if a character is found inside the letter thought by computer.
   #### Fix:
   - Slicing was used in this case. First position of character was located and then replaced with the actual word. Solution was taken from [this](https://pythonexamples.org/python-string-replace-character-at-specific-position/) link.

8. main() function was the one where the program starts executing without no checks which was wrong.
    #### Fix:
    - My mentor added if __name__ == "__main__": before main function and explained why it was necessary here.

9. I was trying to insert data to spread sheet without giving it proper structure on which application crashes.
    #### Fix:
    - Data needed to be inserted inside list and then pushed to spread sheet.

## Unfixed bugs
- No unfixed bugs.

Return back to the [README.md](/README.md) file.