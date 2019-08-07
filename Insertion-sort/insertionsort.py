import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')


def insertionsort(lista):
    interacoes = 0
    for i in range(1, len(lista)):
        atual = lista[i]
        j = i - 1
        while j >= 0 and atual < lista[j]:
            interacoes += 1
            lista[j + 1] = lista[j]
            j -= 1
        interacoes += 1
        lista[j + 1] = atual
    return interacoes


def desenhaGrafico(x, y, y2, figura, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista aleatória")
    ax.plot(x, y2, label="Lista invertida")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(figura)


def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista


def listaDecrescente(tamanho):
    lista = list(range(1, tamanho + 1))
    lista.reverse()
    return lista


tamanho = [10000, 20000, 50000, 100000]
tempo = []
interacoes = []
tempo2 = []
interacoes2 = []

for i in range(4):
    lista = geraLista(tamanho[i])
    lista2 = listaDecrescente(tamanho[i])
    tempo.append(timeit.timeit("insertionsort({})".format(lista), setup="from __main__ import insertionsort", number=1))
    interacoes.append(insertionsort(lista))
    tempo2.append(timeit.timeit("insertionsort({})".format(lista2), setup="from __main__ import insertionsort", number=1))
    interacoes2.append(insertionsort(lista2))

desenhaGrafico(tamanho, tempo, tempo2, 'insertionsort-tempo.png', 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
desenhaGrafico(tamanho, interacoes, interacoes2, 'insertionsort-interacoes.png', 'Tamanho da lista', 'Quantidade de interacoes')
