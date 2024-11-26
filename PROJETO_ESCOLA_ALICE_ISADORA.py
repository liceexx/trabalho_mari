import tkinter as tk
from tkinter.ttk import *
from tkinter import messagebox
import mysql.connector


conexao_banco = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='escola'
)

cursor = conexao_banco.cursor()


janela = tk.Tk()
janela.title("Menu")
janela.geometry("500x500")

titulo = tk.Label(janela, text='ESCOLA', background='orange', font='Arial 50') #label é um texto fixo oinde vc coloca algo escrito
titulo.grid(row=0, column=6, pady=20)


# função de cadastrar os usuarios
def cadastrar():
    cadastrar = tk.Toplevel() #uma nova janela para o cmapo cadastrar
    cadastrar.title("Cadastrar")
    cadastrar.geometry("500x500")
    botao_voltar2 = tk.Button(cadastrar, text="Fechar", command=cadastrar.destroy)
    botao_voltar2.grid(row = 50, column= 0)


    def cadastrar_aluno():
        aluno = tk.Toplevel()
        aluno.title("Cadastrar Aluno")
        aluno.geometry("1500x2000")
        cadastrar.destroy()
        

        Label.id_label = Label(aluno, text='ID: ') 
        Label.id_label.grid(row=1, column=0)
        id_entry = Entry(aluno)  #entry é onde você coloca a "resposta" do label
        id_entry.grid(row=1, column=1)

        Label.nome_label = Label(aluno, text='Nome: ')
        Label.nome_label.grid(row=2, column=0)
        nome_entry = Entry(aluno)
        nome_entry.grid(row=2, column=1)

        Label.cpf_label = Label(aluno, text='CPF: ') 
        Label.cpf_label.grid(row=4, column=0)
        cpf_entry = Entry(aluno)
        cpf_entry.grid(row=4, column=1)

        Label.data_nascimento_label = Label(aluno, text='Data de Nascimento: ') 
        Label.data_nascimento_label.grid(row=5, column=0)
        data_nascimento_entry = Entry(aluno)
        data_nascimento_entry.grid(row=5, column=1)

        Label.telefone_label = Label(aluno, text='Telefone: ')  
        Label.telefone_label.grid(row=6, column=0)
        telefone_entry = Entry(aluno)
        telefone_entry.grid(row=6, column=1)

        Label.pai_label = Label(aluno, text='Pai: ')  
        Label.pai_label.grid(row=7, column=0)
        pai_entry = Entry(aluno)
        pai_entry.grid(row=7, column=1)

        Label.mae_label = Label(aluno, text='Mãe: ')  
        Label.mae_label.grid(row=8, column=0)
        mae_entry = Entry(aluno)
        mae_entry.grid(row=8, column=1)

        Label.telefone_resp_label = Label(aluno, text='Telefone Responsável: ')  
        Label.telefone_resp_label.grid(row=9, column=0)
        telefone_resp_entry = Entry(aluno)
        telefone_resp_entry.grid(row=9, column=1)

        Label.endereco_label = Label(aluno, text='Endereço: ')  
        Label.endereco_label.grid(row=10, column=0)
        endereco_entry = Entry(aluno)
        endereco_entry.grid(row=10, column=1)

        Label.ano_escolar_label = Label(aluno, text='Ano Escolar: ')  
        Label.ano_escolar_label.grid(row=11, column=0)
        ano_escolar_entry = Entry(aluno)
        ano_escolar_entry.grid(row=11, column=1)

        Label.turno_label = Label(aluno, text='Turno: ')  
        Label.turno_label.grid(row=12, column=0)
        turno_entry = Entry(aluno)
        turno_entry.grid(row=12, column=1)

        colunas = ('id', 'nome', 'cpf', 'data_nascimento', 'telefone_aluno', 'nome_pai', 'nome_mae', 'telefone_responsavel', 'endereco', 'ano_escolar', 'turno_aluno')
        tree = Treeview(aluno, columns=colunas, show="headings")
        tree.grid(row=20, column=0, columnspan=5)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')


        def comando():
            id_value = id_entry.get()  # Obtém os valores dos campos para poder trabalhar com eles
            nome_value = nome_entry.get()
            cpf_value = cpf_entry.get()
            data_nascimento_value = data_nascimento_entry.get()
            telefone_value = telefone_entry.get()
            nome_pai_value = pai_entry.get()
            nome_mae_value = mae_entry.get()
            telefone_resp_value = telefone_resp_entry.get()
            endereco_value = endereco_entry.get()
            ano_escolar_value = ano_escolar_entry.get()
            turno_value = turno_entry.get()

            # Label para exibir mensagens (usando tk.Label para permitir customização de cor)
            if not hasattr(comando, "mensagem_label"):
                comando.mensagem_label = tk.Label(aluno, text="", fg="red")
                comando.mensagem_label.grid(row=14, column=1, columnspan=3)

            mensagem_label = comando.mensagem_label

            # Verificação de campos obrigatórios
            if not id_value or not nome_value or not cpf_value:
                mensagem_label.config(text="Por favor, preencha os campos obrigatórios (ID, Nome e CPF).")
                mensagem_label.after(3000, lambda: mensagem_label.config(text=""))  # Limpa a mensagem após 3 segundos
                return

            # Validação de ID (somente números)
            if not id_value.isdigit():
                mensagem_label.config(text="O ID deve conter apenas números.")
                mensagem_label.after(3000, lambda: mensagem_label.config(text=""))
                return

            # Validação de CPF (somente números)
            if not cpf_value.isdigit():
                mensagem_label.config(text="O CPF deve conter apenas números.")
                mensagem_label.after(3000, lambda: mensagem_label.config(text=""))
                return

            # Validação de Nome (somente letras e espaços)
            if not all(char.isalpha() or char.isspace() for char in nome_value): #isalpha verifica se é caracter e se não tem caracter especial// isspace verifica se n tem espaço em branco
                mensagem_label.config(text="O Nome deve conter apenas letras.")
                mensagem_label.after(3000, lambda: mensagem_label.config(text="")) #uma função para apagar a mensagem em 3 segundos
                return

            # Verificação de duplicidade de ID
            cursor.execute(f"SELECT id FROM aluno WHERE id = '{id_value}'")
            if cursor.fetchone() is not None:  # Se o ID já existe
                mensagem_label.config(text="O ID informado já está cadastrado. Insira outro ID.")
                mensagem_label.after(3000, lambda: mensagem_label.config(text=""))
                return

            # Insere os dados no banco
            comando_sql = f'''INSERT INTO aluno 
            (id, nome, cpf_aluno, data_nascimento, telefone_aluno, nome_pai, nome_mae, telefone_responsavel, endereco, ano_escolar, turno_aluno)
            VALUES ("{id_value}", "{nome_value}", "{cpf_value}", "{data_nascimento_value}", "{telefone_value}", 
            "{nome_pai_value}", "{nome_mae_value}", "{telefone_resp_value}", "{endereco_value}", 
            "{ano_escolar_value}", "{turno_value}")'''
            cursor.execute(comando_sql)
            conexao_banco.commit()

            # Atualiza Treeview
            tree.insert('', tk.END, values=(
                id_value, nome_value, cpf_value, data_nascimento_value, telefone_value,
                nome_pai_value, nome_mae_value, telefone_resp_value, endereco_value, 
                ano_escolar_value, turno_value))

            # Exibe mensagem de sucesso
            mensagem_label.config(text="Cadastro realizado com sucesso!", fg="green")
            mensagem_label.after(3000, lambda: mensagem_label.config(text=""))

            # Limpa os campos
            id_entry.delete(0, tk.END)
            nome_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)
            data_nascimento_entry.delete(0, tk.END)
            telefone_entry.delete(0, tk.END)
            mae_entry.delete(0, tk.END)
            pai_entry.delete(0, tk.END)
            telefone_resp_entry.delete(0, tk.END)
            endereco_entry.delete(0, tk.END)
            ano_escolar_entry.delete(0, tk.END)
            turno_entry.delete(0, tk.END)




        
        botao_cadastro = tk.Button(aluno, text="cadastrar aluno", command=comando)
        botao_cadastro.grid(row = 30, column=4)

        botao_voltar2 = tk.Button(aluno, text="Fechar", command=aluno.destroy)
        botao_voltar2.grid(row = 35 , column=4)

    def cadastrar_professor():
        professor = tk.Toplevel()
        professor.title("Cadastrar Professor")
        professor.geometry("1500x2000")
        cadastrar.destroy
        botao_voltar2 = tk.Button(professor, text="Fechar", command=cadastrar.destroy)
        botao_voltar2.grid(row = 20, column=0)

        Label.id_label = Label(professor, text='ID: ')
        Label.id_label.grid(row=1, column=0)
        id_entry = Entry(professor)
        id_entry.grid(row=1, column=1)


        Label.nome_label = Label(professor, text='Nome: ')
        Label.nome_label.grid(row=2, column=0)
        nome_entry = Entry(professor)
        nome_entry.grid(row=2, column=1)


        Label.salario_label = Label(professor, text='Salário: ')
        Label.salario_label.grid(row=3, column=0)
        salario_entry = Entry(professor)
        salario_entry.grid(row=3, column=1)


        Label.cpf_label = Label(professor, text='CPF: ')
        Label.cpf_label.grid(row=4, column=0)
        cpf_entry = Entry(professor)
        cpf_entry.grid(row=4, column=1)


        Label.data_nascimento_label = Label(professor, text='Data de Nascimento: ')
        Label.data_nascimento_label.grid(row=5, column=0)
        data_nascimento_entry = Entry(professor)
        data_nascimento_entry.grid(row=5, column=1)


        Label.endereco_label = Label(professor, text='Endereço: ')
        Label.endereco_label.grid(row=6, column=0)
        endereco_entry = Entry(professor)
        endereco_entry.grid(row=6, column=1)


        Label.telefone_label = Label(professor, text='Telefone: ')
        Label.telefone_label.grid(row=7, column=0)
        telefone_entry = Entry(professor)
        telefone_entry.grid(row=7, column=1)


        Label.nr_aulas_label = Label(professor, text='Número de Aulas: ')
        Label.nr_aulas_label.grid(row=8, column=0)
        nr_aulas_entry = Entry(professor)
        nr_aulas_entry.grid(row=8, column=1)


        Label.materia_label = Label(professor, text='Matéria: ')
        Label.materia_label.grid(row=9, column=0)
        materia_entry = Entry(professor)
        materia_entry.grid(row=9, column=1)


        colunas = ('ID', 'Nome', 'Salário', 'CPF', 'Data de Nascimento', 
                'Endereço', 'Telefone', 'Número de Aulas', 'Matéria')
        tree = Treeview(professor, columns=colunas, show="headings")
        tree.grid(row=20, column=0, columnspan=5)

        for col in colunas:
            tree.heading(col, text=col)
            tree.column(col, width=100, anchor='center')



        def comando2():

            id_value = id_entry.get()
            nome_value = nome_entry.get()
            salario_value = salario_entry.get()
            cpf_value = cpf_entry.get()
            data_nascimento_value = data_nascimento_entry.get()
            endereco_value = endereco_entry.get()
            telefone_value = telefone_entry.get()
            nr_aulas_value = nr_aulas_entry.get()
            materia_value = materia_entry.get()

    
            # Validação dos campos

            if not hasattr(comando2, "mensagem_label"):
                comando2.mensagem_label = tk.Label(professor, text="", fg="red")
                comando2.mensagem_label.grid(row=14, column=1, columnspan=3)

            # Verificação de campos obrigatórios
            if not id_value or not nome_value or not cpf_value:
                comando2.mensagem_label.config(text="Por favor, preencha os campos obrigatórios (ID, Nome e CPF).")
                comando2.mensagem_label.after(3000, lambda: comando2.mensagem_label.config(text=""))  # Limpa a mensagem após 3 segundos
                return

            if not id_value.isdigit():
                comando2.mensagem_label.config(text="O ID deve conter apenas números.")
                comando2.mensagem_label.after(3000, lambda: comando2.mensagem_label.config(text=""))
                return

            if not cpf_value.isdigit():
                comando2.mensagem_label.config(text="O CPF deve conter apenas números.")
                comando2.mensagem_label.after(3000, lambda: comando2.mensagem_label.config(text=""))
                return

            if not all(char.isalpha() or char.isspace() for char in nome_value):
                comando2.mensagem_label.config(text="O Nome deve conter apenas letras.")
                comando2.mensagem_label.after(3000, lambda: comando2.mensagem_label.config(text=""))
                return

            # Caso todos os campos sejam válidos, realiza o cadastro
            comando_sql = f'''INSERT INTO professores 
            (id, nome, salario, cpf, data_nascimento, endereco, telefone, numero_aulas, materia) 
            VALUES ("{id_value}", "{nome_value}", "{salario_value}", "{cpf_value}", "{data_nascimento_value}", "{endereco_value}",
            "{telefone_value}", "{nr_aulas_value}", "{materia_value}")'''
            
            cursor.execute(comando_sql)
            conexao_banco.commit()

            # Atualiza a tabela com os dados cadastrados
            tree.insert('', tk.END, values=(
                id_value, nome_value, salario_value, cpf_value, data_nascimento_value,
                endereco_value, telefone_value, nr_aulas_value, materia_value))

            # Exibe a mensagem de sucesso
            comando2.mensagem_label.config(text="Cadastro realizado com sucesso!")
            comando2.mensagem_label.after(3000, lambda: comando2.mensagem_label.config(text=""))

            # Limpa os campos após o cadastro
            id_entry.delete(0, tk.END)
            nome_entry.delete(0, tk.END)
            salario_entry.delete(0, tk.END)
            cpf_entry.delete(0, tk.END)
            data_nascimento_entry.delete(0, tk.END)
            endereco_entry.delete(0, tk.END)
            telefone_entry.delete(0, tk.END)
            nr_aulas_entry.delete(0, tk.END)
            materia_entry.delete(0, tk.END)


        botao_cadastro = tk.Button(professor, text="cadastrar professor", command=comando2)
        botao_cadastro.grid(row = 30, column=4)

        botao_voltar2 = tk.Button(professor, text="Fechar", command=professor.destroy)
        botao_voltar2.grid(row = 35 , column=4)



        botao_cadastro = tk.Button(professor, text="cadastrar professor", command=comando2)
        botao_cadastro.grid(row = 30, column=4)

        botao_voltar2 = tk.Button(professor, text="Fechar", command=professor.destroy)
        botao_voltar2.grid(row = 35 , column=4)

    

    botao_aluno= tk.Button(cadastrar, text="Cadastrar Aluno",command=cadastrar_aluno)
    botao_aluno.grid(row = 2, column=30)



    btn_professor= tk.Button(cadastrar, text="Cadastrar Professor",command=cadastrar_professor)
    btn_professor.grid(row = 4, column=30)


def deletar():
    deletar = tk.Toplevel()
    deletar.title("Deletar")
    deletar.geometry("500x500")

    def deletar_aluno():
        deletar_aluno = tk.Toplevel()
        deletar_aluno.title("Deletar Aluno")
        deletar_aluno.geometry("500x500")
        deletar.destroy()


        Label(deletar_aluno, text='ID do Aluno: ').grid(row=1, column=0)
        id_entry = Entry(deletar_aluno)
        id_entry.grid(row=1, column=1)

        def comando():
            id_value = id_entry.get()

            if not id_value.isdigit():
                messagebox.showerror("Erro", "Por favor, insira um ID válido.")
                return

            comando_sql = f'DELETE FROM aluno WHERE id = {id_value}'
            cursor.execute(comando_sql)
            conexao_banco.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", "Aluno deletado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum aluno encontrado com o ID fornecido.")

            id_entry.delete(0, tk.END)

        tk.Button(deletar_aluno, text="Excluir", command=comando).grid(row=2, column=1)

        botao_voltar2 = tk.Button(deletar_aluno, text="Fechar", command=deletar_aluno.destroy)
        botao_voltar2.grid(row = 35 , column=4)

    def deletar_professor():
        deletar_professor = tk.Toplevel()
        deletar_professor.title("Deletar Professor")
        deletar_professor.geometry("500x500")
        deletar.destroy()

        Label(deletar_professor, text='ID do Professor: ').grid(row=1, column=0)
        id_entry = Entry(deletar_professor)
        id_entry.grid(row=1, column=1)

        def comando():
            id_value = id_entry.get()

            if not id_value.isdigit():
                messagebox.showerror("Erro", "Por favor, insira um ID válido.")
                return

            comando_sql = f'DELETE FROM professores WHERE id = {id_value}'
            cursor.execute(comando_sql)
            conexao_banco.commit()

            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", "Professor deletado com sucesso!")
            else:
                messagebox.showwarning("Aviso", "Nenhum professor encontrado com o ID fornecido.")

            id_entry.delete(0, tk.END)

        tk.Button(deletar_professor, text="Excluir", command=comando).grid(row=2, column=1)

        botao_voltar2 = tk.Button(deletar_professor, text="Fechar", command=deletar_professor.destroy)
        botao_voltar2.grid(row = 35 , column=4)

    tk.Button(deletar, text="Fechar", command=deletar.destroy).grid(row=10, column=30)
    tk.Button(deletar, text="Deletar Aluno", command=deletar_aluno).grid(row=2, column=30)
    tk.Button(deletar, text="Deletar Professor", command=deletar_professor).grid(row=4, column=30)


def pesquisa():
    pesquisa = tk.Toplevel()
    pesquisa.title("Pesquisa")
    pesquisa.geometry("500x500")
    botao_voltar= tk.Button(pesquisa, text="Fechar", command=pesquisa.destroy)
    botao_voltar.grid(row = 10, column=0)



    def pesquisar_aluno():
        pesquisar_aluno = tk.Toplevel()
        pesquisar_aluno.title("Pesquisar aluno")
        pesquisar_aluno.geometry("500x500")
        pesquisa.destroy()
        botao_voltar2 = tk.Button(pesquisar_aluno, text="Fechar", command=pesquisar_aluno.destroy)
        botao_voltar2.grid(row = 10, column=0)

            
        Label(pesquisar_aluno, text="Pesquisar pelo ID ou Nome Completo").grid(row=0, column=0, columnspan=2, pady=10)
        Label(pesquisar_aluno, text="ID:").grid(row=1, column=0, padx=10, pady=10)
        id_entry = Entry(pesquisar_aluno)
        id_entry.grid(row=1, column=1)

        Label(pesquisar_aluno, text="Nome Completo:").grid(row=2, column=0, padx=10, pady=10)
        nome_entry = Entry(pesquisar_aluno)
        nome_entry.grid(row=2, column=1)

        resultado_label = Label(pesquisar_aluno, text="", wraplength=400, justify="left")
        resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

        def comando():
            id_value = id_entry.get().strip()
            nome_value = nome_entry.get().strip()

            if id_value.isdigit():
            
                cursor.execute(f'SELECT * FROM aluno WHERE id = "{id_value}"')
            elif nome_value:
            
                cursor.execute("SELECT * FROM aluno WHERE nome LIKE %s", ('%' + nome_value + '%',))

            else:
                resultado_label.config(text="Por favor, insira um ID ou Nome válido.")
                return
            
            resultado = cursor.fetchall()
            if resultado:
                resultado_texto = "\n".join([f"ID: {row[0]}\n Nome: {row[1]}\n CPF: {row[2]}" for row in resultado])
                resultado_label.config(text=f"Resultados encontrados:\n\n{resultado_texto}")
            else:
                resultado_label.config(text="Nenhum registro encontrado.")

            id_entry.delete(0, tk.END)
            nome_entry.delete(0,tk.END)

        tk.Button(pesquisar_aluno, text="Pesquisar", command=comando).grid(row=15, column=1)


    def pesquisar_professor():
        pesquisar_professor = tk.Toplevel()
        pesquisar_professor.title("Pesquisar professor")
        pesquisar_professor.geometry("500x500")
        pesquisa.destroy()
        botao_voltar2 = tk.Button(pesquisar_professor, text="Fechar", command=pesquisar_professor.destroy)
        botao_voltar2.grid(row = 15, column=0)

        Label(pesquisar_professor, text="Pesquisar pelo ID ou Nome Completo").grid(row=0, column=0, columnspan=2, pady=10)
        Label(pesquisar_professor, text="ID:").grid(row=1, column=0, padx=10, pady=10)
        id_entry = Entry(pesquisar_professor)
        id_entry.grid(row=1, column=1)

        Label(pesquisar_professor, text="Nome Completo:").grid(row=2, column=0, padx=10, pady=10)
        nome_entry = Entry(pesquisar_professor)
        nome_entry.grid(row=2, column=1)

        resultado_label = Label(pesquisar_professor, text="", wraplength=400, justify="left")
        resultado_label.grid(row=4, column=0, columnspan=2, pady=10)

        def comando():
            id_value = id_entry.get().strip()
            nome_value = nome_entry.get().strip()

            if id_value.isdigit():
            
                cursor.execute(f'SELECT * FROM professores WHERE id = "{id_value}"')
            elif nome_value:
            
                cursor.execute("SELECT * FROM professores WHERE nome LIKE %s", ('%' + nome_value + '%',))

            else:
                resultado_label.config(text="Por favor, insira um ID ou Nome válido.")
                return
            
            resultado = cursor.fetchall()
            if resultado:
                resultado_texto = "\n".join([f"ID: {row[0]}, Nome: {row[1]}, Curso: {row[2]}" for row in resultado])
                resultado_label.config(text=f"Resultados encontrados:\n\n{resultado_texto}")
            else:
                resultado_label.config(text="Nenhum registro encontrado.")

        tk.Button(pesquisar_professor, text="Pesquisar", command=comando).grid(row=15, column=1)

    tk.Button(pesquisa, text="Fechar", command=pesquisa.destroy).grid(row=10, column=30)
    tk.Button(pesquisa, text="Pesquisar Aluno", command=pesquisar_aluno).grid(row=2, column=30)
    tk.Button(pesquisa, text="Pesquisar Professor", command=pesquisar_professor).grid(row=4, column=30)

def atualizar():
    atualizar = tk.Toplevel()
    atualizar.title("Atualizar")
    atualizar.geometry("500x500")
    
    def atualizar_professor():
        atualizar_professor = tk.Toplevel()
        atualizar_professor.title("Atualizar Funcionário")
        atualizar_professor.geometry("500x400")

        Label(atualizar_professor, text="ID do Funcionário:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = Entry(atualizar_professor)
        id_entry.grid(row=0, column=1)

        escolha = tk.StringVar(value="nome")
        Label(atualizar_professor, text="O que deseja atualizar?").grid(row=1, column=0, padx=10, pady=10)
        tk.Radiobutton(atualizar_professor, text="Nome", variable=escolha, value="nome").grid(row=1, column=1)
        tk.Radiobutton(atualizar_professor, text="ID", variable=escolha, value="id").grid(row=2, column=1)

        valor_label = Label(atualizar_professor, text="Novo Nome:")
        valor_label.grid(row=3, column=0, padx=10, pady=10)
        valor_entry = Entry(atualizar_professor)
        valor_entry.grid(row=3, column=1)

        def atualizar_label():
            if escolha.get() == "nome":
                valor_label.config(text="Novo Nome:")
            elif escolha.get() == "id":
                valor_label.config(text="Novo ID:")

        escolha.trace_add("write", lambda *args: atualizar_label())

        def comando():
            id_value = id_entry.get().strip()
            novo_valor = valor_entry.get().strip()

            if not id_value:
                messagebox.showerror("Erro", "Por favor, insira o ID do funcionário.")
                return
            if not novo_valor:
                messagebox.showerror("Erro", "Por favor, insira o novo valor.")
                return
            
            if escolha.get() == "nome":
                cursor.execute("UPDATE professores SET nome = %s WHERE id = %s", (novo_valor, id_value))
            elif escolha.get() == "id":
                cursor.execute("UPDATE professores SET id = %s WHERE id = %s", (novo_valor, id_value))
            
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", "Informações do funcionário atualizadas com sucesso.")

        tk.Button(atualizar_professor, text="Atualizar", command=comando).grid(row=15, column=1)

    tk.Button(atualizar, text="Atualizar Professor", command=atualizar_professor).grid(row=4, column=30)

    def atualizar_aluno():
        atualizar_aluno = tk.Toplevel()
        atualizar_aluno.title("Atualizar Aluno")
        atualizar_aluno.geometry("500x400")

        Label(atualizar_aluno, text="ID do Aluno:").grid(row=0, column=0, padx=10, pady=10)
        id_entry = Entry(atualizar_aluno)
        id_entry.grid(row=0, column=1)

        escolha = tk.StringVar(value="nome")
        Label(atualizar_aluno, text="O que deseja atualizar?").grid(row=1, column=0, padx=10, pady=10)
        tk.Radiobutton(atualizar_aluno, text="Nome", variable=escolha, value="nome").grid(row=1, column=1)
        tk.Radiobutton(atualizar_aluno, text="ID", variable=escolha, value="id").grid(row=2, column=1)

        valor_label = Label(atualizar_aluno, text="Novo Nome:")
        valor_label.grid(row=3, column=0, padx=10, pady=10)
        valor_entry = Entry(atualizar_aluno)
        valor_entry.grid(row=3, column=1)

        def atualizar_label():
            if escolha.get() == "nome":
                valor_label.config(text="Novo Nome:")
            elif escolha.get() == "id":
                valor_label.config(text="Novo ID:")

        escolha.trace_add("write", lambda *args: atualizar_label())

        def comando():
            id_value = id_entry.get().strip()
            novo_valor = valor_entry.get().strip()

            if not id_value:
                messagebox.showerror("Erro", "Por favor, insira o ID do aluno.")
                return
            if not novo_valor:
                messagebox.showerror("Erro", "Por favor, insira o novo valor.")
                return
            
            if escolha.get() == "nome":
                cursor.execute("UPDATE aluno SET nome = %s WHERE id = %s", (novo_valor, id_value))
            elif escolha.get() == "id":
                cursor.execute("UPDATE aluno SET id = %s WHERE id = %s", (novo_valor, id_value))
            
            conexao_banco.commit()
            messagebox.showinfo("Sucesso", "Informações do aluno atualizadas com sucesso.")

        tk.Button(atualizar_aluno, text="Atualizar", command=comando).grid(row=15, column=1)

    tk.Button(atualizar, text="Atualizar Aluno", command=atualizar_aluno).grid(row=5, column=30)


tk.Button(janela, text="Cadastrar", command=cadastrar).grid(row=4, column=6)
tk.Button(janela, text="Deletar", command=deletar).grid(row=6, column=6)
tk.Button(janela, text="Pesquisar", command=pesquisa).grid(row=8, column=6)
tk.Button(janela, text="Atualizar", command=atualizar).grid(row=10, column=6)

janela.mainloop()