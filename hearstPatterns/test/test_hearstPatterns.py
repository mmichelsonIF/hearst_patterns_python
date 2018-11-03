import unittest
from hearstPatterns.hearstPatterns import HearstPatterns

class TestHearstPatterns(unittest.TestCase):

	def test_hyponym_finder(self):
		h = HearstPatterns()
		hyps1 =  h.find_hyponyms("Forty-four percent of patients with uveitis had one or more identifiable signs or symptoms, such as red eye, ocular pain, visual acuity, or photophobia, in order of decreasing frequency.")

		self.assertEqual(hyps1[0], ("red eye", "symptoms"))
		self.assertEqual(hyps1[1], ("ocular pain", "symptoms"))
		self.assertEqual(hyps1[2], ("visual acuity", "symptoms"))
		self.assertEqual(hyps1[3], ("photophobia", "symptoms"))

		hyps2 = h.find_hyponyms("There are works by such authors as Herrick, Goldsmith, and Shakespeare.")
		self.assertEqual(hyps2[0], ("Herrick", "authors"))
		self.assertEqual(hyps2[1], ("Goldsmith", "authors"))
		self.assertEqual(hyps2[2], ("Shakespeare", "authors"))
	
		hyps3 = h.find_hyponyms("There were bruises, lacerations, or other injuries were not prevalent.")
		self.assertEqual(hyps3[0], ("bruises", "injuries"))
		self.assertEqual(hyps3[1], ("lacerations", "injuries"))

		hyps4 =  h.find_hyponyms("common law countries, including Canada, Australia, and England enjoy toast.")
		self.assertEqual(hyps4[0], ("Canada", "common law countries"))
		self.assertEqual(hyps4[1], ("Australia", "common law countries"))
		self.assertEqual(hyps4[2], ("England", "common law countries"))

		hyps5 = h.find_hyponyms("Many countries, especially France, England and Spain also enjoy toast.")
		self.assertEqual(hyps5[0], ("France", "countries"))
		self.assertEqual(hyps5[1], ("England", "countries"))
		self.assertEqual(hyps5[2], ("Spain", "countries"))

		hyps6 = h.find_hyponyms("There are such benefits as postharvest losses reduction, food increase and soil fertility improvement.")
		self.assertEqual(hyps6[0], ("postharvest losses reduction", "benefits"))
		self.assertEqual(hyps6[1], ("food increase", "benefits"))
		self.assertEqual(hyps6[2], ("soil fertility improvement", "benefits"))

if __name__ == '__main__':
    unittest.main()