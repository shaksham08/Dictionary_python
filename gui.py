import tkinter as tk

window = tk.Tk()
label = tk.Label(
    text="Hello, Tkinter",
    fg="white",
    bg="black",
    width=200,
    height=200
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

entry = tk.Entry(fg="yellow", bg="blue", width=50)

entry.pack()

button.pack()

label.pack()

window.mainloop()
