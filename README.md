# Guess_My_Word_Game
This project is a program that can play "Guess my word" - aka Hangman - as the guessor (via the terminal without interface)

## Components:

### 0. Data Preparation:
We found a free dataset that contains 333,333 word. However, It needed some cleaning for invalid/unpoular words. Using pandas library, we managed to filter words based on occurrences count, and removed most of invalid words. Having around 50,000 words remaining, we splitted the words into groups, based on word length, to save each group into an independent text file,instead of searching the whole dataset each turn.

### 1. Main:
This module serves as the controller, responsible for facilitating user interaction and monitoring the progress of the game:

- Initiates the conversation with the user, guiding them through the gameplay process, and reading user answers.
- Throughout the game, it monitors the progress and keeps track of attempts, ensuring that the game proceeds smoothly.
- Interacts primarily with the "Thinker" module to make guesses, process user responses, and update the game state.

### 2. Thinker:
This module, as its name suggests, performs the task of thinking and making guesses for the program. It is responsible for:
- Providing the best possible guess each time, relying on the frequencies of letters within the set of words. The optimal guess is determined by the most frequently occurring letter. 
- It filters the word set depending on the user response. If the guessed letter is correct it removes all words that don't contain this letter at the specified positions, otherwise remove all word which contain it.

### 3. Word Manager:
This module serves as a tool for managing and manipulating words, particularly for tasks like word guessing games or word puzzles. It provides functionality to:
- Track the state of a word (with hidden letters)
- Generate regex patterns for word matching
- Update the word state based on user input

### 4. Data:
This module serves as the manager of word datasets, who facilitates interactions among various program modules. Its primary functions include handling data operations such as loading and updating word datasets efficiently.

## Usage
This project is relatovely simple to use. If you want to try it:

- Download [Python](https://www.python.org/downloads/)
- Download [this repository](https://github.com/homanydata/Guess_My_Word_Game/archive/refs/heads/main.zip)
- Run All cells in prepare_data.ipynb notebook. A 'Dataset' folder will be created automatically
- Run main.py, insert the length of the word you have chosen, then reply to each of the program guesses.

*Good Luck, try to beat our program :)*


For more details about the code, a detailed documentation is included in this repository at [Hangman Project Documentation](./Hangman%20Project%20Documentation.pdf)
