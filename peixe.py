import tkinter as tk
from tkinter import messagebox  #Função para mostrar uma janela de aviso

class Peixe:    #classe peixe
    def __init__(self, nome, preco):    #Construtor da classe Peixe
        self.__nome = nome
        self.__preco = preco

    #Getters
    @property
    def nome(self):
        return self.__nome
    
    @property
    def preco(self):
        return self.__preco
    
    def getPeixe(self):
        return self.__nome + " - " + self.__preco   #retorna o nome e o preço do peixe
    
class PeixeComanda: #classe adicional para melhor controle dos peixes na comanda
    def __init__(self, Peixe, peso):    #Construtor da classe PeixeComanda
        self.__Peixe = Peixe
        self.__peso = peso

    #Getters
    @property
    def Peixe(self):
        return self.__Peixe
    
    @property
    def peso(self):
        return self.__peso
    
    def getPeixeComanda(self):
        return self.__Peixe.nome + " - " + self.__peso   #retorna o nome e o peso do peixe
    
class Comanda:
    def __init__(self, listaPeixeComanda):  #Construtor da classe Comanda
        self.__listaPeixeComanda = listaPeixeComanda

    #Getters
    @property
    def listaPeixeComanda(self):
        return self.__listaPeixeComanda
    
    def getComanda(self):   #Retorna a comanda
        total = 0

        ret += "Comanda: \n"

        for peixeComanda in self.__listaPeixeComanda:   #percorre a lista de peixes da comanda peixe por peixe
            valor = peixeComanda.Peixe.preco * peixeComanda.peso    #calcula o valor cobrado pelo peixe
            total += valor                                          #soma o valor do peixe ao total
            ret += peixeComanda.getPeixeComanda() + ' - R$' + str(valor) + "\n"

        ret += "Total: R$" + str(total)
        
        return ret
    
class LimiteCadastrarPeixe(tk.Toplevel): #classe da tela de cadastro de peixe
    def __init__(self, controle):
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('250x100')        #Dimensões da janela
        self.title("Cadastrar Peixe")   #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.frameNome = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.frameNome.pack()
        self.framePreco.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelPreco = tk.Label(self.framePreco,text="Preço: ")
        self.labelNome.pack(side="left")    #Empacota o labelNome no frameNome
        self.labelPreco.pack(side="left")   #Empacota o labelPreco no framePreco  

        #Entries são usados para receber entradas de texto
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputNome.pack(side="left")    #Empacota o inputNome no frameNome
        self.inputPreco = tk.Entry(self.framePreco, width=20)
        self.inputPreco.pack(side="left")   #Empacota o inputPreco no framePreco

        #Buttons são usados para criar botões
        self.buttonSubmit = tk.Button(self.frameButton, text="Enter")       #Botão Enter
        self.buttonSubmit.pack(side="left")                                 #Empacota o botão no frameButton
        self.buttonSubmit.bind("<Button>", controle.enterHandler)           #Vincula o botão a função enterHandler

        self.buttonClear = tk.Button(self.frameButton, text="Clear")        #Botão Clear
        self.buttonClear.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonClear.bind("<Button>", controle.clearHandler)            #Vincula o botão a função clearHandler

        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")    #Botão Concluído
        self.buttonFecha.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)            #Vincula o botão a função fechaHandler

    def mostraJanela(self, titulo, msg):    #Função para mostrar uma janela de aviso
        messagebox.showinfo(titulo, msg)    #Mostra uma janela de aviso com o título e a mensagem passados como parâmetro

class LimiteConsultaPeixe(tk.Toplevel): #classe da tela de exibição da lista de peixes
    def __init__(self, controle, peixes):   #Construtor da classe LimiteConsultaPeixe
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('550x100')        #Dimensões da janela
        self.title("Consultar Peixes")  #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.framePeixe = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.framePeixe.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelPeixe = tk.Label(self.framePeixe,text="Lista de peixes:")
        self.labelPeixe.pack(side="top")   #Empacota o labelPeixe no framePeixe

        #Texts são usados para mostrar textos
        self.textPeixe = tk.Text(self.framePeixe, height=10, width=30)  #Cria um textPeixe com 25 linhas e 30 colunas
        self.textPeixe.pack(side="top")                                 #Empacota o textPeixe no framePeixe
        self.textPeixe.insert(tk.END, peixes)                           #Insere o texto com a lista de peixes no textPeixe

        #Buttons são usados para criar botões
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")    #Botão Concluído
        self.buttonFecha.pack(side="left")                                  #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)            #Vincula o botão a função fechaHandler

class LimiteFechaComanda(tk.Toplevel): #classe da tela de fechamento da comanda
    def __init__(self, controle, peixes): #Construtor da classe LimiteFechaComanda
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('550x100')        #Dimensões da janela
        self.title("Fechar Comanda")    #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.framePeixe = tk.Frame(self)
        self.framePeso = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.framePeixe.pack()
        self.framePeso.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelPeixe = tk.Label(self.framePeixe,text="Peixe: ")
        self.labelPeso = tk.Label(self.framePeso,text="Peso: ")
        self.labelPeixe.pack(side="left")   #Empacota o labelPeixe no framePeixe
        self.labelPeso.pack(side="left")    #Empacota o labelPeso no framePeso

        #ComboBoxes são usados para criar caixas de seleção
        self.escolhaPeixe = tk.StringVar()                                                  #Cria uma variável para armazenar a escolha do peixe
        self.comboboxPeixe = tk.OptionMenu(self.framePeixe, width = 15, values = peixes)    #Cria uma combobox com as opções da lista de peixes
        self.comboboxPeixe.pack(side="left")                                                #Empacota a combobox no framePeixe

        #Entries são usados para receber entradas de texto
        self.inputPeso = tk.Entry(self.framePeso, width=20)
        self.inputPeso.pack(side="left")    #Empacota o inputPeso no framePeso

        #Buttons são usados para criar botões
        self.buttonAdd = tk.Button(self.frameButton, text="Adiciona Peixe")         #Botão Adiciona Peixe
        self.buttonAdd.pack(side="left")                                            #Empacota o botão no frameButton
        self.buttonAdd.bind("<Button>", controle.adicionaPeixeHandler)              #Vincula o botão a função adicionaPeixeHandler

        self.buttonFecha = tk.Button(self.frameButton, text="Fecha Comanda")        #Botão Concluído
        self.buttonFecha.pack(side="left")                                          #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaComandaHandler)             #Vincula o botão a função fechaHandler

    def mostraJanela(self, titulo, msg):    #Função para mostrar uma janela de aviso
        messagebox.showinfo(titulo, msg)    #Mostra uma janela de aviso com o título e a mensagem passados como parâmetro

class LimiteRelatorio(tk.Toplevel): #classe da tela de exibição do relatório
    def __init__(self, controle, relatorio): #Construtor da classe LimiteRelatorio
        tk.Toplevel.__init__(self)      #Construtor da classe Toplevel (janela)
        self.geometry('550x100')        #Dimensões da janela
        self.title("Relatório")         #Título da janela
        self.controle = controle        #Controle da janela

        #Frames são usados para organizar os widgets
        self.frameRelatorio = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        #Empacota os frames
        self.frameRelatorio.pack()
        self.frameButton.pack()

        #Labels são usados para mostrar textos
        self.labelRelatorio = tk.Label(self.frameRelatorio,text="Relatório:")
        self.labelRelatorio.pack(side="top")   #Empacota o labelRelatorio no frameRelatorio

        #Texts são usados para mostrar textos
        self.textRelatorio = tk.Text(self.frameRelatorio, height=10, width=30)  #Cria um textRelatorio com 25 linhas e 30 colunas
        self.textRelatorio.pack(side="top")                                     #Empacota o textRelatorio no frameRelatorio
        self.textRelatorio.insert(tk.END, relatorio)                            #Insere o texto com o relatório no textRelatorio

        #Buttons são usados para criar botões
        self.buttonFecha = tk.Button(self.frameButton, text="Concluído")        #Botão Concluído
        self.buttonFecha.pack(side="left")                                      #Empacota o botão no frameButton
        self.buttonFecha.bind("<Button>", controle.fechaHandler)                #Vincula o botão a função fechaHandler