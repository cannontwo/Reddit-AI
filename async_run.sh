#!/bin/bash
nohup python -u ./bot.py > bot.log &
echo $! > save_pid.log
echo $!
