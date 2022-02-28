#Criando listas em uma única linha:

#ista = []
#for i in range(11):
#    lista.append(2*i)
#print(lista)

#OU:

#lista = [i*2 for i in range(11)]
#print(lista)

#Listas aninhadas:

#Transposição de matriz (transformar colunas em linhas e vice-versa).

matriz = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
'''
transposta = []
for i in range(4):
    linhaTransposta = []
    for linha in matriz:
        linhaTransposta.append(linha[i])
        transposta.append(linhaTransposta)
        print(transposta)
'''

#OU:

'''
transposta = []
for i in range(4):
    transposta.append([linha[i]for linha in matriz])
    print(transposta)
'''

#OU:

transposta = [[linha[i]for linha in matriz] for i in range(4)]
print(transposta)

#Estou com dúvidas na Compreensão de Listas (principalmente aninhadas).