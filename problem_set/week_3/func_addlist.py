lista_test = [1,2,3]

def add_lista(lista):
    suma = 0
    for number in lista:
        suma += number
    return suma

print(add_lista(lista_test))

print ('Using the sum function, i get: ' + str(sum(iter(lista_test))))
