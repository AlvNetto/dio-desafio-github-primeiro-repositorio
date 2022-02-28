#DECLARANDO VARIÁVEIS
print("\n---------------------\nDECLARANDO VARIÁVEIS")

X = 5
x = 7
print(x)



#TIPO INTEIRO
print("\n-----------_\nTIPO INTEIRO")

print(x)
print(type(x))



#TIPO FLOAT
print("\n-----------\nTIPO FLOAT")

pontoFlutuante = 3.5222

print(pontoFlutuante)
print(type(pontoFlutuante))



#TIPO BOOL
print("\n---------\nTIPO BOOL")

booleano = False

print(booleano)
print(type(booleano))



#TIPO STRING
print("\n-------------\nTIPO STRING")

texto = "TESTE"

print(texto)
print(type(texto))



#CONVERSÃO ENTRE TIPOS
print("\n----------------------\nCONVERSÃO ENTRE TIPOS")

numero1 = 1
texto2 = "2"
#numero1 + texto2

numero2 = int(texto2)
print(numero2)
print(type(numero2))
print(numero1 + numero2)



floatParaInt = int(1.0)
intParaTexto = str(10) # "10"
textoParaFloat = float("2.5") # 2.5

print("-----------------------")
print()

print(type(floatParaInt))
print("Netto"+intParaTexto)
print(type(textoParaFloat))
