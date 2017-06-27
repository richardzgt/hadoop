#!/bin/bash

# 20151012_1225   1200
# 20151012_1226   1128
# 20151012_1227   1162
# 20151012_1228   1202
# 20151012_1229   1230
# 20151012_1230   1196
# 应该没意义，因为有些在线用户是不发信令的，这时候就统计不到
#key-value 20150928_1259 05977538669@ecplive.com
current_date=$(date +%Y%m%d)

#-input /user/ecp/yiliao_app/$current_date
#test dir /user/ecp/test
#log dir /user/ecp/yiliao_app/20151009
../bin/hadoop jar /usr/local/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-input /user/ecp/yiliao_app/20151009 \
-output /user/ecp/output/$current_date"_"$$ \
--jobconf mapred.map.tasks=1 \
--jobconf mapred.reduce.tasks=1 \
-mapper app_mapper1.py \
-reducer app_reducer1.py \
-file app_mapper1.py \
-file app_reducer1.py


#参数中间文件，然后再mapper合并"排序" key，reducer合并
#key 20150928_1259_05977538669@ecplive.com
../bin/hadoop dfs -test -e /user/ecp/output/$current_date"_"$$/part-00000
[ $? -ne 0 ] && echo "misstake appread" && exit 2
../bin/hadoop jar /usr/local/hadoop-1.2.1/contrib/streaming/hadoop-streaming-1.2.1.jar \
-input /user/ecp/output/$current_date"_"$$ \
-output /user/ecp/output/$current_date"_"$$"_final" \
--jobconf mapred.map.tasks=1 \
--jobconf mapred.reduce.tasks=1 \
-mapper app_mapper2.py \
-reducer app_reducer2.py \
-file app_mapper2.py \
-file app_reducer2.py

#clean files
if [ $? -eq 0 ]; then
    ../bin/hadoop dfs -rmr /user/ecp/output/$current_date"_"$$
fi 

