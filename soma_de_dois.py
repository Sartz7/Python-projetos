def somar(a, b):
    return a + b
try:
    Numero1 = float(input("Digite o primeiro número: "))
    Numero2 = float(input("Digite o segundo número: "))

    resultado = somar(Numero1, Numero2)
    print("A soma dos dois números é: ", resultado)

except ValueError:
    print("Erro: Por favor, insira números válidos.")
