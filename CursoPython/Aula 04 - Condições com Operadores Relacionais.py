#Condições com Operadores Relacionais:

n1 = 7
n2 = 2

if n1 == n2:
   print("números iguais")
elif n1 < n2:
   print("n1 menor que n2")
elif n1 > n2:
   print("n1 maior que n2")

#Outro exemplo do livro:

n1 = 5

#if 0 <= n1 <= 6:
   #print("n1")

#Agora a mesma coisa com Operadores Lógicos:

if 0 <= n1 and n1 <=6:
    print(n1)


#Exemplo criado por mim baseado no livro:

estaChovendo = False
TemSunga = False

if estaChovendo:
   print("fiqueEmCasa")
elif TemSunga:
   print("VaParaPiscina")
else:
   print("VaBrincar")


#Outro Exemplo:

MomoAma = True
MomoTriste = False

if MomoAma:
   print("MomoAma")
else:
    if MomoTriste:
       print("MomoTriste")
    else:
       print("MomoMorreu")