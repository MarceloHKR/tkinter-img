from tkinter import*
from PIL import ImageTk, Image
import os

root = Tk()

#lista e procura as imagens da nossa pasta imagens
arquivos = os.listdir('imagens')

#variável para armazenar as imagens
imagens = []

#imagens/ é a pasta

#percorre a lista de arquivos / muda as imagens
for arquivo in arquivos:
    #abre a imagem
    img = Image.open('imagens/' + arquivo)
    #adiciona a imagem na lista / transforma o texto(nome do arquivo) em imagem pro Tkinter
    imagens.append(ImageTk.PhotoImage(img))

#Exibe os arquivos em um Label
#arquivos_label = Label(root, text = arquivos)
#arquivos_label.pack()


img_label = Label(root, image = imagens[2])

img_label.pack()



root.mainloop()