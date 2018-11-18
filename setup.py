from setuptools import setup, find_packages

setup(name = "hearstPatterns",
      version = "0.1.3",
      description = 'This is an implementation of Hearst patterns, for finding hyponyms, written in Python.',
      url = 'https://github.com/mmichelsonIF/hearst_patterns_python',
      author = 'mmichelsonIF',
      author_email = 'mmichelson@inferlink.com',
      license='Apache License 2.0',
      packages = find_packages(),
      install_requires=[
          'spacy',
      ],
)
