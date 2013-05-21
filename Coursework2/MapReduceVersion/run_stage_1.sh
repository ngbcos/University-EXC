#!/bin/bash

hadoop fs -rmr /user/s0840449/data/output/stage1

hadoop jar /opt/hadoop/hadoop-0.20.2/contrib/streaming/hadoop-0.20.2-streaming.jar \
  -input /user/s0840449/data/input/stage1 \
  -output /user/s0840449/data/output/stage1 \
  -mapper mapper.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage1/mapper.py \
  -reducer reducer.py \
  -file ~/Documents/Coursework/EXC-Coursework/MapReduceVersion/stage1/reducer.py 

# Copy to local for debug.
rm -rf stage1output
hadoop fs -copyToLocal /user/s0840449/data/output/stage1 ./stage1output
