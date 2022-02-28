print("BREAK:")
for numero in range(5,11):
    if numero == 7:
        break
    print(numero)

numero1 = 0

while 1:
    numero1 += 3
    if numero1 >= 100:
        break
    else:
        print(numero1)


print("CONTINUE:")
for numero in range(5,11):
    if numero == 7:
        continue
    print(numero)