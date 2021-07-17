import random
import matplotlib.pyplot as pyplot
def principal():
    i = int(input('Inteiro inicial do intervalo? '))
    f = int(input('Inteiro final do intervalo? '))
    num = int(input('Quantidade de escolhas? '))
    funcaoElementos(i, f, num) #chama a função num

def funcaoElementos(inicial, final , n):
    lista = []
    for i in range(n):
        elemento = random.randint(inicial, final) #escolhe numeros aleatoriamente
        lista.append(elemento) #junta os elementos na lista
    exibeContagemTextual(inicial, final, lista) #vai chamar a função que exibe o texto
    percentual(lista, final, inicial, n) #calcula o percentual e já tem o plot nela

def exibeContagemTextual(ini, fini, lis):
    for j in range(ini, fini+1): #começando do numero inicial vai ate o final pra exibir o texto
        print('{} - {}'.format(j, quantidadeNumeros(lis,j)))
        #chama a função de quantidade pra exibir a quantidade

def quantidadeNumeros(l, t): #calcula a quantidade de repetiçoes q os numeros aparecem na lista
    quant = l.count(t)
    return quant

def percentual(lista1, f1, i1, numero):
    listaplot =[]
    listanumeros = []
    media = numero / (f1 - i1 + 1)
    for k in range(i1, f1 + 1):#chama do inicio ate o fim do intervalo
        listaplot.append(((quantidadeNumeros(lista1, k) - media) / (media))*100) #coloca na lista p plotar os numeros
        listanumeros.append(k)
    print(listaplot)
    plot(listaplot, listanumeros)#chama a função plot

def plot(listaplot1, listanumeros1):
    pyplot.plot(listanumeros1, listaplot1, 'go-')  # plota valores
    pyplot.xlabel('Elementos')
    pyplot.ylabel('%')
    pyplot.show()

principal()
