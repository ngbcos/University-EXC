#!/usr/bin/python

# Reduces a set of (word, upper_prob, lower_prob) tuples
# into a single capitalized/non-capitalized output word, 
# based on the product of the probabilities.

from __future__ import division
import sys
import itertools

# Outputs the word, formatted according to the probabilities.
def outputWord(word, wordCount, lowerProb, upperProb):
  if (lowerProb >= upperProb):
    wordToOutput = word.lower()
  else:
    wordToOutput = word.capitalize()
  for _ in itertools.repeat(None, wordCount):
    print wordToOutput

def main():
  previousWord = None
  upperProb = 1.0
  lowerProb = 1.0
  wordCount = 0

  for line in sys.stdin:
    parts = line.strip().split()

    # Ignore empty lines.
    if not parts:
      continue

    word = parts[0].strip()

    if previousWord != None and word != previousWord:
      # A new word, so output the old one.
      outputWord(previousWord, wordCount, lowerProb, upperProb)
      upperProb = 1.0
      lowerProb = 1.0

    # Update the probabilities
    upperProb *= float(parts[1])
    lowerProb *= float(parts[2])
    wordCount = int(parts[3])
    previousWord = word

  # Now output the final word.
  outputWord(previousWord, wordCount, lowerProb, upperProb)

if __name__ == '__main__':
  main()
