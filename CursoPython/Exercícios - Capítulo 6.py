'''
lista = []
for i in range(5):
    lista.append( 5* int(input("Entre com um numero: ")))
print(lista)
'''

'''
lista = []
for i in range(10):
    numero = int(input("Entre com um numero: "))
    existe = False
    for num in lista:
        if numero == num:
            existe = True
            break
        if not existe:
            lista.append( numero)
print("Lista ",lista)
'''

'''
lista = []
for i in range(10):
    numero = int(input("Entre com um numero:"))
    lista.append( numero)

maiorNumero = lista[0]
for numero in lista:
    if numero > maiorNumero:
        maiorNumero = numero
print("Maior numero",maiorNumero)
'''

lista1 = [3,4,5,6,7]
lista2 = [0,1,2,3,4]
lista3 = []
for i in lista1:
    existe = False
    for j in lista2:
        if i == j:
            existe = True
            break
        if not existe:
            lista3.append(i)
for i in lista2:
    existe = False
    for j in lista1:
        if i == j:
            existe = True
            break
        if not existe:
            lista3.append(i)
print(lista3)
