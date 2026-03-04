def contar_vogais(texto):
    """Conta o número de vogais em um texto."""
    vogais = "aeiouáéíóú"
    contador = 0
    
    for letra in texto.lower():
        if letra in vogais:
            contador += 1
    
    return contador

texto=input("Digite um texto: ")   
print(f"O número de vogais no texto é: {contar_vogais(texto)} vogais.")
