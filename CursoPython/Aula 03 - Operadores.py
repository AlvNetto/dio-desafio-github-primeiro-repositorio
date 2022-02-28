#OPERADORES
print("\n---------------\nOPERADORES UNÁRIOS")

print("Operador '~' : ",~4)
print("Operador '+' : ",+4)
print("Operador '-' : ",-(-4))

meuInt = +3
meuInt = -meuInt
print(meuInt)


#OPERADOR ARITMÉTICO
print("\n-------------------\nOPERADORES ARITMÉTICOS")
x = 7
y = 2

print("Operador '+' : ", x+y)
print("Operador '-' : ", x-y)
print("Operador '*' : ", x*y)
print("Operador '**' : ", x**y)
print("Operador '/' : ", x/y)
print("Operador '//' : ", x//y)
print("Operador '%' : ", x%y)

print( ((3+4)*2)/3 )



#OPERADORES RELACIONAIS
print("\n-------------------\nOPERADORES RELACIONAIS")

print("Op. Relacional x == y : ", x==y)
print("Op. Relacional x != y : ", x!=y)
print("Op. Relacional x < y : ", x<y)
print("Op. Relacional x > y : ", x>y)
print("Op. Relacional x >= y : ", x>=y)
print("Op. Relacional x <= y : ", x<=y)


#OPERADORES LÓGICOS
print("\n-------------------\nOPERADORES LÓGICOS")

v = True
f = False

print("Op. Lógico v and f : ", v and f)
print("Op. Lógico v or f : ", v or f)
print("Op. Lógico v and not f : ", v and not f)


#OPERADORES DE ATRIBUIÇÃO
print("\n-------------------\nOPERADORES DE ATRIBUIÇÃO")

print("Op. de Atribuição x = y")
x = y
print("x: ", x)
print("y: ", y)


print("Op. de Atribuição x += y")
#x = x + y
#x += y
print("x: ", x)
print("y: ", y)


print("Op. de Atribuição x -= y")
#x = x - y
#x -= y
print("x: ", x)
print("y: ", y)


print("Op. de Atribuição x *= y")
x = x * y
#x *= y
print("x: ", x)
print("y: ", y)



#OPERADORES DE ATRIBUIÇÃO
print("\n-------------------\nOPERADORES DE ATRIBUIÇÃO")

#1. expoentes e unário
print(-2**2)
print(2**-2)

#2. Aritméticos. primeiro divisões e multiplicação, depois + e -

print(1+3/3*1)

#3. Depois de comparação, seguido de igualdade

print(False != 3 > 2)

#4. Por fim, operadores lógicos

print(False != 3 > 2 and True)
