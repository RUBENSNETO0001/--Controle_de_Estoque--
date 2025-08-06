from tkinter import *
from funcoes.adicionar import adicionar

class Aplicativo:
    def __init__(self, master=None):
        self.master = master
        master.title("Controle de Estoque")
        
        # Configuração padrão
        self.fontePadrao = ("Calibri", "10")
        
        # Container principal
        self.widget1 = Frame(master)
        self.widget1.pack(pady=10)
        
        # Container para o formulário (vazio inicialmente)
        self.segundoContainer = Frame(master)
        self.segundoContainer.pack(fill=BOTH, expand=True)
        
        # Botão para adicionar
        Button(self.widget1,
              text="Adicionar",
              font=self.fontePadrao,
              width=10,
              command=self.chamar_adicionar).pack(side=LEFT, padx=5)
        
        # Botão para sair
        Button(self.widget1,
              text="Sair",
              font=self.fontePadrao,
              width=10,
              command=master.quit).pack(side=LEFT, padx=5)
    
    def chamar_adicionar(self):
        adicionar(self)

root = Tk()
app = Aplicativo(root)
root.geometry("400x200")
root.mainloop()