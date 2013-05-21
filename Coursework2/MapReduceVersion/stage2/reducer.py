#!/usr/bin/python

# Reduces multiple tuples of a words features to a single set of 
# (feature, word, word_count) tuples (where "word" is unique between
# each set).

import sys

# Outputs the tuples for a word and it's features.
def outputTuples(word, features, wordCount):
  for feature in features:
    # Skip non-existant features.
    if feature is None or len(feature) == 0:
      continue

    # The "." is a marker for Stage 3.
    print feature + "\t" + word + "\t" + str(wordCount) + "\t."
  

def main():
  previousWord = None
  features = []
  wordCount = 0

  for line in sys.stdin:
    parts = line.rstrip("\n").split("\t")

    # Skip empty lines.
    if len(parts) == 0:
      continue;

    # The word and the first feature are the same (case insensitively).
    word = parts[0]

    if previousWord != None and word != previousWord:
      # A new word.
      outputTuples(previousWord, features, wordCount)
      wordCount = 0
    features = parts[0:5]
    wordCount += 1
    previousWord = word
  
  # Output the last word.
  outputTuples(previousWord, features, wordCount)

if __name__ == '__main__':
  main()
