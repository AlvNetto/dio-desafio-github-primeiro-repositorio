# -*- encoding: utf-8 -*-

#Exemplo de Lambda:

'''
f = lambda x,y: x*y
print(f(2,4))

#OBS: Note que não precisa de "return", pois a instrução é sempre devolvida.
'''

#Com argumento padrão:

'''
f = lambda x,y=3: x*y
print(f(2))
'''

#Lambda explicitando argumentos:

'''
f = lambda x,y,w: x*y*w
print(f(w=2,y=3,x=1))
'''

#Escopo de função:
'''
def tres():
    x=3

x=2
tres()
print(x)

#OBS: A função tem suas variáveis próprias dentro dela.
#Neste caso a função não faz nada além de criar uma variável x dentro da própria função, não impactando no código, que já tem uma outra variável com mesmo nome (x), mas com valor diferente.
'''

#Documentando funções:

def somaTres(x):
    """Soma três à variável passada como entrada"""

    x+=3
print(somaTres.__doc__)



