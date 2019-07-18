An implementation of Hearst patterns for hyponyms in Python. [1] Now, extended to include more patterns from [2]!

By default, the library does not use the extended patterns (so it behaves like "classic" Hearst patterns). If you do want to use the extended pattern set, you initialize the constructor and set the extended paramter to True

```
h = HearstPatterns(extended = True)
```

The core API call is find_hyponyms(text) which will process the text and return the hyponyms in a list of tuples,
of the form (specific-term, general-term)

# Installation:

```
pip install hearstPatterns
```

# Installation notes:

## As of version 0.1.3:

The library now uses Spacy, so if you are using a prior version, please see the NLTK specific instructions below.

## Versin 0.1.2 and below:

Note that Hearst patterns rely on Noun Phrases, so we build our own simple chunker, and therefore leverage NLTK in order
to do the Part-of-Speech tagging. Therefore, there is a requirement on nltk (see requirements.txt)

Some users report needing to install specific components of NLTK after the inital install. Specifically, you might need to:

```
$ python
>>> import nltk
>> nltk.download('punkt')
>> nltk.download('averaged_perceptron_tagger')
```

# Testing:

```
python -m unittest discover
```

---
# References:

[1] Hearst, M. A. "Automatic acquisition of hyponyms from large text corpora." Proceedings of the 14th conference on Computational linguistics-Volume 2. Association for Computational Linguistics, 1992.

[2] Seitner, J., Bizer, C., Eckert, K., Faralli, S., Meusel, R., Paulheim, H., & Ponzetto, S. "A large database of hypernymy relations extracted from the web." Proceedings of the 10th edition of the Language Resources and Evaluation Conference, 2016.
