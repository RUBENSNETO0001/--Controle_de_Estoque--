from tkinter import messagebox, Label, Frame, Entry, Button, LEFT, Scrollbar, Listbox, RIGHT, Y, END
from bd.bd import conectar, fechar_conexao

def pesquisar_Produtos(listbox): 
    """
    Função que busca produtos no banco de dados e exibe em uma Listbox
    
    Parâmetros:
    - listbox: widget Tkinter onde os resultados serão exibidos
    """ 
    conexao = conectar()
    if conexao:
        try: 
            cursor = conexao.cursor()
            query = "SELECT * FROM estoque"
            
            cursor.execute(query)
            regis = cursor.fetchall()
            
            listbox.delete(0, END)  # Corrigido: listbox em minúsculo
            
            for linha in regis:
                item_formatado = f"ID: {linha[0]} | Nome: {linha[1]} | Quantidade: {linha[2]} | Preço: R${linha[3]:.2f}"
                listbox.insert(END, item_formatado)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar produtos: {str(e)}")
        finally:
            fechar_conexao(conexao, cursor)
        
        
def pesquisar(app):
    form_container = Frame(app.segundoContainer)
    form_container.pack(pady=10, fill='both', expand=True)
    
    Label(form_container, text="Lista de Produtos", font=app.fontePadrao).pack(pady=5)
    
    list_frame = Frame(form_container)
    list_frame.pack(fill='both', expand=True, padx=10, pady=5)
    
    scrollbar = Scrollbar(list_frame)
    scrollbar.pack(side=RIGHT, fill=Y)
    
    listbox = Listbox(
        list_frame, 
        yscrollcommand=scrollbar.set,
        width=80,
        height=15,
        font=('Arial', 10)
    )
    listbox.pack(side=LEFT, fill='both', expand=True)
    
    scrollbar.config(command=listbox.yview)
    
    btn_frame = Frame(form_container)
    btn_frame.pack(pady=5)
     
    Button(
        btn_frame, 
        text="Atualizar Lista", 
        font=app.fontePadrao,
        command=lambda: pesquisar_Produtos(listbox)
    ).pack()
    
    
    pesquisar_Produtos(listbox)