import sys
import time
import datetime
import winsound
import winsound

# Some features to add.
# 1. Some basic stat on how many boxes today, week, month.
# 2. Number of goal acheived today, week, overall. 
# 3. Number of distractions 

FreqStart = 3500
FreqEnd= 1500
DurStart =500 
DurEnd =1000 

start_time = datetime.datetime.now()

# This should be in minutes
interval = 24
interval_td = datetime.timedelta(minutes=24)

target_time = start_time + interval_td

#print start_time
#print target_time

# This should be in seconds.
tick_time = 60

winsound.Beep(FreqStart,DurStart)
sys.stdout.write('------------------------')
sys.stdout.write('\r')
while target_time > datetime.datetime.now():
    time.sleep(tick_time)
    sys.stdout.write('+')
winsound.Beep(FreqEnd,DurEnd)

