# -*- encoding: utf-8 -*-

# Com múltiplos argumentos:
'''
def multiplica(n1,n2):
    return n1 * n2

print(multiplica(10,2))
'''

# Argumentos com valor padrão:
'''
def multiplica(num1=3,num2=3):
    return num1 * num2

print(multiplica())
'''

# Com número variável de argumentos:

def multiplicaNumeros(*varArgs):
    total = 1
    for arg in varArgs:
        total *= arg
    return total
print(multiplicaNumeros(3,2,1,3,1))