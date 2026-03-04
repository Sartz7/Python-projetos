def contar_palavras(frase):
    """Conta a frequência de palavras em uma frase."""
    palavras = frase.lower().split()
    contagem = {}
    
    for palavra in palavras:
        # Remove pontuação básica
        palavra_limpa = palavra.strip('.,!?;:')
        
        if palavra_limpa:
            contagem[palavra_limpa] = contagem.get(palavra_limpa, 0) + 1
    
    return contagem