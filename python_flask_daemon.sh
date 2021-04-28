#!/bin/bash
interval=10	# 间隔10s检测一次
for ((i=0;i<60;i=(i+interval)));do
process_num=`ps -ef |grep -w "python app.py"|grep -v grep | wc -l`
if [ $process_num -eq 0  ]; then
	echo "flask not running, now start it"
	cd /opt/flask_aging
	python app.py
elif [ $process_num -gt 0  ]; then
	echo "flask is ok"
fi
date
sleep $interval
done
exit 0 
