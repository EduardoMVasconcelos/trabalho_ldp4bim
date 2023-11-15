print("CALCULADORA")

print("Adição: +")
print("Subtração: -")
print("Multiplicação: *")
print("Divisão: /")

lista_adicao = []
lista_subtracao = []
lista_multiplicacao = []
lista_divisao = []

def adicao(a):
    resultado = a + b 
    return resultado

def subtracao(a):
    resultado = a - b 
    return resultado

def multiplicacao(a):
    resultado = a * b 
    return resultado

def divisao(a):
    resultado = a / b 
    return resultado

escolha = input("Deseja realizar uma operação matemática? [s ou n]: ")

while escolha == 's':
    a = float(input("Informe a: "))
    b = float(input("Informe b: "))
    operacao = input("Informe a operação: ")
    if operacao == '+':
        print(f"{a} + {b} = {adicao(a)}")
        lista_adicao.append(adicao(a))
            
    elif operacao == '-':
        print(f"{a} - {b} = {subtracao(a)}")
        lista_subtracao.append(subtracao(a))
            
    elif operacao == '*':
        print(f"{a} * {b} = {multiplicacao(a)}")
        lista_multiplicacao.append(multiplicacao(a))
            
    elif operacao == '/':
        print(f"{a} / {b} = {divisao(a)}")
        lista_divisao.append(divisao(a))
    escolha = input("Deseja realizar uma operação matemática? [s ou n]: ")
        
if escolha == 'n': 
    print("Calculadora desligada!")
    print("Histórico de resultados:")  
    print(f"Adições efetuadas: {lista_adicao}")
    print(f"Subtrações efetuadas: {lista_subtracao}")
    print(f"Multiplicações efetuadas: {lista_multiplicacao}")
    print(f"Divisões efetuadas: {lista_divisao}")