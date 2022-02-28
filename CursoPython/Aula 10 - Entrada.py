#Aula Entrada

#nome = input("Digite seu nome: ")
#saudacao = "Olá, " + nome
#print(saudacao)

#PREVENINDO ERROS

'''
Testa se de fato conseguimos converter o input para .int.
Se der errado, então, avisa ao usuário.
Se der certo, executa a soma.
'''

try:
    num1 = int (input("Digite o primeiro número: "))  #tenta a conversão
    num2 = int (input("Digite o segundo número: "))  #tenta a conversão também

except: #Só executa se falhar a tentativa TRY.
    print("Você deve inserir números inteiros.")

else: #Caso não execute a exceção:
    print(num1 + num2)

#OBS: Note os diversos tipos de comentários (# e ''')1, que não atrapalham a execução do código.