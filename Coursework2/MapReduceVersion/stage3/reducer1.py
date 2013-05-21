#!/usr/bin/python

# Reduces the data from the model - tuples of
# (feature, upper_prob, lower_prob) - and the 
# training data - tuples of (feature, word) -
# to a set of (word, probability) tuples.
#
# There may be multiple (word, probability) tuples per word.

from __future__ import division
import sys
import exceptions

# Outputs the word tuples.
def outputWords(wordsToClassify, upperProb, lowerProb):
  for wordToClassify, wordCount in wordsToClassify:
    print wordToClassify + "\t" + str(upperProb) + "\t" + str(lowerProb) + "\t" + str(wordCount)

def main():
  previousFeature = None
  upperProb = None
  lowerProb = None
  wordsToClassify = []

  for line in sys.stdin:
    parts = line.strip().split()

    # Skip empty lines.
    if not parts:
      continue

    # The feature is always the first element of an input tuple.
    feature = parts[0]

    if previousFeature != None and feature != previousFeature:
      # A new feature. Output the set of words for the previous one, unless
      # there was no data from the model.
      if (lowerProb is not None or upperProb is not None):
        outputWords(wordsToClassify, upperProb, lowerProb)
      upperProb = None
      lowerProb = None
      wordsToClassify = []

    if len(parts) == 3:
      # The (feature, upper_prob, lower_prob) tuple.
      upperProb = float(parts[1])
      lowerProb = float(parts[2])
    elif len(parts) == 4:
      # A (feature, word, count, placeholder) tuple. 
      # The placeholder is ignored.
      wordsToClassify.append([parts[1], parts[2]])
    previousFeature = feature

  # Now output the final feature.
  if (lowerProb is not None or upperProb is not None):
    outputWords(wordsToClassify, upperProb, lowerProb)

if __name__ == '__main__':
  main()
