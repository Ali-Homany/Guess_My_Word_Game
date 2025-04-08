import unittest
from unittest.mock import patch, mock_open
import utils.data as data


class TestData(unittest.TestCase):
    @patch("builtins.open", new_callable=mock_open, read_data="hello\nwater\nscience")
    def test_read_dataset_for_length(self, mock_open_file):
        word_length = 5
        expected_dataset = ["hello", "water", "science"]
        mock_open.return_value = expected_dataset

        result = data.read_dataset_for_length(word_length)

        self.assertEqual(result, expected_dataset)
        mock_open_file.assert_called_once_with(f"Dataset/word_dataset_length_{word_length}_size_6040.txt", "r")

    @patch("builtins.open", new_callable=mock_open, read_data="hello\nwater\nscience\ncrazy")
    @patch("data.os.rename")
    def test_learn_word(self, mock_os_rename, mock_open_file):
        # check that it doesn't append word if it already exists there
        word = "crazy"
        data.learn_word(word=word)
        mock_open_file.assert_called_with(f"Dataset/word_dataset_length_{len(word)}_size_6040.txt", "a")
        mock_open_file.return_value.__enter__().write.assert_not_called()
        mock_os_rename.assert_not_called()

        mock_open_file.reset_mock()
        mock_os_rename.reset_mock()

        word = "fruit"
        data.learn_word(word=word)
        mock_open_file.assert_called_once_with(f"Dataset/word_dataset_length_{len(word)}_size_6040.txt", "a")
        mock_os_rename.assert_called_once_with(f"Dataset/word_dataset_length_{len(word)}_size_6040.txt",
                                               f"Dataset/word_dataset_length_{len(word)}_size_6041.txt")
        mock_open_file.return_value.__enter__().write.assert_called_once_with(word + "\n")

    @patch("data.getPattern")
    @patch("data.isPattern")
    def test_filter_words(self, mock_isPattern, mock_getPattern):
        mock_getPattern.return_value = "pattern"
        dataset = ["hello", "water", "science"]

        letter = "e"
        positions = [3]

        mock_isPattern.side_effect = lambda word, pattern: word[3] == "e"
        result = data.filter_words(dataset, letter, positions)
        expected_result = ["water", "science"]

        mock_getPattern.assert_called_once_with(len(dataset[0]), letter, positions)
        self.assertEqual(result, expected_result, "result is wrong, not as expected")

        mock_getPattern.reset_mock()
        mock_isPattern.reset_mock()

        letter = "c"
        positions = []

        mock_isPattern.side_effect = lambda word, pattern: "c" not in word
        result = data.filter_words(dataset, letter, positions)
        expected_result = ["hello", "water"]

        mock_getPattern.assert_called_once_with(len(dataset[0]), letter, positions)
        self.assertEqual(result, expected_result, "result is wrong, not as expected")


if __name__ == "__main__":
    unittest.main()
