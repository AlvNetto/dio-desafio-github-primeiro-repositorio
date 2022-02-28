#Exemplo da vídeo-aula:

#Operadores Lógicos: or e and

nota = 70
presenca = 60

if nota < 70 or presenca < 70:
    print("Você foi reprovado!")

    if nota < 70:
        print("Tente melhorar sua nota ano que vem!")
    if presenca < 70:
        print ("Você deve frequentar as aulas!")

else:
    print("Você foi aprovado!")

    if nota == 100 and presenca == 100:
        print("Com louvor!")

#OBS: Dúvida sobre o comando pass, citado no livro (pág. 49).