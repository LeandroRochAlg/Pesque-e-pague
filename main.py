import tkinter as tk
import peixe as px

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root    #root é a main window
        self.root.geometry('300x200')

        self.menubar = tk.Menu(self.root)           #cria uma barra de menu para a janela root

        self.menuPeixe = tk.Menu(self.menubar)      #cria um menu para ser inserido na barra de menu
        self.menuComanda = tk.Menu(self.menubar)
        self.menuRelatorio = tk.Menu(self.menubar)

        # Menu Peixe
        self.menuPeixe.add_command(label="Cadastrar", command=self.controle.cadastrarPeixe)         #Botão Cadastrar
        self.menuPeixe.add_command(label="Consultar", command=self.controle.consultarPeixe)         #Botão Consultar
        self.menubar.add_cascade(label="Peixe", menu=self.menuPeixe)                                #Menu

        # Menu Comanda
        self.menuComanda.add_command(label="Fechar", command=self.controle.fecharComanda)           #Botão Fechar
        self.menubar.add_cascade(label="Comanda", menu=self.menuComanda)                            #Menu

        self.menuRelatorio.add_command(label="Faturamento", command=self.controle.gerarRelatorio)   #Botão Faturamento
        self.menubar.add_cascade(label="Relatório", menu=self.menuRelatorio)                        #Menu

        self.root.config(menu=self.menubar) #Configuração do Menu

class ControlePrincipal():
    def __init__(self):
        self.root = tk.Tk()                             #Cria a janela principal
        self.ctrlPeixe = px.CtrlPeixe(self)             #Cria o controle de peixe
        self.limite = LimitePrincipal(self.root, self)  #Cria a tela principal
        self.root.title("Pesque-Pague do Seu Zé")       #Título da janela principal
        self.root.mainloop()                            #Loop da janela principal

    #Funções dos botões do menu principal
    def cadastrarPeixe(self):
        self.ctrlPeixe.cadastrarPeixe()

    def consultarPeixe(self):
        self.ctrlPeixe.consultarPeixe()

    def fecharComanda(self):
        self.ctrlPeixe.fecharComanda()

    def gerarRelatorio(self):
        self.ctrlPeixe.gerarRelatorio()

if __name__ == '__main__':
    c = ControlePrincipal() #Cria o controle principal e inicia o programa