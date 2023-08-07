def reajuste(salario, dependentes):
    novoSalario = 0
    if salario >= 0 and salario <= 500:
        novoSalario = salario * 1.30 + (25 * dependentes)
    elif salario > 500 and salario <= 1000:
        novoSalario = salario * 1.20 + (25 * dependentes)
    elif salario > 1000:
        novoSalario = salario * 1.10  + (25 * dependentes)
    diferencaSalarial = novoSalario - salario
    print(novoSalario)
    print(diferencaSalarial)


def folhaPag():
    nome = str(input("nome do funcinário: "))
    salario = float(input("salário do funcionário: "))
    dependentes = int(input("número de filhos: "))
    reajuste(salario, dependentes)

def main():
    while True:
        print("Menu")
        print("Digite um número positivo para continuar")
        print("Ou um número negativo para encerrar")
        opcao = float(input("Número: "))
        if opcao < 0:
            break
        else:
            folhaPag()

main()
