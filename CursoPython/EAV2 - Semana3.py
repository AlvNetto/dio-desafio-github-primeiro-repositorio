'''
Script para calcular média de dois valores inteiros inseridos pelo usuário e apresente o resultado na tela.
'''

#variáveis (guardar informações)
#operadores aritmeticos (Ex: somar/dividir)
#input (entrada de dados e a leitura de dados de entrada)

'''
#Exemplo 1:
print('--- Programa de Cálculo de Média ---')
primNumero = int (input ('Digite o primeiro valor:'))
segNumero = int (input ('Digite o segundo valor:'))
média = (primNumero + segNumero)/2
print(f'A média entre {primNumero} e {segNumero} é igual à {média}')
'''

'''
#Exemplo 2:
print('--- Conversão de C para F ---')
tempCel = float (input ("Digite a temperatura: "))
print(f'A temperatura {tempCel} em Celsius corresponde a {(9*tempCel + 160)/5} em Fahrenheit')
'''

'''
#Exemplo 3:

print('--- Aferição de Paridade ---')
valor = int(input('Digite um valor inteiro: '))
if valor%2 == 0:
    print(f'O valor {valor} é PAR')
else:
    print(f'O valor {valor} é ÍMPAR')
'''

#Exemplo 4:

'''
Receber 2 números entre 0 e 10 que representem notas de alunos.
Com base nas notas, apresente na tela a seguinte situação:

- Aprovado
- Apto Final
- Reprovado

ORIENTAÇÕES:
1- O aluno está aprovado se sua média for maior ou igual a sete.
2- O aluno está apto para a prova final se sua média for entre quatro e sete.
3- O aluno está reprovado se a sua média for menor que quatro.
'''

print('--- SITUAÇÃO ACADÊMICA ---')
Primnota =float(input('Digite sua primeira nota: '))
Segnota =float(input('Digite sua segunda nota: '))
media = (Primnota + Segnota)/2
#print(f'Média: {media}')

if media >=7:
    print (f'ALUNO APROVADO COM MÉDIA {media}')
elif media <4:
    print (f'ALUNO REPROVADO COM MÉDIA {media}')
else:
    print(f'ALUNO APTO A FINAL COM MÉDIA {media}')