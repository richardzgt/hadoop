#!/bin/bash

#purpose to put up hdfs file
#hdfs://192.168.102.36:9000/user/ecp/yiliao_ap
HD_DIR="/usr/local/hadoop-1.2.1"
HD_BIN="$HD_DIR/bin/hadoop"
LOCAL_DIR="/app2/yiliao-app/log/app-server"
PUTED_FILE="$LOCAL_DIR/.HDFS_puted.txt"
current_date=$(date +%Y%m%d)

[ -f "$PUTED_FILE" ] || (touch $PUTED_FILE) 
[ ! -d "$HD_DIR" ] && (echo "not of HD_DIR") && exit 1

#工作目录环境，造成其他很多问题
cd $LOCAL_DIR

function putup()
{
    #进入目录
    
	$HD_BIN dfs -test -e hdfs://192.168.102.36:9000/user/ecp/yiliao_app/$current_date
if [ $? -ne 0 ] ;then
	$HD_BIN dfs -mkdir hdfs://192.168.102.36:9000/user/ecp/yiliao_app/$current_date
	[ $? -ne 0 ] && (echo "can't create yiliaoapp_DIR") && exit 1
fi
	$HD_BIN dfs -put $1 hdfs://192.168.102.36:9000/user/ecp/yiliao_app/$current_date/$2
	[ $? -ne 0 ] && ( echo "put error!" ) && exit 2
    echo $2,"upload ok"
}


for i in $(ls app.info.log.[0-9]*)
do
	# 空串,已经记录没有上传过，那就执行putup
	if [ -z "$(grep $i $PUTED_FILE)" ] ;then
        filename=${i##*/}
        # putup "123.txt" "123.txt_app1" 
        putup "$filename" "$filename"_"$(hostname)"
        [ $? -eq 0 ] && (echo $filename >> $PUTED_FILE)
	fi

done

