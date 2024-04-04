# avaliacao1_consumo_API

## Conversor de Moedas em Python

### Descrição

<p>Este programa Python permite converter valores entre diferentes moedas, utilizando a API Exchange Rates.</p>
<p>Professor aplicante: <a href: https://github.com/orlandosaraivajr>Orlando Saraiva jr</a></p>
<br>
<p>As tecnologias usadas foram:</p>
<ul>
  <li>Python3</li>
  <li>Exchange Rates API</li>
</ul>
<hr>

### Funcionalidades

#### Conversão de Moeda:
<ul>
  <li>Converta valores entre EUR, USD e BRL.</li>
  <li>Insira o valor a ser convertido e a moeda de origem e destino.</li>
  <li>O programa exibe o valor convertido com duas casas decimais.</li>
</ul>
<h4> Menu interativo:</h4>
<ul>
  <li>Escolha entre converter moeda ou sair do programa.</li>
  <li>O menu utiliza um loop while True para repetir até que o usuário escolha sair.</li>
  <li>A função mostrar_menu exibe as opções e valida a entrada do usuário.</li>
</ul>
<h4> Tratamento de erros:</h4>
<ul>
  <li>O código verifica se a moeda de origem e destino são válidas.</li>
  <li>O código verifica se o valor a ser convertido é um número válido.</li>
  <li>O programa exibe o valor convertido com duas casas decimais.</li>
</ul>
<hr>
<h3> Requisitos</h3>
<ul>
  <li>Python 3.x instalado</li>
  <li>Biblioteca requests instalada: pip install requests</li>
  <li>Chave API da Exchange Rates: https://www.exchangerate-api.com/</li>
</ul>
<hr>
<h3>Como Usar</h3>
<h4>Obtenha a Chave API</h4>
<ul>
  <li>Crie uma conta gratuita na Exchange Rates: https://www.exchangerate-api.com/</li>
  <li>Obtenha sua chave API no painel da sua conta.</li>
</ul>
<h4>Configure o Script: </h4>
<ul>
  <li>Abra o arquivo config.py e substitua SUA_API_KEY_AQUI pela sua chave API.</li>
</ul>
<h4>Execute o Script: </h4>
<ul>
  <li>Abra um terminal ou prompt de comando.</li>
  <li>Navegue até o diretório do projeto.</li>
  <li>Execute o seguinte comando:</li>
</ul>

```
python conversor.py
```
<h3>Exemplos de Uso:</h3>

```
python conversor.py

--- Conversor de Moedas ---

1. Converter Moeda
2. Sair

Digite a opção desejada: 1

Digite a moeda de origem (EUR, USD, BRL): USD
Digite a moeda de destino (EUR, USD, BRL): EUR
Digite o valor a converter: 100

100.00 USD equivale a 92.20 EUR

Digite a opção desejada: 2

Saindo do conversor de moedas...
```

<h4>Observações</h4>
<ul>
  <li>A taxa de câmbio é obtida em tempo real da API Exchange Rates.</li>
  <li>O código pode ser adaptado para incluir mais moedas ou funcionalidades.</li>
</ul>
