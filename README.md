An implementation of Hearst patterns for hyponyms in Python. [1] Now, extended to include more patterns from [2]!

I couldn't find a version in Python, so I wrote and released this one.

The core API call is find_hyponyms(text) which will process the text and return the hyponyms in a list of tuples,
of the form (specific-term, general-term)

It could certainly be optimized further for speed, etc. but I hope this release is useful to the community in general.

Note that Hearst patterns rely on Noun Phrases, so we build our own simple chunker, and therefore leverage NLTK in order
to do the Part-of-Speech tagging. Therefore, there is a requirement on nltk (see requirements.txt)

Installation:

```
pip install hearstPatterns
```

Installation notes:

Some users report needing to install specific components of NLTK after the inital install. Specifically, you might need to:

```
$ python
>>> import nltk
>> nltk.download('punkt')
>> nltk.download('averaged_perceptron_tagger')
```

Testing:

```
python -m unittest discover
```

ToDo:

* Speed it up
* Add lemmatization or stemming so that we are only outputting singular NPs
* NLTK pos-tags sometimes lead to issues, and chunker could certainly be improved

====
References:

[1] Hearst, M. A. "Automatic acquisition of hyponyms from large text corpora." Proceedings of the 14th conference on Computational linguistics-Volume 2. Association for Computational Linguistics, 1992.

[2] Seitner, J., Bizer, C., Eckert, K., Faralli, S., Meusel, R., Paulheim, H., & Ponzetto, S. "A large database of hypernymy relations extracted from the web." Proceedings of the 10th edition of the Language Resources and Evaluation Conference, 2016.