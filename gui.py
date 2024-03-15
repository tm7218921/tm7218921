from tkinter import *
from PIL import *
root=Tk()

screen_width=root.winfo_screenwidth()
screen_height= root.winfo_screenheight()
print(screen_height,screen_width)

ls="#d8d9f2"
 win="#34bdeb"
root.geometry(f"{screen_width}x{screen_height}")
root.title("Tanmay")
root.iconbitmap("./components/editor.ico")
#define images
upload = PhotoImage(file="./components/Upload.png")


f1 = Frame(root, bg=ls, width=450)
f1.pack(side=RIGHT, fill=Y)
f2 = Frame(root, bg=win, height=650)
f2.pack(side=TOP, fill=X)
f3 = Frame(root, bg=win, height=450)
f3.pack(side=BOTTOM, fill=X)

b1 = Button(f2, image=upload)
b1.pack()
root.mainloop()