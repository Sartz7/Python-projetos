valor_total = float(input("Digite o valor total da conta: "))
porcentagem_gorjeta = float(input("Digite a porcentagem da gorjeta:"))
valor_gorjeta = valor_total * (porcentagem_gorjeta / 100)
valor_final = valor_total + valor_gorjeta   
print(f"O valor da gorjeta é: R$ {valor_gorjeta:.2f}")
print(f"O valor total a ser pago é: R$ {valor_final:.2f}")