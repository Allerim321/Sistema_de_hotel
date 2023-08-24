from Classes import *
import os

def ver_quartos():
    while True:
        try:
            print("Esses são os quartos disponiveis: ")
            print("[01] - AP Simples")
            print("[02] - AP Simples Casal")
            print("[03] - AP Duplo")
            print("[04] - AP Duplo Casal")
            print("[05] - AP Luxo")
            print("[06] - AP Master")
            print("[07] - voltar")

            quarto=(input("Digite a opção que deseja: "))

            match quarto:
                case "1":
                    ver_quartos
                case "2":
                    ver_quartos
                case "3":
                    ver_quartos
                case "4":
                    ver_quartos
                case "5":
                    ver_quartos
                case "6":
                

                    break
                    
                case _:
                    print ("Opção inválida")
            
            os.system("pause")
            os.system("cls")
            break   
        except:
            print("Erro, opção inválida. Tente novamente.")
            os.system("pause")
            os.system("cls")

def main():
    while True:
        try:
        # Tratamento de erro
           
            print("Bem-vindos a um refúgio de elegância e conforto ")
            print("[01] - Ver quartos")
            print("[02] - Realizar Hospedagem")
            print("[03] - Sair")

            menu=input("Digite o número correspondente ao quarto que gostaria de visitar: ")
          
            match menu:
                case "1":
                    ver_quartos()
                case "2":
                    print("Você escolheu a opção pra realizar a hospedagem de um quarto \n esses são os quartos disponiveis \n")
                case "3":
                    print("Saindo...")
                    os.system("pause")
                    break
                    
                case _:
                    print ("Opção inválida")
                    os.system("pause")
                    os.system("cls") 
                # Tratamento de erro, ou seja, caso ocorra um erro fazer:

        
        
        except:
            print("Erro, opção inválida. Tente novamente.")
            os.system("pause")
            os.system("cls") 
        

            
        
