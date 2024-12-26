#!/usr/bin/env python3

# Install TKinter on Ubuntu
# sudo apt install python3-tk

import tkinter as tk
xposition = 1920
yposition = 1030
xsize = 50
ysize = 50

root = tk.Tk()

# Adjust size
root.geometry(str(xsize)+"x"+str(ysize)+"+"+str(xposition)+"+"+str(yposition))

root.attributes('-topmost',True)
root.overrideredirect(True)
root.configure(bg="#020202")
#root.wait_visibility(root)
#root.title("IBW")

#time_label = tk.Label(root, text="", font=("Arial", 48), fg="#020202", bg="#020202",anchor="e", justify='right')
#time_label.pack()
root.mainloop()
