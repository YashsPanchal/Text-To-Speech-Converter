import tkinter as tk
from tkinter import *
import pyttsx3

root=Tk()

obj=LabelFrame(root,text="Text to speech",font=20,bd=1)
obj.pack(fill="both",expand="yes",padx=10,pady=10)


root.title("Text to speech")
root.geometry("400x200")
root.resizable(False,False)
root.mainloop()
