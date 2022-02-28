#Gerando listas

#lista = [1,1.5,True,"texto",[0,1]]
#lista[1]=3.0
#print(lista)

'''
lista = [0,1,2,3,4,5,6,7,8]
lista4 = lista[0:4]
listaSliceLen = lista[4:len(lista)] #De 4 até o final da lista.
listaPares = lista[0:len(lista):2] #De 0 até o final da lista, porém pulando de 2 em 2.
listaCopiada = lista[0:len(lista)]
listaCopy = lista.copy()
print(lista)
print(lista4)
print(listaSliceLen)
print(listaPares)
print(listaCopiada)
print(listaCopy)
'''

#Consultando posição de elementos da lista:

#lista = [0,1,2,3,4,5,1000,7,8]
#lista.index(1000)
#print(lista.index(1000))


#Inserindo valores:

#lista = [0,1]
#lista.append(3) #Adiciona elemento no final da lista.
#lista.insert(0,4) #Adiciona elemento na posição desejada.
#lista += [4,5,6] #Concatenar listas
#print(lista)


#Removendo valores:

#lista = [0,1,0,1]
#lista.remove(1)
#print(lista)

#lista = [0,1,0,1]
#lista.pop(2) #Remove o item da posição 2.
#lista.pop() #Remove o último item da lista.
#print(lista)

#lista = [0,1,0,1]
#del lista[2] #Remove o item da posição 2.
#print(lista)


#Ordenando valores:

lista = [4,10,1,0,2,3,0]
lista.sort() #Ordena de maneira crescente.
lista.reverse() #Ordena de maneira invertida.
print(lista)






