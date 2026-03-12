import random  
print("Bem-vindo ao jogo de adivinhação!")

def jogo_adivinha():
    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
            palpite = int(input("Tente adivinhar o número (1-100): "))

            if not 1 <= palpite <= 100:
                raise ValueError("O número deve estar entre 1 e 100.")
            
            tentativas +=1  

            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")

            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")

            else:
                print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas!")
            break
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, tente novamente.")

jogo_adivinha() 