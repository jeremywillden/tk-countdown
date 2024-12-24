# Install TKinter on Ubuntu
# sudo apt install python3-tk

import tkinter as tk
import time

def countdown(count):
    hours, rem = divmod(count, 3600)
    mins, secs = divmod(rem, 60)
    if hours < 1:
        time_str = f"{mins:02}:{secs:02}"
    else:
        time_str = f"{hours:02}:{mins:02}:{secs:02}"
    time_label.config(text=time_str)

    if count > 0:
        root.after(1000, countdown, count - 1)
    else:
        time_label.config(text="Time's up!")

def start_countdown():
    try:
        count = int(entry.get())
        countdown(count)
    except ValueError:
        time_label.config(text="Invalid input")

root = tk.Tk()
root.geometry("+3500+950")
root.attributes('-topmost',True)
root.overrideredirect(True)
#root.withdraw()
#root.wait_visibility(root)
#root.wm_attributes('-alpha',0.3)
root.title("Countdown Timer")

time_label = tk.Label(root, text="00:00:00", font=("Arial", 48), fg="#E0E0E0", bg="#020202")
time_label.pack()

root.mainloop()
