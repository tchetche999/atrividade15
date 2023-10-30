# Exercício Python 15: Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo. 
#DICA: PESQUISE E ENTENDA SOBRE DESIGUALDADE TRIANGULAR
reta1 = int(input("insira o comprimento da primeira reta:"))
reta2 = int(input("insira o comprimento da segunda reta:"))
reta3 = int(input("insira o comprimento da terceira reta"))
result = (reta2 + reta3)
if reta1 < result:
    print("pode ser formado um triangulo")
else:
    print("não pode ser formado um triangulo")