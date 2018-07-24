lista_test = [2,3,4]

def prod_lista(lista):
    product = 1
    for number in lista:
        product *= number
    return product

print(prod_lista(lista_test))
