import tkinter as tk

root = None

def window(title):
    global root
    root = tk.Tk()
    root.title(title)
    return root

def loop():
    global root
    root.mainloop()

def button(text="", ev=None):
    bu = tk.Button(root, text=text, command=ev)
    bu.pack()
    return bu

def text(text):
    la = tk.Label(root, text=text)
    la.pack()
    return la

def entry():
    entryy = tk.Entry(root)
    entryy.pack()
    return entryy

def get(entry):
    return entry.get()

def clear(entry):
    entry.delete(0, tk.END)