import tkinter as tk
from tkinter import messagebox

# # 1. Criamos a janela do aplicativo
# janela = tk.Tk()
# janela.title("Sistema do Laboratório")
# janela.geometry("400x250")

# # Função que o botão vai executar quando for clicado
# def cadastrar_paciente():
#     nome = entrada_nome.get()
#     if nome:
#         messagebox.showinfo("Sucesso!", f"Paciente {nome} cadastrado!\nCódigo de barras gerado.")
#     else:
#         messagebox.showwarning("Aviso", "Por favor, digite o nome do paciente.")

# # 2. Criamos os elementos da tela (Texto, Campo de Digitação e Botão)
# rotulo = tk.Label(janela, text="Digite o nome do paciente:", font=("Arial", 12))
# rotulo.pack(pady=15)

# entrada_nome = tk.Entry(janela, font=("Arial", 12), width=30)
# entrada_nome.pack(pady=10)

# # O botão de ação que você queria ver
# botao = tk.Button(janela, text="Cadastrar no Sistema", font=("Arial", 11), command=cadastrar_paciente, bg="black", fg="white")
# botao.pack(pady=20)

# # 3. Mantém o aplicativo aberto rodando
# janela.mainloop()

# import barcode
# from barcode.writer import ImageWriter

# def cadastrar_paciente():
#     nome = entrada_nome.get()
    
#     if nome:
#         # 1. O Python gera um número único para o paciente (ex: baseado no relógio ou ID)
#         numero_id = "123456789012" 
        
#         # 2. A biblioteca do Python cria o código de barras no formato padrão (EAN13)
#         codigo = barcode.get('ean13', numero_id, writer=ImageWriter())
        
#         # 3. O Python salva o arquivo de imagem 'codigo_paciente.png' no seu computador
#         codigo.save('codigo_paciente')
        
#         messagebox.showinfo("Sucesso!", f"Paciente {nome} cadastrado!\nImagem 'codigo_paciente.png' salva na pasta!")

import tkinter as tk
from tkinter import messagebox
import barcode
from barcode.writer import ImageWriter

# 1. Criamos a janela do aplicativo
janela = tk.Tk()
janela.title("Sistema do Laboratório")
janela.geometry("400x250")

# Função que o botão vai executar quando for clicado
def cadastrar_paciente():
    nome = entrada_nome.get()
    
    if nome:
        # Número de 12 dígitos para o padrão EAN13 (o Python gera o 13º dígito sozinho)
        numero_id = "123456789012" 
        
        # Cria o código de barras salvando como imagem (.png)
        codigo = barcode.get('ean13', numero_id, writer=ImageWriter())
        
        # Salva o arquivo na mesma pasta com o nome 'codigo_paciente'
        codigo.save('codigo_paciente')
        
        messagebox.showinfo("Sucesso!", f"Paciente {nome} cadastrado!\nImagem 'codigo_paciente.png' salva na pasta!")
    else:
        messagebox.showwarning("Aviso", "Por favor, digite o nome do paciente.")

# 2. Criamos os elementos da tela
rotulo = tk.Label(janela, text="Digite o nome do paciente:", font=("Arial", 12))
rotulo.pack(pady=15)

entrada_nome = tk.Entry(janela, font=("Arial", 12), width=30)
entrada_nome.pack(pady=10)

botao = tk.Button(janela, text="Cadastrar no Sistema", font=("Arial", 11), command=cadastrar_paciente, bg="black", fg="white")
botao.pack(pady=20)

# 3. Mantém o aplicativo aberto rodando
janela.mainloop()