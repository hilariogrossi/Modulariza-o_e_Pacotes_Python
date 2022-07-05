def leiaDinheiro(mensagem):
    Válido = False

    while not Válido:
        entrada = str(input(mensagem)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO! \033[0;33m"{entrada}"\033[m é um Preço Inválido!')
        else:
            Válido = True
            return float(entrada)
