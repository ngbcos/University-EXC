#!/usr/bin/python

# The built in Hadoop IdentityMapper doesn't work for some reason, so
# I'm using a custom one instead. It's probably my fault.

import sys

def main():
  for line in sys.stdin:
    print line.strip()

if __name__ == '__main__':
  main()
