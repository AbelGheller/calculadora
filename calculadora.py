def soma(a, b):
    return a + b

def subtrai(a, b):
    return a - b

def multiplica(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return 'Erro: divisão por zero'
    return a / b

if __name__ == "__main__":
    print("Calculadora Simples")
    print("Operações disponíveis: soma, subtrai, multiplica, divide")
    op = input("Escolha a operação: ")
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))

    if op == "soma":
        print("Resultado:", soma(a, b))
    elif op == "subtrai":
        print("Resultado:", subtrai(a, b))
    elif op == "multiplica":
        print("Resultado:", multiplica(a, b))
    elif op == "divide":
        print("Resultado:", divide(a, b))
    else:
        print("Operação inválida.")
