texto = input("Digite um texto: ")

palavras_longas = []

for palavra in texto.split():
    if len(palavra) > 10:
        palavras_longas.append(palavra)

if palavras_longas:
    print("Palavras com mais de 10 caracteres:")
    for palavra in palavras_longas:
        print(palavra) 

else: print("Nenhuma palavra com mais de 10 caracteres foi encontrada.") 
