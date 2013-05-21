#!/bin/bash

cat stage3part2output/* > ../classified-mapreduce.txt
python ../Utilities/diff.py ../classified-mapreduce.txt ../test-truth.txt
