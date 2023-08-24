from Classes import *
import os

def main():
    while True:
        try:
        # Tratamento de erro
           
            print("Bem-vindos a um refúgio de elegância e conforto ")
            print("[01] - AP Simples")
            print("[02] - AP Simples")
            print("[03] - AP Simples Casal")
            print("[04] - AP Simples Casal")
            print("[05] - AP Duplo")
            print("[06] - AP Duplo")
            print("[07] - AP Duplo Casal")            
            print("[08] - AP Duplo Casal")
            print("[09] - AP Luxo")
            print("[10] - AP Luxo")
            print("[11] - AP Master")
            print("[12] - AP Master")
            print("[13] - Sair")

            menu=input("Digite o número correspondente ao quarto que gostaria de visitar: ")
          
            match menu:
                case "1":
                    print("Você escolheu o AP simples algumas informações vão estar listadas abaixo: \n")
                case "2":
                    print("Você escolheu o AP Simples algumas informações vão estar listadas abaixo: \n")
                case "4, 04":
                    print("Você escolheu o AP Simples Casal algumas informações vão estar listadas abaixo: \n")
                case "5":
                    print("Você escolheu o AP Duplo algumas informações vão estar listadas abaixo: \n")
                case "6":
                    print("Você escolheu o AP Duplo algumas informações vão estar listadas abaixo: \n")
                case "7":
                    print("Você escolheu o AP Duplo Casal algumas informações vão estar listadas abaixo: \n")
                case "8":
                    print("Você escolheu o AP Duplo Casal algumas informações vão estar listadas abaixo: \n")
                case "9":
                    print("Você escolheu o AP Luxo algumas informações vão estar listadas abaixo: \n")
                case "10":
                    print("Você escolheu o AP Luxo algumas informações vão estar listadas abaixo: \n")
                case "11":
                    print("Você escolheu o AP Master algumas informações vão estar listadas abaixo: \n")
                case "12":
                    print("Você escolheu o AP Master algumas informações vão estar listadas abaixo: \n")
                    
                case "13":
                        exit()
       
                case _:
                    print ("Opção inválida")
                    os.system("pause")
                    os.system("cls") 
                # Tratamento de erro, ou seja, caso ocorra um erro fazer:

        
        
        except:
            print("Erro, opção inválida. Tente novamente.")
        

            
        
