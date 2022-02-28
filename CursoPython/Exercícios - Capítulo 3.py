numero1 = -1

if numero1 > 0:
    print("numero1 positivo")
elif numero1 < 0:
    print("numero1 negativo")
else:
    print("numero1 é igual a zero")



numero1 = 1

if (numero1%2) == 0:
    print("numero1 par")
else:
    print("numero1 impar")


hora = 20

if 6 < hora < 12:
    print("Bom dia!")
elif 12 < hora < 18:
    print("Boa tarde!")
else:
    print("Boa noite!")


nota1 = 4.0
nota2 = 5.5

media = (nota1+nota2)/2

print("Media:",media)

if media >= 7.0:
    print("Aprovado!")
else:
    print("Reprovado!")

if media >= 9.0:
    print("Conceito A")
elif 8.0 <= media <= 9.0:
    print("Conceito B")
elif 7.0 <= media < 8.0:
    print("Conceito C")
elif 5.0 <= media <= 7.0:
    print("Conceito D")
else:
    print("Conceito E")

