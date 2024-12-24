# Install TKinter on Ubuntu
# sudo apt install python3-tk

import tkinter as tk
import time
from datetime import datetime
eventstart = datetime.strptime('2024-12-24 12:00:00', '%Y-%m-%d %H:%M:%S')

starttimes = [
    datetime.strptime('2024-12-23 22:03:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2024-12-23 22:13:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2024-12-23 22:23:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2024-12-23 22:33:00', '%Y-%m-%d %H:%M:%S'),
    datetime.strptime('2024-12-23 22:43:00', '%Y-%m-%d %H:%M:%S'),
]

durations = [ # minutes to count down before each start time, one per starttime
    9,
    9,
    9,
    9,
    9,
]

timeranges = []

for index, starttime in enumerate(starttimes):
    endcountdown = starttime.timestamp()
    startcountdown = endcountdown - (durations[index] * 60)
    timeranges.append({'start': startcountdown, 'end': endcountdown})

print(timeranges)

def getcurrentcountdown():
    nowtime = datetime.now().timestamp()
    for timerange in timeranges:
        if nowtime > timerange['start'] and nowtime < timerange['end']:
            return timerange['end'] - nowtime
    return -1

xposition = 3520
yposition = 950
xoffsetfortwonumbers = 80

def countdown():
    count = int(getcurrentcountdown())
    hours, rem = divmod(count, 3600)
    mins, secs = divmod(rem, 60)
    if count < 0:
        root.withdraw()
        # to restore the window
        # root.deiconify()
        # root.destroy() to end the program
        return

    if hours < 1:
        time_str = f"{mins:02}:{secs:02}"
        root.geometry("+"+str(xposition+xoffsetfortwonumbers)+"+"+str(yposition))
        time_label.config(text=time_str)
    else:
        time_str = f"{hours:02}:{mins:02}:{secs:02}"
        time_label.config(text=time_str)

    if count >= 0:
        root.after(250, countdown)
    else:
        time_label.config(text="")

root = tk.Tk()
root.geometry("+"+str(xposition)+"+"+str(yposition))
root.attributes('-topmost',True)
root.overrideredirect(True)
root.wait_visibility(root)
root.title("Countdown Timer")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 48), fg="#E0E0E0", bg="#020202",anchor="e", justify='right')
time_label.pack()
countdown()
root.mainloop()
