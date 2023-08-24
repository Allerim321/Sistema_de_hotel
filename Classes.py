import os
from Algoritmo import *

class Hotel:
    def listar(self):
        print ("")
    
class Quartos(Hotel):
    def reserva(self, nome, telefone, quarto, ocupado = 0):
        self.nome=nome
        self.telefone=telefone
        self.quarto=quarto

        if ocupado == 1:
            print("Um quarto está reservado")
        elif ocupado == 2:
            print("Todos os quartos estão reservados")
        

class Ap_luxo(Quartos):
    def listar_ap_luxo(self):
        banana=input("O quarto de luxo possui um amplo espaço com vista exclusiva e poltronas confortáveis.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if banana=="1":
            Quartos.ocupado+1
        else:
            os.system('cls')
            

class Ap_Master(Quartos):
    def listar_ap_master(self):
        kiwi=input("O quarto master é o mais espaçoso e com a melhor vista, contando com uma ampla varanda, poltronas confortáveis e 5 cômodos separados por portas.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if kiwi==1:
            Quartos.ocupado+1
        else:
            os.system('cls')


class Ap_Simples(Quartos):
    def listar_ap_simples(self):
        açaí=input("O apartamento simples possui um tamanho ideal para seu conforto, com uma cama de solteiro, mobílias necessárias e uma pequena varanda para apreciar a vista.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if açaí==1:
            Quartos.ocupado+1
        else:
            os.system('cls')


class Ap_Simples_casal(Quartos):
    def listar_ap_simples_casal(self):
        maçã=input("O apartamento simples de casal possui um tamanho ideal para seu conforto, com uma cama de casal, mobílias necessárias e uma pequena varanda para apreciar a vista.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if maçã==1:
            Quartos.ocupado+1
        else:
            os.system('cls')

class Ap_Duplo(Quartos):
    def listar_ap_duplo(self):
        pera=input("O apartamento duplo possui um tamanho ideal para seu conforto, com duas camas de solteiro, mobílias necessárias e uma pequena varanda para apreciar a vista.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if pera==1:
            Quartos.ocupado+1
        else:
            os.system('cls')

class Ap_Duplo_casal(Quartos):
    def listar_ap_duplo_casal(self):
        morango=input("O apartamento duplo de casal possui um tamanho ideal para seu conforto, com duas camas de casal, mobílias necessárias e uma pequena varanda para apreciar a vista.\nDigite 1 para confirmar o agendamento do quarto. Precione qualquer outra tecla para sair.")
        if morango==1:
            Quartos.ocupado+1
        else:
            os.system('cls')