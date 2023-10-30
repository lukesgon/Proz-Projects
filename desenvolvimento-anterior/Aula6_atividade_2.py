while True:
    try:
        nome_completo = str(input("Por favor insira seu nome completo: "))
        ano_nascimento = int(input("Por favor, insira seu ano de nascimento, de 1922 a 2023: "))
        idade = (2023 - ano_nascimento)
        if (nome_completo != ("")) and (1922 <= ano_nascimento <= 2023):
            print(f"Olá {nome_completo}, o seu nome foi registrado com sucesso.")
            print(f"O seu ano de nascimento também foi registrado com sucesso, de forma que ele indica que você completa {idade} em 2023.")
            print("Sistema finalizado")
            break
        else:
            print("Sua entrada não corresponde aos requisitos apresentados anteriormente, por favor verifique e preencha novamente.")
            continue
    except:
        print("Algum dado entrado é invalido.")
        print("Por favor verifique se o seu nome foi preenchido corretamente.")
        print("Verifique também se você inseriu APENAS NÚMEROS na entrada do seu ano de nascimento.")
        print("Tente novamente.")
        continue
