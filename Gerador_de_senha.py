import random
import string

def gerar_senha(comprimento=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

if __name__ == "__main__":
    senha = gerar_senha()
    print(f"Senha gerada: {senha}")