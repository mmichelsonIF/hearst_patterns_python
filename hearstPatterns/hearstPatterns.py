import re
import string
import nltk
from nltk.tag.perceptron import PerceptronTagger

class HearstPatterns(object):

	def __init__(self):
		self.__chunk_patterns = r""" #  helps us find noun phrase chunks
 				NP: {<DT|PP\$>?<JJ>*<NN>+}
 					{<NNP>+}
 					{<NNS>+}
		"""

		self.__np_chunker = nltk.RegexpParser(self.__chunk_patterns) # create a chunk parser 

		# now define the Hearst patterns
		# format is <hearst-pattern>, <general-term>
		# so, what this means is that if you apply the first pattern, the firsr Noun Phrase (NP)
		# is the general one, and the rest are specific NPs
		self.__hearst_patterns = [
			("(NP_\w+ (, )?such as (NP_\w+ ? (, )?(and |or )?)+)", "first"),
			("(such NP_\w+ (, )?as (NP_\w+ ?(, )?(and |or )?)+)", "first"),
			("((NP_\w+ ?(, )?)+(and |or )?other NP_\w+)", "last"),
			("(NP_\w+ (, )?including (NP_\w+ ?(, )?(and |or )?)+)", "first"),
			("(NP_\w+ (, )?especially (NP_\w+ ?(, )?(and |or )?)+)", "first"),
		]

		self.__pos_tagger = PerceptronTagger()
		
	def prepare(self, rawtext):
		sentences = nltk.sent_tokenize(rawtext.strip()) # NLTK default sentence segmenter
		sentences = [nltk.word_tokenize(sent) for sent in sentences] # NLTK word tokenizer
		sentences = [self.__pos_tagger.tag(sent) for sent in sentences] # NLTK POS tagger

		return sentences

	def chunk(self, rawtext):
		sentences = self.prepare(rawtext.strip())

		all_chunks = []
		for sentence in sentences:
			chunks = self.__np_chunker.parse(sentence) # parse the example sentence
			#for chunk in chunks:
			#	print str(chunk)
			all_chunks.append(self.prepare_chunks(chunks))
		return all_chunks

	def prepare_chunks(self, chunks):
		# basically, if the chunk is NP, keep it as a string taht starts w/ NP and replace " " with _
		# otherwise, keep the word.
		# remove punct
		# this is all done to make it super easy to apply the Hearst patterns...

		terms = []
		for chunk in chunks:
			label = None
			try: # gross hack to see if the chunk is simply a word or a NP, as we want. But non-NP fail on this method call
				label = chunk.label()
			except:
				pass

			if label is None: #means one word...
				token = chunk[0]
				pos = chunk[1]
				if pos in ['.', ':', '-', '_']:
					continue
				terms.append(token)
			else:
				np = "NP_"+"_".join([a[0] for a in chunk]) #This makes it easy to apply the Hearst patterns later
				terms.append(np)
		return ' '.join(terms)

	"""
		This is the main entry point for this code.
		It takes as input the rawtext to process and returns a list of tuples (specific-term, general-term)
		where each tuple represents a hypernym pair.

	"""
	def find_hyponyms(self, rawtext):

		hyponyms = []
		np_tagged_sentences = self.chunk(rawtext)

		for raw_sentence in np_tagged_sentences:
			# two or more NPs next to each other should be merged into a single NP, it's a chunk error

			# find any N consecutive NP_ and merge them into one...
			# So, something like: "NP_foo NP_bar blah blah" becomes "NP_foo_bar blah blah"
			sentence = re.sub(r"(NP_\w+ NP_\w+)+", lambda m: m.expand(r'\1').replace(" NP_", "_"), raw_sentence)

			for (hearst_pattern, parser) in self.__hearst_patterns:
				matches = re.search(hearst_pattern, sentence)
				if matches:
					match_str = matches.group(0)

					nps = [a for a in match_str.split() if a.startswith("NP_")]

					if parser == "first":
						general = nps[0]
						specifics = nps[1:]
					else:
						general = nps[-1]
						specifics = nps[:-1]
						print str(general)
						print str(nps)

					for i in range(len(specifics)):
						#print "%s, %s" % (specifics[i], general)
						hyponyms.append((self.clean_hyponym_term(specifics[i]), self.clean_hyponym_term(general)))

		return hyponyms


	def clean_hyponym_term(self, term):
		# good point to do the stemming or lemmatization
		return term.replace("NP_","").replace("_", " ")

