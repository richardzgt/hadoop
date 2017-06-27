#!/bin/bash

../bin/hadoop jar /usr/local/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-input /user/ecp/yiliao_app/20151009 \
-output /output/word2 \
-mapper app_mapper1.py \
-combiner app_combiner.py \
-reducer app_reducer.py \
-file app_mapper.py \
-file app_combiner.py \
-file app_reducer.py