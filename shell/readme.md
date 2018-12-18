```
sh_name=`basename $0`
CNT=`ps -ef | grep ${sh_name} | grep -v grep | wc -l`
if [ ${CNT} -gt 2 ]; then
	log_print "check is up"
	exit 1
fi
```
