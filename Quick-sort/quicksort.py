import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.use('Agg')


def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista invertida")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)


def listaDecrescente(tamanho):
    lista = list(range(1, tamanho + 1))
    lista.reverse()
    return lista


def quicksort(lista, inicial, final):
    tamanho = final - inicial + 1
    pilha = [0] * (tamanho)
    topo = -1
    topo = topo + 1
    pilha[topo] = inicial
    topo = topo + 1
    pilha[topo] = final

    while topo >= 0:
        final = pilha[topo]
        topo = topo - 1
        inicial = pilha[topo]
        topo = topo - 1
        pivo = particionar(lista, inicial, final)

        if pivo - 1 > inicial:
            topo = topo + 1
            pilha[topo] = inicial
            topo = topo + 1
            pilha[topo] = pivo - 1

        if pivo + 1 < final:
            topo = topo + 1
            pilha[topo] = pivo + 1
            topo = topo + 1
            pilha[topo] = final


def particionar(lista, inicial, final):
    i = (inicial - 1)
    pivo = lista[final]

    for j in range(inicial, final):
        if lista[j] <= pivo:
            i = i + 1
            aux = lista[i]
            lista[i] = lista[j]
            lista[j] = aux

    aux = lista[i+1]
    lista[i+1] = lista[final]
    lista[final] = aux
    return i + 1


tamanho = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo = []

for i in range(6):
    lista = listaDecrescente(tamanho[i])
    tempo.append(timeit.timeit("quicksort({}, {}, {})".format(lista, 0, len(lista) - 1), setup="from __main__ import quicksort", number=1))

desenhaGrafico(tamanho, tempo, "quicksort-tempo.png", 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
