import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')


def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista


def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)


def countingsort(lista, maior):
    indice = maior + 1
    ocorrencias = [0] * indice

    for i in lista:
        ocorrencias[i] += 1

    k = 0

    for i in range(indice):
        for j in range(ocorrencias[i]):
            lista[k] = i
            k += 1

    return lista


tamanho = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo = []

for i in range(6):
    lista = geraLista(tamanho[i])
    tempo.append(timeit.timeit("countingsort({}, {})".format(lista, max(lista)), setup="from __main__ import countingsort", number=1))

desenhaGrafico(tamanho, tempo, "countingsort-tempo.png", 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
