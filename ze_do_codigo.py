from tkinter import*

root = Tk()

root.title('Zé do Código')

visor = Entry(root, width = 60)

visor.pack()

def myclick():
    texto = visor.get()
    mylabel = Label(root, texto)
    mylabel.pack

mybutton = Button(root, text="Don't Press")
mybutton.pack()



#.\venv\scripts\activate



root.mainloop()