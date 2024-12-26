#!/usr/bin/env python3

# Install TKinter on Ubuntu
# sudo apt install python3-tk

import tkinter as tk
import time
from datetime import datetime
eventstart = datetime.strptime('2024-12-24 12:00:00', '%Y-%m-%d %H:%M:%S')

starttimes = [
    datetime.strptime('2025-01-25 08:00:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2025-01-25 16:00:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2025-01-25 18:00:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2025-01-26 10:00:00', '%Y-%m-%d %H:%M:%S'),
]

durations = [ # minutes to count down before each start time, one per starttime
    120,
    120,
    30,
    120,
]

timeranges = []
finaltime = datetime.now().timestamp()

for index, starttime in enumerate(starttimes):
    endcountdown = starttime.timestamp()
    startcountdown = endcountdown - (durations[index] * 60)
    timeranges.append({'start': startcountdown, 'end': endcountdown})
    if finaltime < endcountdown:
        finaltime = endcountdown

#print(timeranges)

def getcurrentcountdown():
    nowtime = datetime.now().timestamp()
    for timerange in timeranges:
        if nowtime > timerange['start'] and nowtime < timerange['end']:
            return timerange['end'] - nowtime
    return -1

xposition = 3480
yposition = 950
xoffsetfortwonumbers = 115

def countdown():
    count = int(getcurrentcountdown())
    hours, rem = divmod(count, 3600)
    mins, secs = divmod(rem, 60)
    if count < 0:
        root.withdraw()
    else:
        root.deiconify()
        # root.destroy() to end the program

    if hours < 1:
        time_str = f"{mins:02}:{secs:02}"
        root.geometry("+"+str(xposition+xoffsetfortwonumbers)+"+"+str(yposition))
        time_label.config(text=time_str)
    else:
        time_str = f"{hours:02}:{mins:02}:{secs:02}"
        time_label.config(text=time_str)

    if finaltime < datetime.now().timestamp():
        print("Final Event Countdown is complete at ", datetime.now())
        root.destroy()
        exit()
    else:
        root.after(250, countdown)

root = tk.Tk()
root.geometry("+"+str(xposition)+"+"+str(yposition))
root.attributes('-topmost',True)
root.overrideredirect(True)
root.wait_visibility(root)
root.title("Countdown Timer")
# "Ubuntu Mono" also works well with xposition = 3500
time_label = tk.Label(root, text="00:00:00", font=("Noto Sans Mono", 48), fg="#E0E0E0", bg="#020202",anchor="e", justify='right')
time_label.pack()
countdown()
root.mainloop()
