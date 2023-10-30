while True:
    try:
        num = int(input("Por favor, escreva um número de 1 a 100: "))
        if 1 <= num <= 100:
            print(f"Parabéns, você escreveu o número: {num}")
            break
        else:
            print("O número digitado não está entre 1 e 100.")
            continue
    except:
        print("Você precisa inserir um número inteiro (sem virgula ou ponto). Também é necessário que não haja letras em sua entrada.")
        continue

while True:
    try:
        num_2 = int(input("Por favor, insira um número de 1 a 100, que seja divisível por 2: "))
        num_2_div = int(num_2/2)
        if (1 <= (num_2%2 == 0) <= 100):
            print(f"Parabéns, você escreveu o número {num_2}")
            print(f"A divisão do seu número por 2 é: {num_2_div}")
            break
        else:
            print("O número escrito não atende os requisitos pré-determinados, tente novamente.")
    except:
        print("Você não digitou uma entrada válida.")
        print("Certifique-se que sua entrada é um número inteiro, sem uso de virgula ou ponto, e que letras não tenham sido digitadas.")

while True:
    try:
        num_3 = int(input("Por favor, insira um número de 1 a 100, que seja divisível por 3: "))
        num_3_div = int(num_3/3)
        if (1 <= (num_3%3 == 0) <= 100):
            print(f"Parabéns, você escreveu o número {num_3}")
            print(f"A divisão do seu número por 2 é: {num_3_div}")
            break
        else:
            print("O número escrito não atende os requisitos pré-determinados, tente novamente.")
    except:
        print("Você não digitou uma entrada válida.")
        print("Certifique-se que sua entrada é um número inteiro, sem uso de virgula ou ponto, e que letras não tenham sido digitadas.")