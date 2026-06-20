import tkinter as tk

def window(title):
    root = tk.Tk()
    root.title(title)
    return root

def loop(root):
    root.mainloop()
    return root

def button(root, text="", ev=None):
    bu = tk.Button(root, text=text, command=ev)
    bu.pack()
    return bu

def text(root, text):
    la = tk.Label(root, text=text)
    la.pack()
    return la

def entry(root):
    entryy = tk.Entry(root)
    entryy.pack()
    return entryy

def get(entry):
    return entry.get()

def clear(entry):
    entry.delete(0, tk.END)