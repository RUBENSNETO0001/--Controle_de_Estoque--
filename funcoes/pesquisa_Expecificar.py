from tkinter import messagebox, Label, Frame, Entry, Button, LEFT, Scrollbar, Listbox, RIGHT, Y, END
from bd.bd import conectar, fechar_conexao

def pesquisa_Expecificar(app):
    # Limpa o container
    for widget in app.segundoContainer.winfo_children():
        widget.destroy()
    
    form_container = Frame(app.segundoContainer)
    form_container.pack(pady=10)
    
    Label(form_container, text="Pesquisar Produto", font=app.fontePadrao).pack(pady=5)
    frame = Frame(form_container)
    frame.pack(pady=5)
    
    entry = Entry(frame, width=30, font=app.fontePadrao)
    entry.pack(side=LEFT, padx=5)
    
    app.entries = {"nome": entry}
    
    Button(
        form_container, 
        text="Confirmar", 
        font=app.fontePadrao,
        command=lambda: valida_prod(app)
    ).pack(pady=10)
    
    # Listbox para exibir resultados
    listbox_frame = Frame(app.segundoContainer)
    listbox_frame.pack(pady=10)

    scrollbar = Scrollbar(listbox_frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    app.listbox = Listbox(listbox_frame, width=80, yscrollcommand=scrollbar.set)
    app.listbox.pack(side=LEFT, fill=Y)

    scrollbar.config(command=app.listbox.yview)

def valida_prod(app):
    nome = app.entries["nome"].get().strip()
    if not nome:
        messagebox.showwarning("Aviso", "Digite um nome para pesquisar.")
        return
    
    conexao = conectar()
    if conexao:
        try: 
            cursor = conexao.cursor()
            query = "SELECT * FROM estoque WHERE nome_produto = %s"
            cursor.execute(query, (nome,))
            regis = cursor.fetchall()
            
            app.listbox.delete(0, END)
            
            if not regis:
                app.listbox.insert(END, "Nenhum produto encontrado.")
            else:
                for linha in regis:
                    item_formatado = f"ID: {linha[0]} | Nome: {linha[1]} | Quantidade: {linha[2]} | Preço: R${linha[3]:.2f}"
                    app.listbox.insert(END, item_formatado)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar produtos: {str(e)}")
        finally:
            fechar_conexao(conexao, cursor)