#Imprima uma linha contendo o número da pessoa que Theon deve dizer ser seu algoz. 
# Se existe mais de uma resposta possível, imprima a menor.

import sys

N = int(input())
pessoas = sys.stdin.readline().split()
lowest_pos = 0

for i in range(N):
  if i == 0:
    lowest = pessoas[i]
    continue
  if  pessoas[i] < lowest:
    lowest = pessoas[i]
    lowest_pos = i
    
print(lowest_pos + 1)