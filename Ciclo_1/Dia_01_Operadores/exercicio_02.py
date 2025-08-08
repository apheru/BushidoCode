# Missão 2 – O Ouro Dividido
# Você tem 100 moedas de ouro e precisa dividir igualmente entre 4 aliados.
# Calcule quantas moedas cada um recebe e quantas sobram.

gold_coins = 100
allies = 4

coins_per_ally = gold_coins // allies
coins_left = gold_coins % allies

print(coins_per_ally)
print(coins_left)


# Usei divisão inteira // e resto % para mostrar quantas moedas cada um recebe e o que sobra.
