from tkinter import*
from PIL import ImageTk, Image, ImageOps
from tkinter import messagebox
from tkinter import filedialog
import os

#variável para armazenar as imagens
imagens = []

#variável de controle do índice da imagem atual
imagem_atual = 0

#variavel para armazenar o label da imagem
img_label = None

#variavel para armazenar o caminho da pasta de imagens
img_folder = ""

#função para carregar as imagens
def load_images(root):
    global img_folder
    global imagens
    global img_label

    #se existe uma pasta de imagens
    if img_folder:
        #Limpa a lista de imagens
        imagens.clear()
        #lista e procura as imagens da nossa pasta imagens
        arquivos = os.listdir(img_folder)

        #imagens/ é a pasta

        #percorre a lista de arquivos / muda as imagens
        for arquivo in arquivos:
            #tratativa de erro
            try:
                #abre a imagem
                img = Image.open(os.path.join(img_folder, arquivo))
            except:
                #se não for uma imagem, ignora o arquivo
                continue
            else:
                #redimensiona a imagem / define tamanho padrão para todas as imagens
                img = ImageOps.contain(img, (200, 200))
                #adiciona a imagem na lista / transforma o texto(nome do arquivo) em imagem pro Tkinter
                imagens.append(ImageTk.PhotoImage(img))
    else:
        #cria uma imagem em branco
        img = Image.new("RGB", (200, 200))
        #adiciona a imagem na lista
        imagens.append(ImageTk.PhotoImage(img))
    #carrega a primeira imagem no label
    img_label = Label(root, image = imagens[0])
    #exibe a imagem
    img_label.grid(column=1, row=0, columnspan=3)

#define a função do botão open do menu / abrir pasta
def open_folder(root):
    global img_folder
    img_folder = filedialog.askdirectory()

    if img_folder:
        load_images(root)
        messagebox.showinfo(
            title = 'Abrindo diretório...',
            message=f'O diretório selecionado foi: {img_folder}'
        )
    else:
        messagebox.showerror(
            title='Erro ao abrir diretório',
            message=f'Nenhum diretório foi selecionado'
        )


#defini a função do botão prev
def prev_image(root):
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
def next_image(root):
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


