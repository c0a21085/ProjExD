import tkinter as tk
import tkinter.messagebox as tkm
import maze_maker as mm

def key_down(event):
    global key
    key = event.keysym
    #print(key)

def key_up(event):
    global key
    key = ""
    #print(mx, my)

#0~9までのキーを入力することで､それぞれの数値に対応したこうかとんを表示する。(未完成)
def koukaton_change(event):
    global key, tori
    key = event.keysym
    if key in fig_list:
        tori = tk.PhotoImage(file=f"fig/{key}.png") 
        canvas.create_image(cx, cy, image=tori, tag = "koukaton")
        canvas.pack()        

def main_proc():
    global cx, cy, mx, my
    if key == "Up": my -= 1
    if key == "Down": my += 1
    if key == "Left": mx -= 1
    if key == "Right": mx += 1
    if maze_list[mx][my] == 1: # 移動先が壁だったら
        Gameover()
        if key == "Up": my += 1
        if key == "Down": my -= 1
        if key == "Left": mx += 1
        if key == "Right": mx -= 1
    cx = 50 + 100 * mx
    cy = 50 + 100 * my
    canvas.coords("koukaton", cx, cy)
    Goal()
    root.after(200 ,main_proc)

#Goal地点に付いたらメッセージを表示する
def Goal():
    print(mx, my)
    if mx == 13 and my == 7: #ゴール地点にいるなら
        mes = tkm.showinfo("Congratulation","ゴールしました！！！")
        if mes == "ok": #okボタンを押したら
            root.destroy() #ゲームを終了する
    else:
        pass

#Gameover(条件：移動先が壁だったら。)
def Gameover():
    tkm.showerror("Gameover","壁にぶつかり、けがをしてしまった...") 
    root.destroy()

if __name__ == "__main__":
    key = ""
    cx = 150
    cy = 150
    mx = 1
    my = 1
    fig_list = [n for n in range(10)]

    root = tk.Tk()
    root.title("迷えるこうかとん")
    tori = tk.PhotoImage(file="fig/2.png")
    start = tk.PhotoImage(file="fig/start.png") #Start画像
    goal = tk.PhotoImage(file="fig/goal.png") #Goal画像
    canvas = tk.Canvas(width = 1500, height = 900, bg = "black")
    maze_list = mm.make_maze(15, 9)
    mm.show_maze(canvas, maze_list)
    canvas.create_image(150, 150, image=start) #スタート地点にStart画像を貼る
    canvas.create_image(1350, 750, image=goal) #ゴール地点にGoal画像を貼る
    canvas.create_image(cx, cy, image=tori, tag = "koukaton")
    canvas.pack()

    root.bind("<KeyPress>", key_down)
    #root.bind("<KeyPress>", koukaton_change, "+")
    root.bind("<KeyRelease>", key_up)
    main_proc()

    root.mainloop()