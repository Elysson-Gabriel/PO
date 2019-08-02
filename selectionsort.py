import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def selectionsort(lista):
    comparacoes = 0
    for i in range(len(lista)):
        trocou = False
        menor = i
        for j in range(i + 1, len(lista)):
            comparacoes += 1
            if lista[menor] > lista[j]:
                trocou = True
                menor = j
        if trocou:
            aux = lista[i]
            lista[i] = lista[menor]
            lista[menor] = aux
    return comparacoes

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
troca = []
tempo2 = []
troca2 = []

for i in range(4):
    lista = geraLista(tamanho[i])
    lista2 = listaDecrescente(tamanho[i])
    tempo.append(timeit.timeit("selectionsort({})".format(lista), setup="from __main__ import selectionsort", number=1))
    troca.append(selectionsort(lista))
    tempo2.append(timeit.timeit("selectionsort({})".format(lista2), setup="from __main__ import selectionsort", number=1))
    troca2.append(selectionsort(lista2))

desenhaGrafico(tamanho, tempo, tempo2, 'selectionsort-tempo.png', 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
desenhaGrafico(tamanho, troca, troca2, 'selectionsort-troca.png', 'Tamanho da lista', 'Quantidade de comparações')
