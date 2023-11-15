print("CALCULADORA")

print("Adição: +")
print("Subtração: -")
print("Multiplicação: *")
print("Divisão: /")

lista_adicao = []
lista_subtracao = []
lista_multiplicacao = []
lista_divisao = []

def adicao(x):
    x = a + b 
    return x

def subtracao(x):
    resultado = a - b 
    return resultado

def multiplicacao(x):
    resultado = a * b 
    return resultado

def divisao(x):
    resultado = a / b 
    return resultado

escolha = input("Deseja realizar uma operação matemática? [s ou n]: ")

if escolha == 's':
    a = float(input("Informe a:"))
    b = float(input("Informe b: "))
    operacao = input("Informe a operação: ")
    if operacao == '+':
        print(f"{a} + {b} = {adicao:.2f}")