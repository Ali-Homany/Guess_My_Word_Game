import unittest
from unittest.mock import patch
import main


class TestMain(unittest.TestCase):
    @patch("builtins.input")
    def test_get_word_length(self, mock_input):
        mock_input.side_effect = ["2", "3", "5"]
        self.assertEqual(main.get_word_length(), 5)

        mock_input.side_effect = ["abc", "1%", "4"]
        self.assertEqual(main.get_word_length(), 4)

        mock_input.side_effect = ["25", "15"]
        self.assertEqual(main.get_word_length(), 15)

    def test_is_word_guessed(self):
        self.assertEqual(main.is_word_guessed("hello"), True)
        self.assertEqual(main.is_word_guessed("he_lo"), False)

    @patch("builtins.input")
    def test_get_positions(self, mock_input):
        mock_input.side_effect = ["1 3 5 7 9"]
        expected_result = [0, 2, 4, 6, 8]
        self.assertEqual(main.get_positions(), expected_result)

    @patch("builtins.input")
    def test_right_guess(self, mock_input):
        mock_input.side_effect = ["a", "16272", "yyy", "y"]
        self.assertEqual(main.right_guess("s"), True)

        mock_input.side_effect = ["a", "16272", "N", "y"]
        self.assertEqual(main.right_guess("a"), False)

    @patch("builtins.input")
    @patch("main.data.learn_word")
    def test_handle_game_end(self, mock_learn_word, mock_input):
        mock_input.side_effect = ["grasp"]
        main.handle_game_end(5)
        mock_learn_word.assert_called_once_with("grasp")

        mock_learn_word.reset_mock()

        mock_input.side_effect = ["friend", "grape"]
        main.handle_game_end(5)
        mock_learn_word.assert_called_once_with("grape")


if __name__ == "__main__":
    unittest.main()
