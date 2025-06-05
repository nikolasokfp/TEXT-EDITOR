from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename , asksaveasfilename



def openFile():
    filepath = asksaveasfilename(filetypes = [("Text file", ".txt") , ("ALL files", "*.*") ])
    if not filepath:
        return
    txtEdit.delete("1.0", "end")
    with open(filepath , "r") as input_file:
        text = input_file.read()
        txtEdit.insert(1.0 , text)
        screen.title(f"Simple text editor - {filepath}")



def saveas():
    filepath = asksaveasfilename(defaultextension = "docx", filetypes = [("Text file", ".txt") , ("ALL files", "*.*") ] )
    if not filepath:
        return
    with open(filepath, "w") as output_file:
        text= txtEdit.get(1.0 , END)
        output_file.write(text)
        screen.title

def clear():
    txtEdit.delete("1.0","end")


def exit1():
    screen .destroy()

def viww1():
    print("open")

def help1():
    messagebox.showinfo('Help', 'den me niazei to problima sou apla fige ')

def darkMode():
    choice = darkmode.get()
    if choice==1:
        txtEdit.configure(bg= 'black' , fg= 'white')
    elif choice==0:
        txtEdit.configure(bg = 'white', fg= 'black')
    else :
        print("error")


screen = Tk() #dimiourgia ouonis


screen.title("makis") #titlos

screen.rowconfigure(0, minsize=800, weight=1)
screen.columnconfigure(1 , minsize=800, weight=1)
screen.geometry('900x700')




menubar= Menu(screen)

file = Menu(menubar)
file.add_command(label = "Open" , command= openFile)
file.add_command(label = "Save As" , command= saveas)
file.add_command(label = "Cler" , command= clear)
file.add_command(label = "Exit" , command= exit1)


menubar.add_cascade(label="File" , menu=file)



darkmode = BooleanVar()
darkmode.set(False)


view = Menu(menubar)
view.add_checkbutton(label = "Darkmode", onvalue = 1 , offvalue = 0 , variable= darkmode, command= darkMode)

menubar.add_cascade(label="View" , menu=view)


help = Menu(menubar)
help.add_command(label = "About" , command= help1)
menubar.add_cascade(label="Help" , menu=help)



txtEdit = Text(screen)
txtEdit.grid(row = 0 , column = 1 , sticky="nsew")






screen.config(menu=menubar)
screen.mainloop()   #teleutaia entoli