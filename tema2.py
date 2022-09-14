def creare_lista():
    n = int(input('Nr. de elemente = '))
    lista_locala = []
    for i in range(n):
        elem = float(input('Elementul '+str(i)+' este:'))
        lista_locala.append(elem)
    return lista_locala
lista1 = creare_lista()
print(lista1)