import tkinter as tk
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""
    #print(key)

def main_proc():
    global cx, cy, mx, my
    if key == "Up": 
        my -= 1
    if key == "Down": 
        my += 1
    if key == "Left": 
        mx -= 1
    if key == "Right": 
        mx += 1
    if maze_list[mx][my] == 1: # 移動先が壁だったら
        if key == "Up": 
            my += 1
        if key == "Down": 
            my -= 1
        if key == "Left": 
            mx += 1
        if key == "Right": 
            mx -= 1    
    cx = 50 + 100 * mx
    cy = 50 + 100 * my
    canvas.coords("koukaton", cx, cy)
    root.after(100 ,main_proc)

if __name__ == "__main__":
    key = ""
    cx = 150
    cy = 150
    mx = 1
    my = 1

    root = tk.Tk()
    root.title("迷えるこうかとん")
    
    tori = tk.PhotoImage(file="fig/2.png")

    canvas = tk.Canvas(width = 1500, height = 900, bg = "black")
    maze_list = mm.make_maze(15, 9)
    mm.print_maze(maze_list)
    print(maze_list)
    mm.show_maze(canvas, maze_list)
    canvas.create_image(cx, cy, image=tori, tag = "koukaton")
    canvas.pack()

    #mm.show_maze(canvas, mm.make_maze(15,9))

    root.bind("<KeyPress>", key_down)
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()