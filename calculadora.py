import os

def voltar_ao_menu_principal():
    input("\nDigite uma tecla para voltar ao menu principal: \n")
    main() 

def opcao_invalida():
    os.system("clear")
    print("Opção inválida\n")
    voltar_ao_menu_principal()

            
def calcular_soma():
    os.system("clear")
    numero1=int(input("Defina o primeiro número: "))
    os.system("clear")
    numero2=int(input ("Defina o segundo número: "))
    os.system("clear")
    print (f"O resultado da operação é: {numero1 + numero2}")
    voltar_ao_menu_principal()

def calcular_subtracao():
    os.system("clear")
    numero1=int(input("Defina o primeiro número: "))
    os.system("clear")
    numero2=int(input ("Defina o segundo número: "))
    os.system("clear")
    print (f"O resultado da operação é: {numero1 - numero2}")
    voltar_ao_menu_principal()

def calcular_multiplicacao():
    os.system("clear")
    numero1=int(input("Defina o primeiro número: "))
    os.system("clear")
    numero2=int(input ("Defina o segundo número: "))
    os.system("clear")
    print (f"O resultado da operação é: {numero1 * numero2}")
    voltar_ao_menu_principal()

def calcular_divisao():
    os.system("clear")
    numero1=int(input("Defina o primeiro número: "))
    os.system("clear")
    numero2=int(input ("Defina o segundo número: "))
    os.system("clear")
    print (f"O resultado da operação é: {numero1 / numero2}")
    voltar_ao_menu_principal()

def nome_app():
    print('''
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
─██████████████─██████████████─██████─────────██████████████─██████──██████─██████─────────██████████████─████████████───██████████████─████████████████───██████████████─
─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██████████─██░░██████░░██─██░░██─────────██░░██████████─██░░██──██░░██─██░░██─────────██░░██████░░██─██░░████░░░░██─██░░██████░░██─██░░████████░░██───██░░██████░░██─
─██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
─██░░██─────────██░░██████░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░████████░░██───██░░██████░░██─
─██░░██─────────██░░░░░░░░░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░░░░░░░░░██─██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██─────────██░░██████░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░██████░░██─██░░██──██░░██─██░░██──██░░██─██░░██████░░████───██░░██████░░██─
─██░░██─────────██░░██──██░░██─██░░██─────────██░░██─────────██░░██──██░░██─██░░██─────────██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
─██░░██████████─██░░██──██░░██─██░░██████████─██░░██████████─██░░██████░░██─██░░██████████─██░░██──██░░██─██░░████░░░░██─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░████─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─
─██████████████─██████──██████─██████████████─██████████████─██████████████─██████████████─██████──██████─████████████───██████████████─██████──██████████─██████──██████─
──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────''')

def exibir_opcoes():
    print("\n1 - Calcular soma entre dois números")
    print("2 - Calcular subtração entre dois números")
    print("3 - Calcular multiplicação entre dois números")
    print("4 - Calcular divisão entre dois números\n")

def escolher_opcoes():
    try:
        escolha=int(input("Escolha uma opção: "))
        if escolha == 1:
            calcular_soma()
        elif escolha == 2:
            calcular_subtracao()
        elif escolha == 3:
            calcular_multiplicacao()
        elif escolha == 4:
            calcular_divisao()
        else:
            opcao_invalida()

    except:
        opcao_invalida()

def main():
    os.system("clear")
    nome_app()
    exibir_opcoes()
    escolher_opcoes()

if __name__=="__main__":
    main()
