#!/usr/bin/python

# Reduces tuples of (feature, upper_count, lower_count) to one
# tuple of (feature, upper_prob, lower_prob) per feature.

# Use float division by default.
from __future__ import division

import sys

# Outputs the tuple of (feature, upper_prob, lower_prob).
def outputTuple(feature, upperCount, lowerCount):
  upperProb = upperCount / (upperCount + lowerCount)
  lowerProb = lowerCount / (upperCount + lowerCount)
  print feature + "\t" + str(upperProb) + "\t" + str(lowerProb)

def main():
  previousFeature = None
  upperCount = 0.0
  lowerCount = 0.0

  for line in sys.stdin:
    parts = line.strip().split()
    feature = parts[0]

    if previousFeature != None and feature != previousFeature:
      # New feature - output the probabilities.
      outputTuple(previousFeature, upperCount, lowerCount)
      upperCount = 0.0
      lowerCount = 0.0

    # Update the counters.
    upperCount += float(parts[1])
    lowerCount += float(parts[2])
    previousFeature = feature

  # Now output the last feature.
  outputTuple(previousFeature, upperCount, lowerCount)

if __name__ == '__main__':
  main()
