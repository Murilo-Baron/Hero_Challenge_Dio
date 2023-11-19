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
