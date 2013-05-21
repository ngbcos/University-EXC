#!/usr/bin/python

# Maps the training data to (feature, upper_count, lower_count) entries.

import sys
import re

#maxSize = 15000

# Checks for uppercase characters.
# Note from the coursework description:
# "any mixed cased words in the test data should be assumed to be just 
# upper-case initial"
uppercaseReg = re.compile("[A-Z]")

# Returns the last N letters of a string, or None if the string is
# too short.
def getLastNLetters(string, n):
  if len(string) < n:
    return None
  return string[-n:].lower()

# Returns the first N letters of a string, or None if the string is
# too short.
def getFirstNLetters(string, n):
  if len(string) < n:
    return None
  return string[:n].lower()

# Outputs the (feature, upper_count, lower_count) entries from a map.
def outputMap(map):
  for key, value in map.items():
    print key + "\t" + str(value[0]) + "\t" + str(value[1])

def main():
  featuresMap = {}
  for line in sys.stdin:
    words = line.strip().split()
    for word in words:
      features = []
      features.append(word.lower())
      features.append(getLastNLetters(word, 2))
      features.append(getLastNLetters(word, 3))
      features.append(getFirstNLetters(word, 2))
      features.append(getFirstNLetters(word, 3))

      for feature in features:
        # Skip empty features.
        if feature is None:
          continue

        # Add the feature to the map if it is not already there.
        if feature not in featuresMap:
          featuresMap[feature] = [0,0]

        if re.search(uppercaseReg, word):
          featuresMap[feature][0] += 1
        else:
          featuresMap[feature][1] += 1

      # Make sure that the featuresMap doesnt get too big.
      # Removed because it's too slow.
      #if len(featuresMap) > maxSize:
      #  outputMap(featuresMap)
      #  featuresMap = {}

  outputMap(featuresMap)

if __name__ == '__main__':
  main()
