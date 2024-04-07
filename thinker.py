from word import Word_Manager
import data


'''
    This module, as its name suggests, performs the task of thinking and making guesses for the program.
    The 'Thinker' class is responsible for providing the best possible guess each time, relying on the 
    frequencies of letters within the set of words. The optimal guess is determined by the most frequently
    occurring letter. This module interacts directly with the main module, the word module, and the data 
    module. Its objective is to facilitate the connection between the main module and the word module. 
    This is achieved by delivering the user's response from the main module to the word module, and conveying 
    the updated word state from the word class back to the main class.
'''


class Thinker:
    def __init__(self, nb_of_letters: int) :
        '''
        -  dataset (list): This attribute holds the dataset of words with 'n' letters, utilizing the ‘read_dataset_for_length’ method in the data module.
        -  guessed_letters (list): It stores the guessed letters to prevent re-guessing a letter.
        -  word  (Word_manager): Initialized by the number of letters, the ‘thinker’ serves as the intermediary between the ‘word’ module and the ‘main’ module.
        '''
        self.dataset = data.read_dataset_for_length(nb_of_letters)
        self.word = Word_Manager(nb_of_letters)
        self.guessed_letters = []

    def buildFrequency(self) -> dict[str, int]:
        '''
        This function constructs a dictionary and accesses the words within the dataset. It then adds the encountered letters in the words list along with the number of times each letter occurs.
        Returns: (dict):  frequency dictionary, where the keys are the letters encountered within the dataset, and the values are their respective frequencies
        '''
        frequency = dict()
        for word in self.dataset:
            for letter in word:
                if letter not in frequency:
                    frequency[letter] = 1
                else:
                    frequency[letter] += 1  
        return frequency

    def mostFrequent(self, frequency: dict[str, int]) -> str:
        '''
        This function is designed to optimize the guess by selecting the letter with the highest frequency of occurrences.

        Parameters: frequency (dict): the pairs (letter-frequency) are sorted in decreasing order of frequencies.

        Returns: (str) most_freq
        '''
        # arrange keys in decreasing order of values
        sorted_freq = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        most_freq = ""
        for letter, freq in sorted_freq:
            most_freq = letter
            #if mostFreq is guessed before, take next most frequent letter
            if letter not in self.guessed_letters:
                break
        return most_freq

    def guess(self) -> str:
        '''
        This function uses the two previous methods to make the guess, then appends the guess to ‘guessed_letters’ list.
        Returns : (str) guessed letter
        '''
        freq = self.buildFrequency()
        my_guess = self.mostFrequent(frequency=freq)
        self.guessed_letters.append(my_guess)
        return my_guess

    def think(self, letter: str, positions: list[int]) -> str:
        '''
        This function interacts with the main and word modules.
            -	Delivers given user response to word.update_state()
            -	Updates the dataset attribute using filter_words() method from the data module based on user response
        Parameters:
            -	letter (str): guessed letter
            -	positions (list[int]): list of positions of the letter in the word. If empty, letter is not in word
        Returns: (str) the updated word state as a string by calling word.getState()
        '''
        self.word.updateState(letter=letter, positions=positions)
        self.dataset = data.filter_words(dataset=self.dataset, letter=letter, positions=positions)
        return self.word.getState()
