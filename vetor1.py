#Você recebeu o desafio de ler um valor e criar um programa que coloque o valor lido na primeira posição de um vetor N[10].

n = int(input())



for i in range(10):

  print("N[%d] = %d" % (i, n))

  n = n * 2