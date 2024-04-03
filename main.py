from requisicoes import obter_taxa_cambio

def converter_moeda(moeda_origem, moeda_destino, valor_a_converter):
    taxa_cambio = obter_taxa_cambio(moeda_origem, moeda_destino)
    return valor_a_converter * taxa_cambio if taxa_cambio else None

def mostrar_menu():
    print('\n$$$ Conversor de Moedas $$$')
    print('1. Converter Moeda')
    print('2. Sair')
    while True:
        opcao = input('Digite a opção desejada: \n')
        if opcao in ('1', '2'):
            return opcao
        else:
            print('Opção inválida. Tente novamente.')

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            # Converter moeda
            moeda_origem = input('Digite a moeda de origem (EUR, USD, BRL): \n').upper()
            if moeda_origem not in ('EUR', 'USD', 'BRL'):
                print('Moeda de origem inválida.')
                continue

            moeda_destino = input('Digite a moeda de destino (EUR, USD, BRL): \n').upper()
            if moeda_destino not in ('EUR', 'USD', 'BRL'):
                print('Moeda de destino inválida.')
                continue

            try:
                valor_a_converter = float(input('Digite o valor a converter: \n'))
            except ValueError:
                print('Valor inválido.')
                continue

            valor_convertido = converter_moeda(moeda_origem, moeda_destino, valor_a_converter)
            if valor_convertido is not None:
                print(f'{valor_a_converter:.2f} {moeda_origem} equivale a {valor_convertido:.2f} {moeda_destino}')
            else:
                print('Falha ao obter taxa de câmbio.')

        elif opcao == '2':
            # Sair do programa
            print('Saindo do conversor de moedas...')
            break

        else:
            print('Opção inválida.')

if __name__ == '__main__':
    main()
