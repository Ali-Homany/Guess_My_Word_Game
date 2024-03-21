import re

class Word_Manager:
    def __init__(self, word_size: int):
        self.word_state = ["_" for _ in range(word_size)]

    @classmethod
    def getPattern(cls, letter: str, positions: list[int], word_length: int) -> re.Pattern:
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
        return bool(compiled_pattern.fullmatch(word))
 
    def getState(self) -> str:
        return ''.join(self.word_state)

    def updateState(self, letter: str, positions: list[int]) -> None:
        # raise error if any position is invalid (negative, out of range, or already occupied)
        if not all(isinstance(pos, int) and 0 <= pos < len(self.word_state) and self.word_state[pos] == "_" for pos in positions):
            raise ValueError("Invalid position(s) or position(s) already occupied")
        # if all valid, update word_state
        for position in positions:
            self.word_state[position] = letter
