#!/bin/bash
DEFAULT_DELAY=0
if [ "x$1" = "x" -o "x$1" = "xnone" ]; then
   DELAY=$DEFAULT_DELAY
else
   DELAY=$1
fi
sleep $DELAY
cd /home/dm
su dm -c "./overclock_gpus.sh"
su dm -c "screen -dmS fans ./fan_control.py"
su dm -c "./mine.sh"
su dm -c "pm2 start ~/Code/miner-monitor/src/main.js"
