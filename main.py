import data
from thinker import Thinker


'''
    The main module in the Hangman game project serves as the controller,
    responsible for facilitating user interaction and monitoring the progress 
    of the game. It acts as the intermediary between the user and other 
    modules, primarily the "Thinker" module. The main module does not perform 
    significant computational tasks by itself but orchestrates the game flow 
    and coordinates actions with the "Thinker" module
'''


def play_game(word_length: int, tries: int = 10) -> None:
    '''
    This function manages the entire gameplay process, from initializing the game environment to handling the end of the game.
    Parameters:
        -	word_length (int): represents the length of the word the player needs to guess.
        -	Tries (int, optional): represents the number of attempts allowed to guess the word. Default is 10.

    '''
    thinker = Thinker(nb_of_letters=word_length)

    while  tries > 0:
        guessed_letter = thinker.guess()

        if guessed_letter == "":
          print("I give up!")
          break

        if not right_guess(guessed_letter):
            tries -= 1
            print("Incorrect guess. Attempts remaining:", tries)
            thinker.think(letter=guessed_letter , positions=[])
            continue

        while True:
            try:
                positions = get_positions(guessed_letter)
                response = thinker.think(letter=guessed_letter, positions=positions)
                print("Current word state: ", response)
                break
            except ValueError:
                    print("Invalid position(s). Please enter new position(s).")
        
        if is_word_guessed(state=response):
            print("Congratulations! I guessed the word.")
            data.learn_word(word=response)
            return

    handle_game_end(word_length=word_length)  


def is_word_guessed(state: str) -> bool:
    '''
    Parameters: state (str): represents the current state of the word with guessed letters filled in.
    Returns: (bool) returns True if all letters have been revealed, indicating that the word has been guessed, and False otherwise
    '''
    return '_' not in state


def right_guess(guessed_letter: str) -> bool:
    '''
    This function prompts the user to confirm whether the guessed letter is present in the word.
    Parameters: guessed_letter (str): Represents the letter guessed by the program.
    Returns: (bool) returns True if the user confirms the presence of the guessed letter, otherwise False
    '''
    response = input(f"Is '{guessed_letter}' in the word? (y/n): ").strip().lower()
    if response not in ["y","n"]:
        print("Invalid input. Please enter 'y' or 'n'.")
        return right_guess(guessed_letter)
    return response == "y"


def is_numeric(s: str) -> bool:
    '''
    Parameters: s (str): represents the string to be checked.
    Returns: (bool) returns True if all characters in the string are numeric, False otherwise
    '''
    return all(char.isdigit() for char in s)

  
def get_positions(guessed_letter) -> list[int]:
    '''
    This function prompts the user to input the positions of the guessed letter within the word. 
    Parameters: guessed_letter (str): Represents the guessed letter for which positions need to be entered.
    Returns: (list[int]) Returns a list of integers representing the positions entered by the user
    '''
    positions_str = input(f"Enter the position(s) of '{guessed_letter}' in the word (space-separated): ")
    positions = [int(pos.strip()) - 1 if is_numeric(pos.strip()) else str(pos.strip()) for pos in positions_str.split()]
    return positions


def handle_game_end(word_length) -> None:
    '''
    This function handles the end of the game by prompting the user to enter the word if it was not guessed correctly.
    Parameters: word_length (int): Represents the length of the word the player needs to guess
    '''
    print("Game over!")
    while True:
        new_word = input("Please enter the word you were thinking of: ")
        if len(new_word) == word_length:
            data.learn_word(new_word)
            break
        else:
            print(f"The word must have exactly {word_length} letters.")


def get_word_length() -> int:
    '''
    This function prompts the user to input the desired length of the word to be guessed.
    Returns: int: Returns the length of the word specified by the user
    '''
    word_length = input("Enter the size of the word(between 4 and 12): ")
    if not ( is_numeric(word_length) and (3 < int(word_length) <= 12) ):
        return get_word_length()
    return int(word_length)


if __name__ == "__main__":
    word_length = get_word_length()
    play_game(word_length=word_length)
