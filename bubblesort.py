import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import randint

mpl.use('Agg')

def bubblesort(lista):
    tamanho = len(lista)
    trocas = 0
    for i in range(tamanho):
        for j in range(1, tamanho - i):
            if lista[j] < lista[j - 1]:
                aux = lista[j]
                lista[j] = lista[j - 1]
                lista[j - 1] = aux
                trocas += 1
    return trocas
    
def desenhaGrafico(x, y, figura, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Desempenho")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(figura)

def geraLista(tamanho):
    lista = []
    while tamanho > 0:
        n = randint(1, tamanho)
        lista.append(n)
        tamanho -= 1
    return lista

tamanho = [10000, 20000, 50000, 100000]
tempo = []
troca = []

for i in range(4):
    lista = geraLista(tamanho[i])
    tempo.append(timeit.timeit("bubblesort({})".format(lista), setup="from __main__ import bubblesort", number=1))
    troca.append(bubblesort(lista))

desenhaGrafico(tamanho, tempo, 'bubblesort-tempo', 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
desenhaGrafico(tamanho, troca, 'bubblesort-troca', 'Tamanho da lista', 'Quantidade de operações (swap)')
