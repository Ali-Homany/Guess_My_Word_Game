import re
import unittest
from unittest.mock import patch
from utils.word import Word_Manager


class TestWordManager(unittest.TestCase):
    def setUp(self) -> None:
        self.word = Word_Manager(5)
        self.assertEqual(self.word.wordState, ["_", "_", "_", "_", "_"])

    def test_getState(self):
        self.assertEqual(self.word.getState(), "_____")
        self.word.wordState = ["a", "_", "c", "_", "b"]
        self.assertEqual(self.word.getState(), "a_c_b")

    def test_updateState(self):
        self.word.updateState("a", [0])
        self.assertEqual(self.word.wordState, ["a", "_", "_", "_", "_"])
        with self.assertRaises(ValueError):
            self.word.updateState("a", [-10, 1])
            self.word.updateState("a", [100, 1])
            self.word.wordState = ["a", "_", "_", "_", "_"]
            self.word.updateState("b", [0, 1])

    @patch("word.re.compile")
    def test_getPattern(self, mock_compile):
        mock_compile.return_value = "a____"

        self.assertEqual(self.word.getPattern("a", [], 5), "a____")
        mock_compile.assert_called_once_with("[^a]{5}")

        mock_compile.reset_mock()

        self.assertEqual(self.word.getPattern("a", [0, 3], 5), "a____")
        mock_compile.assert_called_once_with("a..a.")



if __name__ == "__main__":
    unittest.main()
