#!/usr/bin/python

# Maps the test data to tuples of (feature1, feature2, 
# feature3, feature4, feature5).
#
# Note feature1 (roughly) equals word.

import sys

# Returns the last N letters of a string, or None if the string is
# too short.
def getLastNLetters(string, n):
  if len(string) < n:
    return ""
  return string[-n:].lower()

# Returns the first N letters of a string, or None if the string is
# too short.
def getFirstNLetters(string, n):
  if len(string) < n:
    return ""
  return string[:n].lower()

def main():
  for line in sys.stdin:
    word = line.strip()

    # Extract the features and print them
    output_string = "\t".join([word.lower(),
                     getLastNLetters(word, 2),
                     getLastNLetters(word, 3),
                     getFirstNLetters(word, 2),
                     getFirstNLetters(word, 3)])
    print output_string

if __name__ == '__main__':
  main()
