import tkinter as tk
import tkinter.messagebox as tkm

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}ボタンが押されました")

button = tk.Button(root, text = "0", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 4, column= 0)

button_1 = tk.Button(root, text = "1", font = ("",30), width = 4, height = 2)
button_1.bind("<1>", button_click)
button_1.grid(row = 3, column = 2)

button_2 = tk.Button(root, text = "2", font = ("",30), width = 4, height = 2)
button_2.bind("<1>", button_click)
button_2.grid(row = 3, column = 1)

button = tk.Button(root, text = "3", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 3, column= 0)

button = tk.Button(root, text = "4", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 2, column= 2)

button = tk.Button(root, text = "5", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 2, column= 1)

button = tk.Button(root, text = "6", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 2, column= 0)

button = tk.Button(root, text = "7", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 1, column= 2)

button = tk.Button(root, text = "8", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 1, column= 1)

button = tk.Button(root, text = "9", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 1, column= 0)
root.mainloop()