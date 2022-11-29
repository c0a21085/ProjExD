import tkinter as tk
import tkinter.messagebox as tkm
import math

root = tk.Tk()
root.title("電卓")
root.geometry("265x475")

def button_click(event):
    btn = event.widget
    txt = btn["text"]
    if txt == "=": #合計
        try:
            total = eval(entry.get())
        except(SyntaxError or ZeroDivisionError):
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
        else:
            entry.delete(0, tk.END)
            entry.insert(tk.END, total)
    elif txt == "C": #一文字クリア
        entry.delete(len(entry.get())-1,tk.END)
    elif txt == "AC": #オールクリア
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, txt)
    #tkm.showinfo(txt, f"{txt}ボタンが押されました")

num_list = [n for n in range(10)]
num_list.append("+")
num_list.append("-")
num_list.append("*")
num_list.append("/")
num_list.append("=")
num_list.append("C")
num_list.append(".")
num_list.append("AC")


#print(num_list)

for num in num_list:
    if type(num) is int:
        button = tk.Button(root, text = str(num), font = ("",20), width = 4, height = 2, bg="#f5f5f5")
        button.bind("<1>", button_click)
        if num % 3 == 0 and num != 0:
            button.grid(row = 6 - math.ceil(num/3), column = 0)
        elif num % 3 == 1:
            button.grid(row = 6 - math.ceil(num/3), column = 2)
        elif num % 3 == 2:
            button.grid(row = 6 - math.ceil(num/3), column = 1)
        elif num == 0:
            button.grid(row = 6 - math.ceil(num/3), column = 1)
    elif type(num) is str:
        button = tk.Button(root, text = num, font = ("",20), width = 4, height = 2, bg="#c0c0c0")
        button.bind("<1>", button_click)
        if num == "+":
            button.grid(row = 5, column = 3)
        elif num == "-":
            button.grid(row = 4, column = 3)
        elif num == "*":
            button.grid(row = 3, column = 3)
        elif num == "/":
            button.grid(row = 2, column = 3)
        elif num == "=":
            button.grid(row = 6, column = 3)
        elif num == "C":
            button.grid(row = 1, column = 2)
        elif num == "AC":
            button.grid(row = 1, column = 3)
        elif num == ".":
            button.grid(row = 6, column = 2)
        
entry = tk.Entry(justify="right", width=16, font=("", 20))
entry.grid(row = 0, columnspan=5)

root.mainloop()