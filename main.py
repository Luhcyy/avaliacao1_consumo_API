from requisicoes import obter_taxa_cambio

def converter_moeda(moeda_origem, moeda_destino, valor_a_converter):
    #Converte um valor de uma moeda para outra.
    taxa_cambio = obter_taxa_cambio(moeda_origem, moeda_destino)
    if taxa_cambio is not None:
        valor_convertido = valor_a_converter * taxa_cambio
        return valor_convertido
    else:
        return None

def main():
    #Executa o programa principal do conversor de moedas.
    while True:
        moeda_origem = input('Digite a moeda de origem (EUR, USD, BRL): ').upper()
        if moeda_origem not in ('EUR', 'USD', 'BRL'):
            print('Moeda de origem inválida.')
            continue

        moeda_destino = input('Digite a moeda de destino (EUR, USD, BRL): ').upper()
        if moeda_destino not in ('EUR', 'USD', 'BRL'):
            print('Moeda de destino inválida.')
            continue

        try:
            valor_a_converter = float(input('Digite o valor a converter: '))
        except ValueError:
            print('Valor inválido.')
            continue

        valor_convertido = converter_moeda(moeda_origem, moeda_destino, valor_a_converter)
        if valor_convertido is not None:
            print(f'{valor_a_converter:.2f} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}')
        else:
            print('Falha ao obter taxa de câmbio.')

if __name__ == '__main__':
    main()