from Classes import *
import os

def ver_quartos():
    while True:
        try:
            print("Os quartos")

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
                    print(" ")
                case "2":
                    print("Vo")
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
        

            
        
