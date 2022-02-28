#COMANDO PRINT:

#nome = "Luiz"
#sobrenome = "Veloso"
#print("Nome",nome+" "+sobrenome, sep=": ")

#FORMATAR VARIAVEIS:

#idade = 88.344432

#print("Idade: %d" % idade) #Mostrar idade como número inteiro.
#print("Idade: %f" % idade) #Mostrar idade como fração.
#print("Idade: %.1f" % idade) #Mostrar idade como fração em apenas uma casa decimal.
#print("Idade: %.2f" % idade) #Mostrar idade como fração com duas casas decimais.

#COMO IMPRIMIR A SAÍDA DO ARQUIVO:

#arquivo = open("ARQUIVO.txt","w")
#print("NOSSO PRIMEIRO ARQUIVO SALVO.", file=arquivo)
#arquivo.close()

'''
arquivo = open("ARQUIVO.txt","a")
print("NOSSA SEGUNDA LINHA SALVA.", file=arquivo)
arquivo.close()
'''

#OBS: "w" Cria um arquivo onde é escrita a string desejada.
# O "a" adiciona uma informação no arquivo.

'''
a = 1
b = 2
print("a=",a,end=' ')
print("e b=",b)
'''

print("a=%s" % "a")
print("a=%f" % 1.5324)
print("%s=%f" % ("a",1.5324))
