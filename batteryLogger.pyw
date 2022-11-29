import psutil
import datetime
import os
import time
from tendo import singleton

def logTask():
    wpath = os.path.expanduser('~/batteryLog.csv')
    battery = psutil.sensors_battery()
    with open(wpath, 'a') as wf:
        wf.write('%s,%s,%s\n' % (
            datetime.datetime.now().isoformat(),
            battery.power_plugged,
            battery.percent
        ))

me = singleton.SingleInstance()

if __name__ == '__main__':
    # Ignore unused variable warning: me should live until the end of the script.
    while True:
        logTask()
        time.sleep(60)
