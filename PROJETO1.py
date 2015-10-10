#esta função devolve o valor mais alto da lista ou tuplo que foi inserida
def maximo(lista):
    if len(lista) == 0:
        return 0
    max_act = lista[0]
    
    for i in lista:
        if i > max_act:
            max_act = i
            
    return max_act

#esta função devolve o indice do valor mais alto da lista ou tuplo que foi inserida
#e de notar que devolve sempre uma lista com o indice mais alto e no caso de existir
#dois maximos devolve os seus indices também em forma de lista

def max_indice(lista):
    if len(lista) == 0:
        return 0
    nr_max = maximo(lista)
    lista_indice = []
    
    for i in range(len(lista)):
        if lista[i] == nr_max:
            lista_indice = lista_indice + [i, ]
            
    return lista_indice

def mandatos(nr_mandatos, nr_votos):
    list_votos = list(nr_votos)
    list_mandatos = []
    
    for candidatura in range(len(nr_votos)):
        list_mandatos = list_mandatos + [0]

    for cada_mandato in range(nr_mandatos):

        if len(max_indice(list_votos)) == 1:
            i = max_indice(list_votos)[0]
            list_mandatos[i] = list_mandatos[i] + 1
            list_votos[i] = nr_votos[i] / (list_mandatos[i] + 1)
            
        elif len(max_indice(list_votos)) >= 2:               #esta parte é para o caso de existirem empates.
            list_indice = max_indice(list_votos)             #se o numero de votos inicial for igual da o mandato
            i = list_indice[0]                               #para a candidatura mais a direita
            for indice in range(len(list_indice)):
                if nr_votos[indice] <= nr_votos[i]:
                    i = list_indice[indice]
            list_mandatos[i] = list_mandatos[i] + 1
            list_votos[i] = nr_votos[i] / (list_mandatos[i] + 1)            
            
    return tuple(list_mandatos)
            