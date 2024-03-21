from word import Word_Manager
import data

class Thinker:
    def __init__(self, nb_of_letters: int) :
        self.dataset = data.read_dataset_for_length(nb_of_letters)
        self.word = Word_Manager(nb_of_letters)
        self.guessed_letters = []

    def buildFrequency(self) -> dict[str, int]:
        frequency = dict()
        for word in self.dataset:
            for letter in word:
                if letter not in frequency:
                    frequency[letter] = 1
                else:
                    frequency[letter] += 1  
        return frequency

    def mostFrequent(self, frequency: dict[str, int]) -> str:
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
        freq = self.buildFrequency()
        my_guess = self.mostFrequent(frequency=freq)
        self.guessed_letters.append(my_guess)
        return my_guess

    def think(self, letter: str, positions: list[int]) -> str:
        self.word.updateState(letter=letter, positions=positions)
        self.dataset = data.filter_words(dataset=self.dataset, letter=letter, positions=positions)
        return self.word.getState()
