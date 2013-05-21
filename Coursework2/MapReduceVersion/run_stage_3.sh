#!/bin/bash

# Part 1

hadoop fs -rmr /user/s0840449/data/output/stage3part1

hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input /user/s0840449/data/output/stage1 \
  -input /user/s0840449/data/output/stage2 \
  -output /user/s0840449/data/output/stage3part1 \
  -mapper mapper.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage3/mapper.py \
  -reducer reducer1.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage3/reducer1.py 

if [[ $? != 0 ]]; then
  echo "Error!"
  exit 1
fi

# Copy to local for debug.
rm -rf stage3part1output
hadoop fs -copyToLocal /user/s0840449/data/output/stage3part1 ./stage3part1output

# Part 2

hadoop fs -rmr /user/s0840449/data/output/stage3part2

hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input /user/s0840449/data/output/stage3part1 \
  -output /user/s0840449/data/output/stage3part2 \
  -mapper mapper.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage3/mapper.py \
  -reducer reducer2.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage3/reducer2.py 

# Copy to local for stage 4.
rm -rf stage3part2output
hadoop fs -copyToLocal /user/s0840449/data/output/stage3part2 ./stage3part2output
