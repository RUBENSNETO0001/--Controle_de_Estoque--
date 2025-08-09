from tkinter import messagebox, Label, Frame, Entry, Button, LEFT
from bd.bd import conectar, fechar_conexao

def remover(app):
    # Limpa o container
    for widget in app.segundoContainer.winfo_children():
        widget.destroy()
    
    form_container = Frame(app.segundoContainer)
    form_container.pack(pady=10)
    
    Label(form_container, text="Remover Produto", font=app.fontePadrao).pack(pady=5)
    frame = Frame(form_container)
    frame.pack(pady=5)
    
    entry = Entry(frame, width=30, font=app.fontePadrao)
    entry.pack(side=LEFT, padx=5)
    
    # Guarda o entry em app.entries para acesso posterior
    app.entries = {"nome": entry}
    
    Button(
        form_container, 
        text="Confirmar", 
        font=app.fontePadrao,
        command=lambda: valida_remocao(app)
    ).pack(pady=10)

def valida_remocao(app):
    nome = app.entries["nome"].get().strip()
    
    if not nome:
        messagebox.showwarning("Aviso", "O campo deve ser preenchido!")
        return
    
    try:
        conexao = conectar()
        if conexao:
            cursor = conexao.cursor()
            query = "DELETE FROM estoque WHERE nome_produto = %s"
            cursor.execute(query, (nome,))
            conexao.commit()
            
            if cursor.rowcount > 0:
                messagebox.showinfo("Sucesso", f"Produto '{nome}' removido com sucesso!")
            else:
                messagebox.showwarning("Aviso", f"O produto '{nome}' não foi encontrado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao remover: {str(e)}")
    finally:
        if 'cursor' in locals():
            fechar_conexao(conexao, cursor)