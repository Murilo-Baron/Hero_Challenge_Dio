# Desafio Classificador de nível de Herói
Este projeto é uma solução para o Desafio Classificador de nível de Herói, onde um herói é classificado em diferentes níveis com base na quantidade de experiência (XP) que ele possui.

# Como Utilizar
Clone o repositório:

git clone https://github.com/seu-usuario/desafio-classificador-heroi.git

# Navegue até o diretório do projeto:

cd desafio-classificador-heroi

# Execute o código Python:

python src/main.py

# Siga as instruções para inserir o nome e a quantidade de XP do herói.

O programa exibirá uma mensagem indicando o nível do herói com base na XP fornecida.

# estrutura do Repositório

README.md: Descrição do projeto, instruções de uso e informações gerais.
src/main.py: Código-fonte principal em Python.
LICENSE: Licença do projeto (pode ser escolhida conforme a necessidade).
CONTRIBUTING.md: Diretrizes para contribuição ao projeto (opcional, dependendo da complexidade do projeto).
docs/: Pasta para documentação adicional, se necessário.

Código-fonte em Python (src/main.py)

# Desafio Classificador de nível de Herói

# Solicita o nome e a quantidade de experiência (XP) do herói
nome_heroi = input("Digite o nome do Herói: ")
xp_heroi = int(input("Digite a quantidade de XP do Herói: "))

# Utiliza uma estrutura de decisão para determinar o nível do herói com base na quantidade de XP
if xp_heroi < 1000:
    nivel = "Ferro"
elif 1001 <= xp_heroi <= 2000:
    nivel = "Bronze"
elif 2001 <= xp_heroi <= 5000:
    nivel = "Prata"
elif 6001 <= xp_heroi <= 7000:
    nivel = "Ouro"
elif 7001 <= xp_heroi <= 8000:
    nivel = "Platina"
elif 8001 <= xp_heroi <= 9000:
    nivel = "Ascendente"
elif 9001 <= xp_heroi <= 10000:
    nivel = "Imortal"
else:
    nivel = "Radiante"

# Exibe a mensagem com o nome do herói e seu nível
print(f"O Herói de nome {nome_heroi} está no nível de {nivel}")

Contribuição
Contribuições são bem-vindas. Para maiores detalhes, consulte o arquivo CONTRIBUTING.md.

Licença
Este projeto está licenciado sob a Licença MIT.