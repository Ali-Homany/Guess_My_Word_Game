import unittest
from unittest.mock import patch, MagicMock
from utils.thinker import Thinker


class TestThinker(unittest.TestCase):
    @patch("thinker.data.read_dataset_for_length")
    @patch("thinker.Word_Manager")
    def setUp(self, mock_Word_Manager, mock_read_dataset_for_length) -> None:
        mock_Word_Manager.return_value = MagicMock()
        mock_read_dataset_for_length.return_value = ["hello", "water", "science"]

        self.thinker = Thinker(5)
        self.expected_freq = {"h": 1, "e": 4, "l": 2, "o": 1, "w": 1, "t": 1, "s": 1, "c": 2, "i": 1,
                              "r": 1, "n": 1, "a": 1}

    def test_build_frequency(self):
        self.assertEqual(self.thinker.build_frequency(), self.expected_freq)

    def test_mostFrequent(self):
        freq = {"a": 1, "b": 4, "c": 2}
        # case 1:
        self.assertEqual(self.thinker.mostFrequent(freq), "b")

        # case 2: avoid previously guessed letters
        self.thinker.guessed_letters = ["e", "b"]
        self.assertEqual(self.thinker.mostFrequent(freq), "c")

    @patch("thinker.Thinker.mostFrequent")
    def test_guess(self, mock_mostFrequent):
        mock_mostFrequent.return_value = "e"

        # case 1
        self.assertEqual(self.thinker.guess(), "e")
        self.assertEqual(self.thinker.guessed_letters, ["e"])

        # case 2: guessed letters is not empty
        self.thinker.guessed_letters = ["b"]
        self.thinker.guess()
        self.assertEqual(self.thinker.guessed_letters, ["b", "e"])

    @patch("thinker.data.filter_words")
    def test_think(self, mock_filter_words):
        mock_filter_words.return_value = ["hello", "science"]

        # check if it returns curr state
        with patch.object(self.thinker.word, "getState") as mock_getState:
            mock_getState.return_value = "__a_"
            self.assertEqual(self.thinker.think("a", [2]), "__a_")

        # check it error is raised
        with patch.object(self.thinker.word, "updateState") as mock_updateState:
            def updateState_raises_error(letter, positions):
                raise ValueError("Error from updateState()")

            mock_updateState.side_effect = updateState_raises_error

            with self.assertRaises(ValueError):
                self.thinker.think("a", [-10])

        # check if it is filtering
        self.thinker.think("a", [2])
        mock_filter_words.assert_called_with(self.thinker.dataset, "a", [2])


if __name__ == "__main__":
    unittest.main()
