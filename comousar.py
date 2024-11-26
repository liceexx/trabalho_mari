# from tkinter import  *
# janela = Tk()
# janela.title("Ola Mundo")
# janela.geometry("500x500")
# janela.mainloop()

# from tkinter import *

# window = Tk() 
# window.geometry("420x420")
# window.title("Izadora")

# icon = PhotoImage(file='logosatcnovo.png')
# window.iconphoto(True,icon)
# window.config(background="black") 

#window.mainloop() #lugar da janela no computador tela




# photo = PhotoImage(file='logosatcnovo.png')
# label = Label(window,
#               text="mano que saudade do meu ex",
#               font=('Arial',40,'bold'), 
#               fg='#00FF00',
#               bg='black',
#               relief=SUNKEN,
#               bd=10,
#               padx=20,
#               pady=20,
#               image=photo,
#               compound='top')

# label.pack()
# #label.place(x=0,y=0)

# window.mainloop()

#butto vc clica nele e el faz algo




#***********COMO CRIAR BOTAO**********
# from tkinter import *

# count = 0
# def click():
#     global count
#     count+=1
#     label.config(text=count)
    

# window = Tk()
# buttom = Button(window,text='Oi isadora')
# buttom.config(command= click) #chama e executa a função q vc criou
# buttom.config(font=('Ink Free', 50, 'bold'))
# buttom.config(bg='#9932CC')
# buttom.config(fg='#D2691E')
# buttom.config(activebackground='#FF0000')
# buttom.config(activeforeground='#D2691E')
# image=PhotoImage(file='emoji.png')
# buttom.config(image=image)
# buttom.config(compound='bottom')
# #buttom.config(state=DISABLED)
# label = Label(window, text = count)
# label.config(font=('Monospace', 50))
# label.pack
# buttom.pack()
# window.mainloop()



#***************APAGAR DELETAR E BACKSPACE**********
# from tkinter import *

# def submit():
#     username = entry.get()
#     print("Hello " + username)

# def delete():
#     entry.delete(0,END) #deleta a linha do texto

# def backspace():
#     entry.delete(len(entry.get())-1,END) #deleta o ultimo caracter

# window = Tk()

# submit = Button(window, text="submit", command=submit)
# submit.pack(side = RIGHT)

# delete = Button(window, text="delete", command=delete)
# delete.pack(side = RIGHT)

# backspace = Button(window, text="backspace", command=backspace)
# backspace.pack(side = RIGHT)

# entry = Entry()
# entry.config(font=('Ink Free', 50))
# entry.config(bg='#40E0D0')
# entry.config(fg='#FF1493')
# #entry.insert(0,'Dorinha')
# #entry.config(state=DISABLED)  #ACTIVE/DISABLED
# entry.config(width=10)
# #entry.config(show='*')
# entry.pack()
# window.mainloop()



#**************checkbox********************

# from tkinter import*

# def display():
#     if (x.get() == 1) & (y.get() == 0):
#         print('Eu gosto da alice')

#     elif (x.get() == 0) & (y.get() == 1):
#         print('Eu gosto da isadora')

#     elif (x.get() == 1) & (y.get() == 1):
#         print('Eu gosto das duas <3')

#     else:
#         print('Eu não gosto de nenhuma')

# window = Tk()

# x = IntVar()
# y = IntVar()

# checkbox = Checkbutton(window, text='Alice', variable= x, onvalue =1, offvalue=0, command=display)
# checkbox.pack()
# checkbox.config(font=('Arial', 20))
# checkbox.config(fg='#C71585')
# checkbox.config(bg='#000000')
# checkbox.config(activeforeground="#C71585")
# checkbox.config(activebackground="#000000")
# #photo = PhotoImage(file='emoji.png')
# #checkbox.config(image=photo, compound = 'left')
# #checkbox.config(padx=25, pady=10, widht=250, height=50)
# checkbox.config(anchor='w')



# checkbox2 = Checkbutton(window, text='Isadora', variable= y, onvalue =1, offvalue=0, command=display)
# checkbox2.pack()
# checkbox2.config(font=('Arial', 20))
# checkbox2.config(fg='#C71585')
# checkbox2.config(bg='#000000')
# checkbox2.config(activeforeground="#C71585")
# checkbox2.config(activebackground="#000000")
# #photo = PhotoImage(file='emoji.png')
# #checkbox2.config(image=photo, compound = 'left')
# #checkbox2.config(padx=25, pady=10, widht=250, height=50)
# checkbox.config(anchor='w')
# window.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# import mysql.connector

# # Função para conectar ao banco de dados
# def conectar_bd():
#     return mysql.connector.connect(
#         host="localhost",
#         user="root",        # seu usuário do MySQL
#         password="",        # sua senha do MySQL
#         database="meubanco" # nome do banco de dados
#     )

# # Função para cadastrar um cliente
# def cadastrar_cliente():
#     nome = entry_nome.get()
#     email = entry_email.get()
    
#     if nome == "" or email == "":
#         messagebox.showwarning("Entrada Inválida", "Por favor, preencha todos os campos.")
#         return
    
#     try:
#         conn = conectar_bd()
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO clientes (nome, email) VALUES (%s, %s)", (nome, email))
#         conn.commit()
#         messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
#         entry_nome.delete(0, tk.END)
#         entry_email.delete(0, tk.END)
#     except mysql.connector.Error as err:
#         messagebox.showerror("Erro", f"Erro ao conectar com o banco de dados: {err}")
#     finally:
#         if conn:
#             conn.close()

# # Função para pesquisar cliente
# def pesquisar_cliente():
#     nome = entry_nome.get()
    
#     if nome == "":
#         messagebox.showwarning("Entrada Inválida", "Por favor, insira o nome para pesquisa.")
#         return
    
#     try:
#         conn = conectar_bd()
#         cursor = conn.cursor()
#         cursor.execute("SELECT id, nome, email FROM clientes WHERE nome LIKE %s", (f"%{nome}%",))
#         resultado = cursor.fetchall()
        
#         if resultado:
#             texto_resultado.delete(1.0, tk.END)  # Limpa a caixa de texto
#             for linha in resultado:
#                 texto_resultado.insert(tk.END, f"ID: {linha[0]}, Nome: {linha[1]}, Email: {linha[2]}\n")
#         else:
#             messagebox.showinfo("Resultado", "Nenhum cliente encontrado.")
#     except mysql.connector.Error as err:
#         messagebox.showerror("Erro", f"Erro ao conectar com o banco de dados: {err}")
#     finally:
#         if conn:
#             conn.close()

# # Criando a interface gráfica com Tkinter
# root = tk.Tk()
# root.title("Cadastro e Pesquisa de Clientes")

# # Frame para cadastrar
# frame_cadastro = tk.Frame(root)
# frame_cadastro.pack(padx=10, pady=10)

# label_nome = tk.Label(frame_cadastro, text="Nome:")
# label_nome.grid(row=0, column=0, padx=5, pady=5)
# entry_nome = tk.Entry(frame_cadastro)
# entry_nome.grid(row=0, column=1, padx=5, pady=5)

# label_email = tk.Label(frame_cadastro, text="Email:")
# label_email.grid(row=1, column=0, padx=5, pady=5)
# entry_email = tk.Entry(frame_cadastro)
# entry_email.grid(row=1, column=1, padx=5, pady=5)

# btn_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar_cliente)
# btn_cadastrar.grid(row=2, columnspan=2, pady=10)

# # Frame para pesquisa
# frame_pesquisa = tk.Frame(root)
# frame_pesquisa.pack(padx=10, pady=10)

# label_nome_pesquisa = tk.Label(frame_pesquisa, text="Pesquisar por nome:")
# label_nome_pesquisa.grid(row=0, column=0, padx=5, pady=5)
# entry_nome_pesquisa = tk.Entry(frame_pesquisa)
# entry_nome_pesquisa.grid(row=0, column=1, padx=5, pady=5)

# btn_pesquisar = tk.Button(frame_pesquisa, text="Pesquisar", command=pesquisar_cliente)
# btn_pesquisar.grid(row=1, columnspan=2, pady=10)

# # Área para exibir resultados da pesquisa
# texto_resultado = tk.Text(root, height=10, width=50)
# texto_resultado.pack(padx=10, pady=10)

# # Inicia a aplicação
# root.mainloop()

""" import tkinter as tk

def abrir_janela():
    cadastrar = tk.Toplevel()
    cadastrar.title("Cadastrar")
    label_nome = tk.Label(cadastrar, text = "nome")
    label_nome.grid(row=0, column=0)
    botao_voltar = tk.Button(cadastrar, text= "Fechar", command = cadastrar.destroy)
    botao_voltar.grid(row=1, column=0)

def deletar():
    deletar = tk.Toplevel()
    deletar.title("Deletar")
    botao_voltar= tk.Button(deletar, text="Fechar", command=deletar.destroy)
    botao_voltar.grid(row = 1, column=3)

janela = tk.Tk()


botao = tk.Button(janela, text= "Cadastrar", command = abrir_janela)
botao.grid(row = 0, column=0)

botao2 = tk.Button(janela, text="Deletar", command= deletar)
botao2.grid(row = 3, column=10)
janela.mainloop() """

# import tkinter as tk

# janela = tk.Tk()
# janela.title("")
# janela.geometry('310x310')


# #dividindo a janela
# frama_cima = tk.Frame(janela, width = 310, heigh= 50, relief='flat')
# frama_cima.grid(row=0, column=0)

# frama_baixo = tk.Frame(janela, relief='flat', bg="#000000")
# frama_cima.grid(row=0, column=0)



# janela.mainloop()

# window = Tk()
# window.geometry("500x500")

# titleLabel = Label(window, text = "Informações", font = ("Arial", 25)).grid(row = 0, column = 0, columnspan=2)

# nome = Label(window, text = "Primeiro nome: ", bg = "red").grid(row = 1, column = 0)
# nomeEntry = Entry(window).grid(row = 1, column = 1)

# sobrenome = Label(window, text = "Segundo nome: ", bg = "green").grid(row = 2, column = 0)
# sobrenomeEntry = Entry(window).grid(row = 2, column = 1)

# email = Label(window, text = "Email: ", bg = "blue").grid(row = 3, column = 0)
# emailEntry = Entry(window).grid(row = 3, column = 1)

# submitButton = Button(window, text = "Submit").grid(row = 4, column = 0, columnspan = 2)

# window.mainloop()


from tkinter import * 
root = Tk()

#Criando o frame e estabelecendo configurações
arq = Frame(bg = "lightgrey")
arq["padx"] = 80
arq["pady"] = 5
arq.pack(fill='both', expand=True)

#Criando espaço para input no frame
inp = Entry(arq)
inp["width"] = 71
inp.configure(font = "Quicksand 12", bg = "white")
inp.pack(side=LEFT)

#Função para exibir o valor dado no terminal
def exibir():
   l = Label (arq, text= inp.get())
   l["padx"] = 20
   l["pady"] = 5
   l.configure(font = "Quicksand 12 bold", bg = "lightgrey")
   l.pack (side="left",fill="y")

#Criando botão para imprimir
bot_visualizar = Button(root, text = "Imprimir", command = exibir)
bot_visualizar.pack()

root.mainloop()


