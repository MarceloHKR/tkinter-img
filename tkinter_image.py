from tkinter import*
from PIL import ImageTk, Image, ImageOps
import os

root = Tk()

#lista e procura as imagens da nossa pasta imagens
arquivos = os.listdir('imagens')

#variável para armazenar as imagens
imagens = []

#variável de controle do índice da imagem atual
imagem_atual = 0


#imagens/ é a pasta

#percorre a lista de arquivos / muda as imagens
for arquivo in arquivos:
    #abre a imagem
    img = Image.open('imagens/' + arquivo)
    #redimensiona a imgem / define tamanho padrão para todas as imagens
    img = ImageOps.contain(img, (200, 200))
    #adiciona a imagem na lista / transforma o texto(nome do arquivo) em imagem pro Tkinter
    imagens.append(ImageTk.PhotoImage(img))

#Exibe os arquivos em um Label
#arquivos_label = Label(root, text = arquivos)
#arquivos_label.pack()


img_label = Label(root, image = imagens[imagem_atual])
img_label.grid(column=1, row=0, columnspan=3)

#defini a função do botão prev
def prev_image():
    global imagem_atual
    global img_label
    global imagens

    #verifica se é a primeira imagem. Se sim, volta para a última imagem
    if imagem_atual == 0:
        imagem_atual = len(imagens) -1
    else:
        imagem_atual -=1

    #apaga a imagem atual
    img_label.grid_forget()

    #exibe a nova imagem
    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=1, row=0, columnspan=3)

#defini a função do botão next
def next_image():
    global imagem_atual
    global img_label
    global imagens

    if imagem_atual == len(imagens) -1:
        imagem_atual = 0
        
    else:
        imagem_atual +=1

    img_label.grid_forget()

    img_label = Label(root, image=imagens[imagem_atual])
    img_label.grid(column=1, row=0, columnspan=3)

#Botão para mostrar a próxima imagem

btn_prev = Button(root, text='Prev', pady=15, font=('Helvetica', 9), command=prev_image)

#Botão para mostrar a imagem anterior

btn_quit = Button(root, text='Sair', pady=15, font=('Helvetica', 9), command=root.quit)

#Botão para fecha a janela

btn_next = Button(root, text='Next', pady=15, font=('Helvetica', 9), command=next_image)

#posicionamento dos botões

btn_prev.grid(column= 1, row=1)
btn_quit.grid(column= 2, row=1)
btn_next.grid(column= 3, row=1)





root.mainloop()