#!/bin/bash

hadoop fs -rmr /user/s0840449/data/output/stage2

hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input /user/s0840449/data/input/stage2 \
  -output /user/s0840449/data/output/stage2 \
  -mapper mapper.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage2/mapper.py \
  -reducer reducer.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage2/reducer.py \

# Copy to local for debug.
rm -rf stage2output
hadoop fs -copyToLocal /user/s0840449/data/output/stage2 ./stage2output

