def aumentar(preço=0, taxa=0, formatado=False):
    '''
        -> Calcula o aumento de um determinado preço, retornando o resultado
        com ou sem formatação.
    :param preço:  O preço informado pelo usuário;
    :param taxa: Qual é a porcentagem do aumento;
    :param formatado: Que a saída com formatação = True, senão = False ou sem parâmentro;
    :return: Retorna o valor reajustado, com ou sem formatação.
    '''
    p = preço + (preço * taxa / 100)
    return p if formatado is False else moeda(p)


def diminuir(preço=0, taxa=0, formatado=False):
    p = preço - (preço * taxa / 100)
    return p if formatado is False else moeda(p)


def dobro(preço=0, formatado=False):
    p = preço * 2
    return p if not formatado else moeda(p)


def metade(preço=0, formatado=False):
    p = preço / 2
    return p if not formatado else moeda(p)


def moeda(preço=0, moeda="R$ "):
    return f'{moeda}{preço:>6.2f}'.replace('.', ',')


def resumo(preço=0, aumento=0, diminuido=0):
    print('-' * 35)
    print('RESUMO DOS VALORES'.center(35))
    print('-' * 35)
    print(f'Preço Analisado: \t{moeda(preço)}.')
    print(f'Metade do Preço: \t{metade(preço, True)}.')
    print(f'Dobro do Preço: \t{dobro(preço, True)}.')
    print(f'{aumento} % de aumento: \t{aumentar(preço, aumento, True)}.')
    print(f'{diminuido} % de reução: \t{diminuir(preço, diminuido, True):}.')
    print('-' * 35)
