from matplotlib import pyplot as plt
import math

data = [
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
]

altura = len(data)
largura = len(data[0])

#Ponto de destino
x1, y1 = 5, 1
distancias = [[math.inf for _ in range(largura)] for _ in range(altura)]

#Propagação
for x in range(largura):
    for y in range(altura):
        distancia = math.sqrt((x - x1) ** 2 + (y - y1) ** 2)
        
        if distancia < distancias[y][x]:
            distancias[y][x] = distancia

        if data[y][x] == 1:
            distancias[y][x] = math.inf


#for linha in distancias:
#    print(linha)

def adja_number(array, x, y):
    rows, cols = len(array), len(array[0])
    atual = array[y][x]
    cima = array[max(y - 1, 0)][x]
    esquerda = array[y][max(x - 1, 0)]
    direita = array[y][min(x + 1, cols - 1)]
    baixo = array[min(y + 1, rows - 1)][x]
    return [atual, cima, esquerda, direita, baixo]

x, y = 0, 9
array_caminho = [[y, x]]
array_sorted = [[x, y]]

while distancias[y][x] != 0.0:
    array = adja_number(distancias, x, y)
    menor_valor = min(array)
    index = array.index(menor_valor)

    if index == 0:
        distancias[y][x] += 99
    elif index == 1:
        distancias[y][x] += 99
        y -= 1
    elif index == 2:
        distancias[y][x] += 99
        x -= 1
    elif index == 3:
        distancias[y][x] += 99
        x += 1
    elif index == 4:
        distancias[y][x] += 99
        y += 1

    array_caminho.append([y, x])
    array_sorted.append([x, y])

array_plot = []

for item in array_sorted:
    if item not in array_plot:
        array_plot.append(item)

print(array_plot)

cor = 'blue'
plt.figure(figsize=(6, 6))
plt.imshow(data, cmap='binary')

#Plot dos pontos
for ponto in array_caminho:
    if ponto == array_caminho[0]:
        plt.plot(ponto[1], ponto[0], marker='o', markersize=10, color='red', markeredgecolor='black', linewidth=0.5)
    elif ponto == array_caminho[-1]:
        plt.plot(ponto[1], ponto[0], marker='o', markersize=10, color='green', markeredgecolor='black', linewidth=0.5)
    else:
        plt.plot(ponto[1], ponto[0], marker='o', markersize=10, color=cor, markeredgecolor='black', linewidth=0.5)

plt.show()

