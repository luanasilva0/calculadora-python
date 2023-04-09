name = input("Qual o seu nome? ")

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def div(a, b):
    return a / b

options = ["1- Soma", "2- Subtração", "3- Multiplicação", "4- Divisão"]

def mensg():
    print("Olá",name,", qual opção você quer escolher?")
    for i in options:
        print(i)
    user_choice = input("Digite a opção: ")

    const = 0
    x = 1

    while(x >= const):

        if(user_choice == "1" or user_choice == "Soma"):
            a = float(input("Digite o primeiro número: "))
            b = float(input("Agora digite outro: "))
            print("O resultado da operação é igual a", sum(a, b))
            const = const + 1

        if(user_choice == "2" or user_choice == "Subtração"):
            a = float(input("Digite o primeiro número: "))
            b = float(input("Agora digite outro: "))
            print("O resultado da operação é igual a", sub(a, b))
            const = const + 1

        if(user_choice == "3" or user_choice == "Multiplicação"):
            a = float(input("Digite o primeiro número: "))
            b = float(input("Agora digite outro: "))
            print("O resultado da operação é igual a", mult(a, b))
            const = const + 1

        if(user_choice == "4" or user_choice == "Divisão"):
            a = float(input("Digite o primeiro número: "))
            b = float(input("Agora digite outro: "))
            print("O resultado da operação é igual a", div(a, b))
            const = const + 1

        if(x <= const):
            other = input("Deseja fazer outra operação? ")
            if(other == "Sim" or other == "sim"):
                for i in options:
                    print(i)
                user_choice = input("Digite a opção: ")
            else:
                break
mensg()