from tkinter import *
from tkinter import messagebox as msg

root = Tk()

root.title("TIC TAC TOE")
root.resizable(0, 0)
p1 = PhotoImage(file = 'F:/Python_GUI/tic-tac-toe.png') # location of image
root.iconphoto(False, p1) # fixed the size
# root.geometry("1200x701")

def theme():
    pass




#disable the game after win

def disabled_btn():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)

    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)

    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)
    
# Check who won

def checkifwon():
    global winner
    winner = False

# horizontal

    if b1["text"] == b2["text"] == b3["text"] == "X":
        b1.config(bg="cyan")
        b2.config(bg="cyan")
        b3.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT",f"Congratulate X Won")
    elif b1["text"] == b2["text"] == b3["text"] == "O":
        b1.config(bg="cyan")
        b2.config(bg="cyan")
        b3.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b4["text"] == b5["text"] == b6["text"] == "X":
        b4.config(bg="cyan")
        b5.config(bg="cyan")
        b6.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b4["text"] == b5["text"] == b6["text"] == "O":
        b4.config(bg="cyan")
        b5.config(bg="cyan")
        b6.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b7["text"] == b8["text"] == b9["text"] == "X":
        b7.config(bg="cyan")
        b8.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b7["text"] == b8["text"] == b9["text"] == "O":
        b7.config(bg="cyan")
        b8.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b1["text"] == b5["text"] == b9["text"] == "X":
        b1.config(bg="cyan")
        b5.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b1["text"] == b5["text"] == b9["text"] == "O":
        b1.config(bg="cyan")
        b5.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")

# vertical

    elif b1["text"] == b4["text"] == b7["text"] == "X":
        b1.config(bg="cyan")
        b4.config(bg="cyan")
        b7.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT",f"Congratulate X Won")
    elif b1["text"] == b4["text"] == b7["text"]  == "O":
        b1.config(bg="cyan")
        b4.config(bg="cyan")
        b7.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b2["text"] == b5["text"] == b8["text"] == "X":
        b2.config(bg="cyan")
        b5.config(bg="cyan")
        b8.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b2["text"] == b5["text"] == b8["text"] == "O":
        b2.config(bg="cyan")
        b5.config(bg="cyan")
        b8.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b3["text"] == b6["text"] == b9["text"] == "X":
        b3.config(bg="cyan")
        b6.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b3["text"] == b6["text"] == b9["text"] == "O":
        b3.config(bg="cyan")
        b6.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    elif b1["text"] == b5["text"] == b9["text"] == "X":
        b1.config(bg="cyan")
        b5.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b1["text"] == b5["text"] == b9["text"] == "O":
        b1.config(bg="cyan")
        b5.config(bg="cyan")
        b9.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")
    
    elif b3["text"] == b5["text"] == b7["text"] == "X":
        b3.config(bg="cyan")
        b5.config(bg="cyan")
        b7.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate X Won")
    elif b3["text"] == b5["text"] == b7["text"] == "O":
        b3.config(bg="cyan")
        b5.config(bg="cyan")
        b7.config(bg="cyan")
        winner = True
        disabled_btn()
        msg.showinfo("RESULT","Congratulate O Won")

    if count == 9 and winner == False:
        msg.showinfo("TIC TAC TOE","GAME TIED")
        reset()
    
clicked = True
count = 0

def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkifwon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkifwon()
    else:
        msg.showerror("TIC TAC TOE","Already filled with " + b["text"])



def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9
    global clicked,count
    clicked = True
# Build Button

    b1 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b1))
    b2 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b2))
    b3 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b3))
    b4 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b4))
    b5 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b5))
    b6 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b6))
    b7 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b7))
    b8 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b8))
    b9 = Button(root,text=' ',font=("Helvetica",20), height= 3,width= 6,bg= "SystemButtonFace", command=lambda:b_click(b9))


    # layout
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)

    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)

    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)

reset()

myMenu = Menu(root)
themes = Menu(myMenu, tearoff=0)
# themes.add_command(label="New")
# myMenu.add_cascade(label="Themes", menu=themes)
myMenu.add_command(label="Refresh",command = reset)
myMenu.add_command(label="Exit", command = root.destroy)
root.config(menu=myMenu)

root.mainloop()
