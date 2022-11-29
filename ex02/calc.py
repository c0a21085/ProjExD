import tkinter as tk
import tkinter.messagebox as tkm
import math

root = tk.Tk()
root.title("電卓")
root.geometry("300x500")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    tkm.showinfo(txt, f"{txt}ボタンが押されました")

num_list = [n for n in range(10)]
#print(num_list)

for num in num_list:
    button = tk.Button(root, text = str(num), font = ("",30), width = 4, height = 2)
    button.bind("<1>", button_click)
    if num % 3 == 0:
        button.grid(row = 4 - math.ceil(num/3), column= 0)
    elif num % 3 == 1:
        button.grid(row = 4 - math.ceil(num/3), column= 2)
    elif num % 3 == 2:
        button.grid(row = 4 - math.ceil(num/3), column= 1)   

button = tk.Button(root, text = "+", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 4 , column= 1)

button = tk.Button(root, text = "=", font = ("",30), width = 4, height = 2)
button.bind("<1>", button_click)
button.grid(row = 4 , column= 2)

        
entry = tk.Entry(justify="right", width=10, font=("", 40))
entry.grid(row = 0, columnspan=3)

root.mainloop()