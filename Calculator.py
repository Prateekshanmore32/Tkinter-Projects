from tkinter import *

def click(event):
    global scvalue
    text=event.widget.cget("text")
    # print(text)
    if text=='=':
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()
    elif text=='C':
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("690x690")
root.title("Calculator")
root.configure(background="black")
Label(root,text="Calculator",font="comicsanms 20 bold").pack(pady=10,padx=10)
scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,padx=20,pady=20)


f=Frame(root,bg="grey")

b=Button(f,text="9",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="8",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="7",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()

f=Frame(root,bg="grey")

b=Button(f,text="6",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="5",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="4",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()


f=Frame(root,bg="grey")

b=Button(f,text="3",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="2",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="1",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()

f=Frame(root,bg="grey")

b=Button(f,text="0",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="+",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="-",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()

f=Frame(root,bg="grey")

b=Button(f,text="*",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="/",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="%",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()

f=Frame(root,bg="grey")

b=Button(f,text="=",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text="C",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

b=Button(f,text=".",font="lucida 10 bold",padx=5,pady=5)
b.pack(side=LEFT,padx=10,pady=10)
b.bind('<Button-1>',click)

f.pack()

root.mainloop()