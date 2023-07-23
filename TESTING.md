# Testing
- I confirmed that all input fields needs a valid value.
- I confirmed that application will not crash on giving in valid values such as space, special chracters and digits and chracters where they are not required.
- I confirmed that user is asked to enter valid input where he/she had given invalid input.
- I confirmed the application will not exit once game is over and will ask user if he/she wants to play again.
- I confirmed that user data will be updated on spread sheet once game is completed.
- I confirmed that user can see the last three users data via main menu.
- I confirmed that game is easy to understand. The hangman ASCII art is also there to enhance the user experince and for better understanding.
- I confirmed that warning messages will appear on invalid inputs.
- I confirmed that user will be asked to enter new alphabet chracter when he/she inputs duplicate characters.
- I confirmed that total stages that user can select is between 1 and 5.

## Validator Testing
### CI Python Linter
I used the recommended [CI Python Linter](https://pep8ci.herokuapp.com/#) to validate my python code.
| Page | PEP8 URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Main Page | [PEP8](https://pep8ci.herokuapp.com/#) | ![screenshot](/documentation/readme_img/ci-python-lynter.png) | Pass: No Errors |
- <b>NOTE : </b> Hangman ASCII arts were causing "W605 invalid escape sequence '\ '" in PEP8 CI validation on three points. To suppress it #noqa is used on these points which is learned from [this stackoverflow](https://stackoverflow.com/questions/18444840/) link.

## List of bugs and issues
