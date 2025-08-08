# Missão 7 – Troca de Armas
# Crie duas variáveis espada e arco com valores de nomes de armas.
# Troque os valores entre elas e exiba no console.

espada = "Excalibur"
arco = "Apollo"

espada, arco = arco, espada

print(espada)
print(arco)

auxiliar = espada
espada = arco
arco = auxiliar

print(espada)
print(arco)

# Foram criada duas variaveis, na sequencia temos uma forma pythonica de ta migrando os valores de um pro outro e exibindo logo abaixo... e no segundo exemplo com a utilização de variavel auxiliar o valor de espada fica nela e o de arco em espada e em seguida arco fico com o valor de auxiliar, assim exibindo os valores atribuidos nos inicio