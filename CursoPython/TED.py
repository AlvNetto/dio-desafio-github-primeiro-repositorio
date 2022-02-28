# -*- encoding: utf-8 -*-

print("\n === Calcule a média === \n")

def medias(nota1,nota2,nota3,caract):
    if caract == "A" or caract == "a":
        return((nota1 + nota2 + nota3) / 3)
    elif caract == "P" or caract == "p":
        return(((nota1*5) + (nota2*3) + (nota3*2)) / (5 + 3 + 2))
    elif caract == "H" or caract == "h":
        return(3 / ((1/nota1) + (1/nota2) + (1/nota3)))
    else:
        print("O tipo de média digitado é inválido. Digite A, P ou H.")
        exit()

while True:
    perg1 = float(input("Digite a primeira nota: "))
    perg2 = float(input("Digite a segunda nota: "))
    perg3 = float(input("Digite a terceira nota: "))
    perg4 = str(input("Digite o tipo de média que deseja calcular (A, P ou H)?"))

    resposta = medias(perg1, perg2, perg3, perg4)

    print("A média é:", resposta)

    repetir = str(input("Deseja realizar novo cálculo (S ou N)? "))

    if repetir == "N" or repetir == "n":
        print("\nAplicação finalizada!")
        exit()

    print("\nReiniciando a aplicação...\n")



