from tkinter import *
from PIL import *
 
def close():
    root.destroy()
 
win="#F8F8F8"
ls="#D8D9F2"
 
root=Tk()
screen_width = root.winfo_screenwidth()
screen_height=root.winfo_screenheight()
 
root.geometry(f"{screen_width}x{screen_height}")
root.title("GUI")
root.iconbitmap("./components/editor.ico")
root.config(bg=win)
 
upload = PhotoImage(file="./components/Upload.png")
rm_bg = PhotoImage(file="./components/rm_bg.png")
Dimensions = PhotoImage(file="./components/Dimensions.png")
 
 
 
f1 = Frame(root, bg = ls, width=450)
f1.pack(side=RIGHT, fill=Y)
 
f2=Frame(root, bg=win, height=450)
f2.pack(side=BOTTOM, fill=X)
 
f3 = Frame(root, bg='green')
f3.pack(side=TOP,fill=X)
 
b1 = Button(f3, image=upload, border=0, bg=win, command=close)
b1.pack()
b2=Button(f2, image=rm_bg, border=0 , bg=win)
b2.grid(row=0, column=0, padx=35, pady=50)
b3=Button(f2, image=Dimensions, border=0 , bg=win)
b3.grid(row=0, column=1, padx=35, pady=50)
 
 
 
 
root.mainloop()
