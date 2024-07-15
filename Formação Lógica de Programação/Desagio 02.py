#Calculadora de Partidas Rankeadas

# Função para calcular o saldo de vitórias e determinar o nível do jogador
def calcular_nivel(vitorias, derrotas):
    saldo_vitorias = vitorias - derrotas

    if vitorias < 10:
        nivel = "Ferro"
    elif 11 <= vitorias <= 20:
        nivel = "Bronze"
    elif 21 <= vitorias <= 50:
        nivel = "Prata"
    elif 51 <= vitorias <= 80:
        nivel = "Ouro"
    elif 81 <= vitorias <= 90:
        nivel = "Diamante"
    elif 91 <= vitorias <= 100:
        nivel = "Lendário"
    else:
        nivel = "Imortal"

    return saldo_vitorias, nivel

# Solicitar a quantidade de vitórias e derrotas ao usuário
vitorias = int(input("Digite a quantidade de vitórias: "))
derrotas = int(input("Digite a quantidade de derrotas: "))

# Chamar a função e armazenar os resultados
saldo_vitorias, nivel = calcular_nivel(vitorias, derrotas)

# Exibir o resultado
print(f"O Herói tem um saldo de {saldo_vitorias} e está no nível de {nivel}")
