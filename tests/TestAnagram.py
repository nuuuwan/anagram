import unittest

from anagram.Anagram import Anagram


class TestAnagram(unittest.TestCase):
    def test_finds_multiple_word_anagram(self):
        anagram = Anagram()
        anagram.words = {"moon", "starer"}

        self.assertEqual({"moon starer"}, anagram.find_anagrams("Astronomer"))

    def test_excludes_one_character_words(self):
        anagram = Anagram()
        anagram.words = {"a", "aa"}

        self.assertEqual({"aa"}, anagram.find_anagrams("aa"))
