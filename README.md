# translation-game
Translation Game (French / Spanish)

-- This game was created for a python project. Please feel free to use it... Nino

## Introduction

The Translation Game is a Python application designed to help users practice their translation skills between English, French, and Spanish. The game has two modes: translation from French/Spanish to English, and translation from English to French/Spanish. In the first mode, the game presents the user with a random word in either French or Spanish, and the user must type in the English translation. In the second mode, the game presents the user with a random English word, and the user must type in the French or Spanish translation. The game uses a CSV file called `dictionary.csv` as the source of words for translation. The file has three columns: the word, the language it's in, and its translation to English. If the game presents a word that is not in the dictionary, it uses the Google Translate API to translate it.

## Design and Implementation

The game is divided into three Python files: `game.py`, `translator.py`, and `dictionary.csv`.

`game.py` contains the main code for running the game. It imports the other files and provides the user interface for choosing between the two modes and playing the game. It also keeps track of the user's score.

`translator.py` contains the code for translating words using the dictionary and the Google Translate API. It has functions for getting a random word in French or Spanish, searching the dictionary for a translation, using the API to translate a word, and translating a sentence to French or Spanish.

`dictionary.csv` contains the dictionary of words used by the game. It has three columns: the word, the language it's in, and its translation to English.

When the user runs `game.py`, the game presents a menu with two options: play the translation game or use the translator. If the user chooses to play the game, the game presents another menu with two options: translate from French/Spanish to English or translate from English to French/Spanish. The game then presents the user with a random word and prompts them to type in the translation. If the user's answer is correct, they earn a point and the game presents another word. If the user's answer is incorrect, the game presents the correct answer and moves on to the next word. The game ends when the user reaches the maximum score or quits the game.

If the user chooses to use the translator, the game prompts them to type in a sentence in English. The game then presents another menu with two options: translate the sentence to French or translate the sentence to Spanish. The game then uses the Google Translate API to translate the sentence and presents the result to the user.

## Conclusion

Overall, the Translation Game provides a fun and educational way for users to practice their translation skills and learn new words in French and Spanish. The game is easy to use and provides a user-friendly interface for both playing the translation game and using the translator. The game is also highly customizable, as users can modify the dictionary and configuration files to suit their needs. The game demonstrates the power of Python in creating engaging and educational applications.

