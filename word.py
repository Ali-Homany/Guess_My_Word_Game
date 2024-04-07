import re

class Word_Manager:
    '''
    The Word_Manager class serves as a tool for managing and manipulating words,
    particularly for tasks like word guessing games or word puzzles. It provides
    functionality to track the state of a word (with hidden letters), generate
    regex patterns for word matching, and update the word state based on user input.
    '''
    def __init__(self, word_size: int):
        '''
        wordState represents the current state of the word, where each letter is
        either revealed or hidden. Underscores (_) in the list indicate hidden
        letters, while actual letters represent revealed positions
        '''
        self.word_state = ["_" for _ in range(word_size)]

    @classmethod
    def getPattern(cls, letter: str, positions: list[int], word_length: int) -> re.Pattern:
        '''
        Generates a regex pattern based on a given letter, its positions in the word, and the word length.

        Parameters:
            - letter (str): The letter to generate the pattern for.
            - positions (list[int]): A list of integers representing positions where the letter appears.
            - word_length (int): The total length of the word.
        Raises:
            - (ValueError) if the positions are invalid or out of range
        '''
        # case 1: letter is incorrect, pattern is word that does not include this letter
        if len(positions) == 0:
            return re.compile(f"[^{letter}]{{{word_length}}}")

        # case 2: letter is correct, pattern is word that includes this letter at the given positions
        # create a list with dots to represent unknown positions
        pattern = ['.' for _ in range(word_length)]
        # replace the dots at specified positions with the given letter
        for position in positions:
            pattern[position] = re.escape(letter)
        # convert the list to a string
        pattern = ''.join(pattern)
        compiled_pattern = re.compile(pattern)
        return compiled_pattern

    @classmethod
    def isPattern(cls, word: str, compiled_pattern: re.Pattern) -> bool:
        '''
        Parameters:
            - word (str): The word to check against the compiled pattern.
            - compiled_pattern (re.Pattern): The compiled regex pattern for matching.
        Returns:
            (bool): True if the word matches the pattern, False otherwise
        '''
        return bool(compiled_pattern.fullmatch(word))
 
    def getState(self) -> str:
        '''
        Returns:
            (str): The current state of the word, with hidden letters represented by underscores
        '''
        return ''.join(self.word_state)

    def updateState(self, letter: str, positions: list[int]) -> None:
        '''
        Updates the word state by revealing new letters at specified positions.

        Parameters:
            - letter (str): The letter to reveal in the word state.
            - positions (list[int]): A list of integers representing positions to reveal the letter.
        Raises:
            - (ValueError) if any position is invalid (negative, out of range, or already occupied)
        '''
        # raise error if any position is invalid (negative, out of range, or already occupied)
        if not all(isinstance(pos, int) and 0 <= pos < len(self.word_state) and self.word_state[pos] == "_" for pos in positions):
            raise ValueError("Invalid position(s) or position(s) already occupied")
        # if all valid, update word_state
        for position in positions:
            self.word_state[position] = letter
