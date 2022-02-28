# -*- encoding: utf-8 -*-

#SEM ARGUMENTO:

'''
def PrimeiraFunc():
    print("Esta é a minha primeira função.")
    print("Ela é bem simples.")
    print("Somente imprime algumas coisas.")

PrimeiraFunc()
PrimeiraFunc()
PrimeiraFunc()
'''

#COM ARGUMENTO:
'''
def ola(nome):
    print("Olá, ",nome)
    print("Como você vai?")

ola("Netto")
'''

#COM RETORNO:

def adicionaDois(numero):
    numero += 2
    return numero

inteiro = 98
inteiro = adicionaDois(inteiro)

print(inteiro)

#OBS: usa-se o "return" quando se quer atribuir o resultado da função à variável.
