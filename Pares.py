#Crie um programa que leia um número e mostre os números pares até esse número, inclusive ele mesmo.

n = int(input())

for i in range(1,n+1):
    if i % 2 == 0:
     print(i)