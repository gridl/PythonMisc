import sched
import time
from datetime import datetime, timedelta

# create a scheduler instance
scheduler = sched.scheduler(timefunc=time.time)

# workfunction
def saytime():
    print(time.ctime())
    # 10 second delay
    scheduler.enter(10,priority=0, action=saytime)

saytime()
try:
    # scheuler is started with run (blocking= true)
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped')

