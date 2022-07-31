from cProfile import label
from fileinput import filename
import tkinter as tk
from tkinter import Frame, filedialog, Text
import os

root = tk.Tk()

def addApp():
    #
    for widget in frame.winfo_children():
        widget.destroy()
    filename= filedialog.askopenfilename(initialdir="/", title="Select File",
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))



canvas = tk.Canvas(root, height=700, width=700, bg="#C7AAE3")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="#070A36")

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10,
pady=5, fg="white", bg="#070A36")

#runapps pack dedicated to colour 4 

runApps.pack()


root.mainloop()
