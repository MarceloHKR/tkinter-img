from tkinter import*
from utils import*

root = Tk()

root.iconbitmap('img_page.ico')

#cria o menubar/ barra do menu no topo da página
menubar = Menu(root)

#submenu/ uma das abas do menu
filemenu = Menu(menubar, tearoff=0)

#adiciona as opções no menu file
filemenu.add_command(
    label='Open',
    command =lambda: open_folder(root)
)
filemenu.add_command(label='Save')
filemenu.add_command(label='Exit')

#adiciona a função cascata no file/ uma função embaixo da outra
menubar.add_cascade(label='File', menu=filemenu)

#adiciona o menubar na janela
root.config(menu=menubar)

load_images(root)

#Botão para mostrar a próxima imagem
btn_prev = Button(root, text='Prev', pady=15, padx= 20, font=('Helvetica', 9), command=lambda: prev_image(root), bg='#212220', fg= 'white')

#Botão para mostrar a imagem anterior
btn_quit = Button(root, text='Sair', pady=15, padx= 15, font=('Helvetica', 9), command=lambda: quit(root), bg='#660000', fg= 'white')

#Botão para fecha a janela
btn_next = Button(root, text='Next', pady=15, padx= 20, font=('Helvetica', 9), command=lambda: next_image(root), bg='#212220', fg= 'white')

root.bind('<Right>', lambda event: next_image(root))
root.bind('<Left>', lambda event: prev_image(root))
root.bind('<Escape>', lambda event: root.quit())

#posicionamento dos botões

btn_prev.grid(column= 1, row=1)
btn_quit.grid(column= 2, row=1)
btn_next.grid(column= 3, row=1)





root.mainloop()
'''
                   _,........_
               _.-'    ___    `-._
            ,-'      ,'   \       `.
 _,...    ,'      ,-'     |  ,""":`._.
/     `--+.   _,.'      _.',',|"|  ` \`
\_         `"'     _,-"'  | / `-'   l L\
  `"---.._      ,-"       | l       | | |
      /   `.   |          ' `.     ,' ; |
     j     |   |           `._`"""' ,'  |__
     |      `--'____          `----'    .' `.
     |    _,-"""    `-.                 |    \
     l   /             `.               F     l
      `./     __..._     `.           ,'      |
        |  ,-"      `.    | ._     _.'        |
        . j           \   j   /`"""      __   |          ,"`.
         `|           | _,.__ |        ,'  `. |          |   |
          `-._       /-'     `L       .     , '          |   |
              F-...-'          `      |    , /           |   |
              |            ,----.     `...' /            |   |
              .--.        j      l        ,'             |   j
             j    L       |      |'-...--<               .  /
             `     |       . __,,_    ..  |               \/
              `-..'.._  __,-'     \  |  |/`._           ,'`
                  |   ""       .--`. `--,  ,-`..____..,'   |
                   L          /     \ _.  |   | \  .-.\    j
                  .'._        l     .\    `---' |  |  || ,'
                   .  `..____,-.._.'  `._       |  `--;"I'
                    `--"' `.            ,`-..._/__,.-1,'
                            `-.__  __,.'     ,' ,' _-'
                                 `'...___..`'--^--' mh
'''