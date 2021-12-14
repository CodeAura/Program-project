import tkinter as tk
from tkinter.constants import BOTTOM
from PIL import ImageTk, Image
import os.path

Window = tk.Tk()
Window.title("CodeAura")
Window.geometry("1440x1024")



path = 'C:\\Users\\Mike\\Documents\\Scripts\\CodeAura\\LoginPage.png'


img = ImageTk.PhotoImage(Image.open(path))
panel = tk.Label(Window, image = img)
panel.pack(side = "bottom", fill = "both", expand = "yes")


Window.mainloop()