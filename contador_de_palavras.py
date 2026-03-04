def main():
    from contador_de_palavras import contar_palavras   
    frase = input("Digite uma frase: ").strip()
    if not frase:
        print("Erro: Nenhuma frase foi digitada.")
    else:
        resultado = contar_palavras(frase)
    if resultado:
        print("Contagem de Palavras:")
        for palavra, quantidade in resultado.items():
            print(f"{palavra}: {quantidade}")
    else:
        print("Nenhuma palavra válida foi encontrada.")
        

def limpar_texto(texto):
    texto = texto.lower()
    caracteres = ".,!?:;\"'()[]{}"
    for char in caracteres:
        texto = texto.replace(char, "")
    return texto
def contar_palavras(frase):
    frase = limpar_texto(frase)
    if not frase.strip():
        return {}
    
    palavras = frase.split()
    contagem = {}
    
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    
    return contagem

if __name__ == "__main__":    main()