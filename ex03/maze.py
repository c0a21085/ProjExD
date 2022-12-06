import tkinter as tk

if __name__ == "__main__":
    key = ""
    
    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    image = tk.PhotoImage(file="fig/2.png")

    canvas = tk.Canvas(width = 1500, height = 900, bg = "black")
    canvas.create_image(300, 400, image=image)
    canvas.pack()

    root.mainloop()