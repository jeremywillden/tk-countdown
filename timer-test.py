# Install TKinter on Ubuntu
# sudo apt install python3-tk

import tkinter as tk
import time
from datetime import datetime
eventstart = datetime.strptime('2024-12-24 12:00:00', '%Y-%m-%d %H:%M:%S')

#fullwidth = 0
xposition = 3520
yposition = 950
xoffsetfortwonumbers = 80

def countdown(count):
#    global fullwidth
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
#        newwidth = root.winfo_width()
#        print("newwidth: ", newwidth)
#        root.geometry("+"+str(3500+(fullwidth-newwidth))+"+950")
        root.geometry("+"+str(xposition+xoffsetfortwonumbers)+"+"+str(yposition))
        time_label.config(text=time_str)
    else:
        time_str = f"{hours:02}:{mins:02}:{secs:02}"
        time_label.config(text=time_str)

    if count >= 0:
        root.after(1000, countdown, count - 1)
    else:
        time_label.config(text="")

def start_countdown():
    try:
        nowtime = datetime.now()
        timeuntil = eventstart - nowtime
        secondsuntil = timeuntil.days * 24 * 3600 + timeuntil.seconds
        count = secondsuntil
        countdown(count)
    except ValueError:
        time_label.config(text="")

root = tk.Tk()
root.geometry("+"+str(xposition)+"+"+str(yposition))
root.attributes('-topmost',True)
root.overrideredirect(True)
#root.withdraw()
root.wait_visibility(root)
fullwidth = root.winfo_width()
print("fullwidth: ", fullwidth)
#root.wm_attributes('-alpha',0.3)
root.title("Countdown Timer")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 48), fg="#E0E0E0", bg="#020202",anchor="e", justify='right')
time_label.pack()
start_countdown()
root.mainloop()
