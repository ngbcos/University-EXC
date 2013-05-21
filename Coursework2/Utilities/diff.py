#!/usr/bin/python

import sys

def main(args):
  if len(args) < 3:
    print "Usage: python diff.py actualFile expectedFile"
    sys.exit(1)

  # Read both files into memory, to avoid opening them multiple times.
  actualWords = []
  expectedWords = []

  f = open(args[1], "r")
  for line in f:
    actualWords.append(line.strip())
  f.close()

  f = open(args[2], "r")
  for line in f:
    expectedWords.append(line.strip())
  f.close()

  matches = 0 
  fails = 0
  actualWords = filter(lambda x : len(x) > 0, actualWords)
  expectedWords = filter(lambda x : len(x) > 0, expectedWords)
  for expectedWord in expectedWords:
    matchFound = False
    for actualWord in actualWords[:]:
      if expectedWord[0] == actualWord[0] and expectedWord.lower() == actualWord.lower():
        print "Matched expected word '" + expectedWord + "' to actual word '" + actualWord + "'"
        matches += 1
        matchFound = True
        actualWords.remove(actualWord)
        break
    if not matchFound:
      print "No match found for '" + expectedWord+ "'"
      fails += 1

  accuracy = (float(matches) / float(matches + fails)) * 100 
  print "Matches: " + str(matches) + ", Fails: " + str(fails)
  print ("Accuracy: %.2f" % accuracy)

if __name__ == '__main__':
  main(sys.argv)
