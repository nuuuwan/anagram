from gig import Ent, EntType

from anagram.Anagram import Anagram

if __name__ == "__main__":
    anagram = Anagram()
    for ent_type in [
        # EntType.PROVINCE,
        EntType.DISTRICT,
        EntType.DSD,
        # EntType.GND,
    ]:
        ents = Ent.list_from_type(ent_type)
        n_matches = 0
        for ent in ents:
            anagrams = anagram.find_anagrams(ent.name)
            if anagrams:
                n_matches += 1
                print(ent.name, anagrams)

        print(f"{ent_type.name}: {n_matches} matches")
