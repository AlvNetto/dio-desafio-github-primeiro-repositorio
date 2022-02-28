#Questão 1:
'''
nome = input("Nome: ")
cidade = input("Cidade: ")
anodenascimento = int(input("Ano de nascimento: "))
print (nome)
print (cidade)
print (2021 - anodenascimento)
'''

#Questão 2:
'''
celsius = int(input("Digire a temperatura em Celsius que você gostaria de converter: "))

fahrenheit = 9.0/5.0 * celsius + 32 #formula específica para esta conversão

print("Temperatura: ", celsius, "Celsius = ", fahrenheit, "F")
'''

#Questão 3:
'''
Mark = 9.0
Marcio = "DEZ"
Maria = 4.5
João = 7.0

print("ALUNO(A)     NOTA")
print("Mark        ",Mark)
print("Marcio      ",Marcio)
print("Maria       ",Maria)
print("João        ",João)
'''

#OU USANDO TABULAÇÕES:

'''
print("ALUNO (A)","NOTA",sep='\t')
print(9*"=",5*"=",sep='\t')
print("Mark","9.0",sep='\t\t')
print("Marcio","DEZ",sep='\t\t')
print("Maria","4.5",sep='\t\t')
print("João","7.0",sep='\t\t')
'''

#Questão 4:
'''
tamanho = int(input ("Digite o tamanho do quadrado: "))
for i in range (tamanho): #para fazer uma iteração/repetição dos elementos "i".
    print(tamanho * "X")
'''
#Duvida no comando "for i in range", na linha 48.


#Questão 5:
'''
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

if numero1 > numero2:
    print(numero2,numero1)
else:
    print(numero1,numero2)
'''

#Questão 6:
'''
character = ""
imprimir = ""

while character != "*": #!= significa "diferente".
    character = input("Digite um caracter (digite * para terminar): ")
    imprimir += character #+= significa "x = x + valor".

print(imprimir)
'''

#Questão 7:

'''
#SEM O ARQUIVO:

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

if 0 == numero1%numero2:
    print(numero1," é múltiplo de ",numero2)
else:
    print(numero1," não é múltiplo de ",numero2)
'''

#COM O ARQUIVO:

numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

arquivo = open("texto.txt","w")

if 0 == numero1%numero2:
    print("primeiro numero é multiplo do segundo", file=arquivo)
else:
    print("primeiro numero não é multiplo do segundo", file=arquivo)
arquivo.close()
