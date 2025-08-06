from tkinter import messagebox, Label, Frame, Entry, Button, LEFT
from bd.bd import conectar, fechar_conexao

def adicionar(app):
    # Limpa o container
    for widget in app.segundoContainer.winfo_children():
        widget.destroy()
    
    form_container = Frame(app.segundoContainer)
    form_container.pack(pady=10)
    
    # Campos do formulário
    campos = [
        ("Nome do Produto", "nomePROD"),
        ("Preço (R$)", "precoPROD"), 
        ("Quantidade", "quantidadePROD")
    ]
    
    app.entries = {}
    
    for label_text, var_name in campos:
        Label(form_container, text=label_text, font=app.fontePadrao).pack(pady=5)
        frame = Frame(form_container)
        frame.pack(pady=5)
        entry = Entry(frame, width=30, font=app.fontePadrao)
        entry.pack(side=LEFT, padx=5)
        app.entries[var_name] = entry
    
    Button(form_container, 
          text="Confirmar", 
          font=app.fontePadrao,
          command=lambda: validar_entrada(app)).pack(pady=10)

def validar_entrada(app):
    nome = app.entries["nomePROD"].get().strip()
    preco = app.entries["precoPROD"].get().strip()
    quantidade = app.entries["quantidadePROD"].get().strip()
    
    if not all([nome, preco, quantidade]):
        messagebox.showwarning("Aviso", "Todos os campos devem ser preenchidos!")
        return
    
    try:
        preco_float = float(preco)
        quantidade_int = int(quantidade)
        
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            
            # Query segura com parâmetros
            query = "INSERT INTO estoque (nome_produto, preco, quantidade_Prod) VALUES (%s, %s, %s)"
            valores = (nome, preco_float, quantidade_int)
            
            cursor.execute(query, valores)
            conexao.commit()
            
            messagebox.showinfo("Sucesso", 
                f"Produto '{nome}' (R${preco_float:.2f}) - {quantidade_int} un. adicionado!")
            
            # Limpa campos
            for entry in app.entries.values():
                entry.delete(0, 'end')
                
    except ValueError as e:
        if "float" in str(e):
            messagebox.showerror("Erro", "O preço deve ser um número válido!")
        else:
            messagebox.showerror("Erro", "A quantidade deve ser um número inteiro!")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro: {str(e)}")
    finally:
        if 'cursor' in locals():
            fechar_conexao(conexao, cursor)