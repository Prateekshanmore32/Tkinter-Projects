from tkinter import *
def newFile():
    pass
def openFile():
    pass
def SaveFile():
    pass
def quitApp():
    pass
def cut():
    pass
def copy():
    pass
def paste():
    pass
def about():
    pass
if __name__ == '__main__':
    #Basic tkinter setup
    root=Tk()
    root.title("Untitled-Notepad")
    root.geometry("655x333")
    #Add TextArea
    # text=Text(root,font="lucida 13")
    # text.pack()
    # file=None
    #creating a menu bar
    MenuBar=Menu(root)
    # File menu Starts
    fileMenu=Menu(MenuBar,tearoff=0)
    # To open new file
    fileMenu.add_command(label="New",command=newFile)
    # To open already exsisting file
    fileMenu.add_command(label="Open",command=openFile)
    # To save the current file
    fileMenu.add_command(label="Save", command=SaveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="exit",command=quitApp)
    MenuBar.add_cascade(label="File",menu=fileMenu)
    # File menu ends


    # Edit menu starts
    editMenu=Menu(MenuBar,tearoff=0)
    # Cut, copy and paste
    editMenu.add_command(label="Cut",command=cut)
    editMenu.add_command(label="Copy",command=copy)
    editMenu.add_command(label="Paste",command=paste)
    MenuBar.add_cascade(label="Edit",menu=editMenu)
    # Edit menu Ends

    # Help menu Starts
    helpMenu=Menu(MenuBar,tearoff=0)
    helpMenu.add_command(label="About Notepad",command=about)
    MenuBar.add_cascade(label="Help",menu=helpMenu)
    # Help menu Ends

    root.config(menu=MenuBar)
    root.mainloop()