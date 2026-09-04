from anagram.Anagram import Anagram

if __name__ == "__main__":
    while True:
        word = input("Enter a word: ")
        anagrams = Anagram().find_anagrams(word)
        print(anagrams)
        print("...")
