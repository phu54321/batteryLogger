import psutil
import datetime
import os
import time

def logTask():
    wpath = os.path.expanduser('~/batteryLog.csv')
    battery = psutil.sensors_battery()
    with open(wpath, 'a') as wf:
        wf.write('%s,%s,%s\n' % (
            datetime.datetime.now().isoformat(),
            battery.power_plugged,
            battery.percent
        ))

while True:
    logTask()
    time.sleep(60)
