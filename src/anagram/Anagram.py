from functools import cached_property


class Anagram:
    @cached_property
    def words(self):
        return set(
            word.strip().lower()
            for word in open("data/words.txt")
            if len(word.strip()) >= 4
        )

    @cached_property
    def pattern_to_words(self):
        pattern_to_words = {}
        for word in self.words:
            pattern = self._pattern(word)
            if pattern not in pattern_to_words:
                pattern_to_words[pattern] = set()
            pattern_to_words[pattern].add(word)
        return pattern_to_words

    def find_anagrams(self, word):
        pattern = self._pattern(word)
        candidates = tuple(
            sorted(
                (candidate, candidate_pattern)
                for candidate_pattern, words in self.pattern_to_words.items()
                if self._subtract_pattern(pattern, candidate_pattern)
                is not None
                for candidate in words
                if len(candidate) >= 2
            )
        )
        return self._find_phrases(pattern, candidates, 0, {})

    def _find_phrases(self, remaining, candidates, start, memo):
        key = (remaining, start)
        if key in memo:
            return memo[key]
        phrases = set()
        for index in range(start, len(candidates)):
            word, pattern = candidates[index]
            phrases.update(
                self._candidate_phrases(
                    remaining, candidates, index, word, pattern, memo
                )
            )
        memo[key] = phrases
        return phrases

    def _candidate_phrases(
        self, remaining, candidates, index, word, pattern, memo
    ):
        remainder = self._subtract_pattern(remaining, pattern)
        if remainder is None:
            return set()
        if not remainder:
            return {word}
        return {
            f"{word} {phrase}"
            for phrase in self._find_phrases(
                remainder, candidates, index, memo
            )
        }

    def _pattern(self, text):
        return "".join(sorted(char for char in text.lower() if char.isalpha()))

    def _subtract_pattern(self, pattern, subpattern):
        remaining = list(pattern)
        for char in subpattern:
            try:
                remaining.remove(char)
            except ValueError:
                return None
        return "".join(remaining)
