# The jamband Phish has been playing together for over 30 years and have a library of 290 songs.
# This program randomly generates one of their songs. For all the wooks out there.

import json
import os
import random
import tkinter as tk
from PIL import ImageTk, Image


root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=525)
canvas.pack()

base_dir = os.path.dirname(os.path.abspath(__file__))
img = ImageTk.PhotoImage(Image.open(os.path.join(base_dir, "phFB.jpg")))
canvas.create_image(20, 20, anchor=tk.NW, image=img)

with open(os.path.join(base_dir, "phishSongs.json")) as f:
    phishsongs = json.load(f)["phishsongs"]

song = random.choice(phishsongs)
canvas.create_text(400, 470, text=song, font=("Helvetica", 20, "bold"), fill="white")
canvas.create_text(400, 505, text="By The Phish From Vermont", font=("Helvetica", 12), fill="white")

root.mainloop()
