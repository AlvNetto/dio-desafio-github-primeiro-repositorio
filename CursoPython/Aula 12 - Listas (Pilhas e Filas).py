#STACK (Pilha):

'''
pilha = [0,1,2,3]
pilha.append(4)
pilha.append(5)
pilha.pop()
pilha.append(6)
pilha.pop()
print(pilha)
'''

#OBS: Utiliza os conceitos vistos na aula anterior.


#QUEUE (Fila):

from collections import deque #Importação do módulo "deque" da biblioteca do Python.

fila = deque([0,1,2,3]) #"deque" estabelece uma variável do tipo "Fila".
fila.append(4)
fila.append(5)
fila.popleft() #Remove o primeiro elemento da fila.
fila.popleft()
print(fila)


