import unittest
from hearstPatterns.hearstPatterns import HearstPatterns

class TestHearstPatterns(unittest.TestCase):

	def test_hyponym_finder(self):
		h = HearstPatterns()
		hyps1 =  h.find_hyponyms("Forty-four percent of patients with uveitis had one or more identifiable signs or symptoms, such as red eye, ocular pain, visual acuity, or photophobia, in order of decreasing frequency.")

		self.assertEqual(hyps1[0], ("red eye", "symptom"))
		self.assertEqual(hyps1[1], ("ocular pain", "symptom"))
		self.assertEqual(hyps1[2], ("visual acuity", "symptom"))
		self.assertEqual(hyps1[3], ("photophobia", "symptom"))

		hyps2 = h.find_hyponyms("There are works by such authors as Herrick, Goldsmith, and Shakespeare.")
		self.assertEqual(hyps2[0], ("herrick", "author"))
		self.assertEqual(hyps2[1], ("goldsmith", "author"))
		self.assertEqual(hyps2[2], ("shakespeare", "author"))
	
		hyps3 = h.find_hyponyms("There were bruises, lacerations, or other injuries were not prevalent.")
		self.assertEqual(hyps3[0], ("bruise", "injury"))
		self.assertEqual(hyps3[1], ("laceration", "injury"))

		hyps4 =  h.find_hyponyms("common law countries, including Canada, Australia, and England enjoy toast.")
		self.assertEqual(hyps4[0], ("canada", "common law country"))
		self.assertEqual(hyps4[1], ("australia", "common law country"))
		self.assertEqual(hyps4[2], ("england", "common law country"))

		hyps5 = h.find_hyponyms("Many countries, especially France, England and Spain also enjoy toast.")
		self.assertEqual(hyps5[0], ("france", "country"))
		self.assertEqual(hyps5[1], ("england", "country"))
		self.assertEqual(hyps5[2], ("spain", "country"))

		hyps6 = h.find_hyponyms("There are such benefits as postharvest losses reduction, food increase and soil fertility improvement.")
		self.assertEqual(hyps6[0], ("postharvest loss reduction", "benefit"))
		self.assertEqual(hyps6[1], ("food increase", "benefit"))
		self.assertEqual(hyps6[2], ("soil fertility improvement", "benefit"))

if __name__ == '__main__':
    unittest.main()
