from Classes import *
import os

def ver_quartos():
    while True:
            os.system("cls")
            print("Esses são os quartos disponiveis: ")
            print("[01] - AP Simples")
            print("[02] - AP Simples Casal")
            print("[03] - AP Duplo")
            print("[04] - AP Duplo Casal")
            print("[05] - AP Luxo")
            print("[06] - AP Master")
            print("[07] - voltar")
            menu_quartos = input("Digite o número correspondente a opção que deseja: ")
            match menu_quartos:
                case "1":
                    print("Este encantador apartamento simples é um espaço acolhedor e funcional, perfeito para quem valoriza a simplicidade e a praticidade. Localizado em um bairro tranquilo, oferece uma atmosfera serena e aconchegante, ideal para relaxar após um longo dia.")
                    os.system("pause")
                case "2":
                    print("Este charmoso apartamento simples de casal é um refúgio acolhedor e íntimo, projetado para acomodação o amor e a convivência. Localizado em um bairro tranquilo, oferece um espaço onde o conforto e a funcionalidade são de maneira harmoniosa. ")
                    os.system("pause")
                case "3":
                    print("Este moderno apartamento duplo é uma solução elegante e prática para acomodar duas pessoas com estilo e conforto. Localizado em um bairro vibrante, oferece um espaço versátil onde cada morador pode desfrutar de sua própria privacidade, ao mesmo tempo em que reúne uma atmosfera de convivência harmoniosa.")
                    os.system("pause")
                case "4":
                    print("Este encantador apartamento duplo para casal é um espaço versátil e convidativo, projetado para oferecer acomodação confortável e flexível para dois casais. Situado num bairro tranquilo e de fácil acesso, este apartamento oferece uma combinação de privacidade e convivência.")
                    os.system("pause")
                case "5":
                    print("Este requintado apartamento de luxo é um verdadeiro exemplo de elegância e sofisticação. Localizado em um dos bairros mais exclusivos da cidade, oferece vistas deslumbrantes da paisagem urbana e do horizonte. Com um design inovador contemporâneo e materiais de alta qualidade, cada detalhe deste apartamento foi cuidadosamente pensado para criar um ambiente de conforto e opulência.")
                    os.system("pause")
                case "6":
                    print("Este magnífico apartamento master redefine o conceito de luxo e exclusividade. Localizado no topo de um edifício icônico, oferece uma vista panorâmica deslumbrante da cidade que se estende até onde os olhos podem alcançar. Projetado para quem busca o auge do conforto e sofisticação, este apartamento encapsula o estilo de vida elevado.")
                    os.system("pause")
                    
                case "7":
                    print("Voltando...")
                    os.system("pause")
                    break
                
                case _:
                    print ("Opção inválida")
                    os.system("pause")
                    os.system("cls") 

def main():
    while True:
        try:
        # Tratamento de erro
            os.system("cls") 
            print("Bem-vindos a um refúgio de elegância e conforto ")
            print("[01] - Ver quartos")
            print("[02] - Realizar Hospedagem")
            print("[03] - Sair")

            menu=input("Digite o número correspondente a opção que deseja: ")
          
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