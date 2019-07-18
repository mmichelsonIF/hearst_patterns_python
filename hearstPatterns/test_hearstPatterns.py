import unittest
from hearstPatterns.hearstPatterns import HearstPatterns


class TestHearstPatterns(unittest.TestCase):

    def test_hyponym_finder(self):
        h = HearstPatterns(extended=True)

        # H1
        hyps1 = h.find_hyponyms("Forty-four percent of patients with uveitis had one or more identifiable signs or symptoms, such as red eye, ocular pain, visual acuity, or photophobia, in order of decreasing frequency.")

        self.assertEqual(tuple(map(str.lower, hyps1[0])), ("red eye", "symptom"))
        self.assertEqual(tuple(map(str.lower, hyps1[1])), ("ocular pain", "symptom"))
        self.assertEqual(tuple(map(str.lower, hyps1[2])), ("visual acuity", "symptom"))
        self.assertEqual(tuple(map(str.lower, hyps1[3])), ("photophobia", "symptom"))

        # H2
        hyps2 = h.find_hyponyms("There are works by such authors as Herrick, Goldsmith, and Shakespeare.")
        self.assertEqual(tuple(map(str.lower, hyps2[0])), ("herrick", "author"))
        self.assertEqual(tuple(map(str.lower, hyps2[1])), ("goldsmith", "author"))
        self.assertEqual(tuple(map(str.lower, hyps2[2])), ("shakespeare", "author"))

        # H3
        hyps3 = h.find_hyponyms("There were bruises, lacerations, or other injuries were not prevalent.")
        self.assertEqual(tuple(map(str.lower, hyps3[0])), ("bruise", "injury"))
        self.assertEqual(tuple(map(str.lower, hyps3[1])), ("laceration", "injury"))

        # H4
        hyps4 = h.find_hyponyms("common law countries, including Canada, Australia, and England enjoy toast.")
        self.assertEqual(tuple(map(str.lower, hyps4[0])), ("canada", "common law country"))
        self.assertEqual(tuple(map(str.lower, hyps4[1])), ("australia", "common law country"))
        self.assertEqual(tuple(map(str.lower, hyps4[2])), ("england", "common law country"))

        # H5
        hyps5 = h.find_hyponyms("Many countries, especially France, England and Spain also enjoy toast.")
        self.assertEqual(tuple(map(str.lower, hyps5[0])), ("france", "country"))
        self.assertEqual(tuple(map(str.lower, hyps5[1])), ("england", "country"))
        self.assertEqual(tuple(map(str.lower, hyps5[2])), ("spain", "country"))

        # H2
        hyps6 = h.find_hyponyms("There are such benefits as postharvest losses reduction, food increase and soil fertility improvement.")
        self.assertEqual(tuple(map(str.lower, hyps6[0])), ("postharvest loss reduction", "benefit"))
        self.assertEqual(tuple(map(str.lower, hyps6[1])), ("food increase", "benefit"))
        self.assertEqual(tuple(map(str.lower, hyps6[2])), ("soil fertility improvement", "benefit"))

        # H'1
        hyps7 = h.find_hyponyms("Fruits, i.e. , apples, bananas, oranges and peaches.")
        self.assertEqual(tuple(map(str.lower, hyps7[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[3])), ("peach", "fruit"))

        hyps7 = h.find_hyponyms("Fruits, e.g. apples, bananas, oranges and peaches.")
        self.assertEqual(tuple(map(str.lower, hyps7[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps7[3])), ("peach", "fruit"))

        # H'2

        hyps10 = h.find_hyponyms("Fruits (e.g. apples, bananas, oranges and peaches.)")
        self.assertEqual(tuple(map(str.lower, hyps10[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[3])), ("peach", "fruit"))

        hyps10 = h.find_hyponyms("Fruits (i.e. apples, bananas, oranges and peaches.)")
        self.assertEqual(tuple(map(str.lower, hyps10[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps10[3])), ("peach", "fruit"))

        # H'3
        hyps8 = h.find_hyponyms("Fruits, for example apples, bananas, oranges and peaches.")
        self.assertEqual(tuple(map(str.lower, hyps8[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps8[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps8[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps8[3])), ("peach", "fruit"))

        # H'4
        hyps9 = h.find_hyponyms("Fruits, which may include apples, bananas, oranges and peaches.")
        self.assertEqual(tuple(map(str.lower, hyps9[0])), ("apple", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps9[1])), ("banana", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps9[2])), ("orange", "fruit"))
        self.assertEqual(tuple(map(str.lower, hyps9[3])), ("peach", "fruit"))


if __name__ == '__main__':
    unittest.main()
