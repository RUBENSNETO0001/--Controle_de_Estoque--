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

                # Campo para adicionar quantidade
                form_qtd = Frame(app.segundoContainer)
                form_qtd.pack(pady=5)

                Label(form_qtd, text="Adicionar Quantidade:", font=app.fontePadrao).pack(side=LEFT, padx=5)

                qtd_entry = Entry(form_qtd, width=10, font=app.fontePadrao)
                qtd_entry.pack(side=LEFT, padx=5)

                Button(
                    form_qtd,
                    text="Atualizar Estoque",
                    font=app.fontePadrao,
                    command=lambda: atualizar_quantidade(nome, qtd_entry.get())
                ).pack(side=LEFT, padx=5)
                
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao buscar produtos: {str(e)}")
        finally:
            fechar_conexao(conexao, cursor)


def atualizar_quantidade(nome, qtd):
    try:
        qtd = int(qtd)
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido para quantidade.")
        return

    conexao = conectar()
    if conexao:
        try:
            cursor = conexao.cursor()
            query = "UPDATE estoque SET quantidade_produto = quantidade_produto + %s WHERE nome_produto = %s"
            cursor.execute(query, (qtd, nome))
            conexao.commit()
            messagebox.showinfo("Sucesso", "Quantidade atualizada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao atualizar produto: {str(e)}")
        finally:
            fechar_conexao(conexao, cursor)
