#A seguinte sequência de números 0 1 1 2 3 5 8 13 21...é conhecida como série de Fibonacci. 
#Nessa sequência, cada número, depois dos 2 primeiros, é igual à soma dos 2 anteriores. 
#Escreva um algoritmo que leia um inteiro N (N < 46) e mostre os N primeiros números dessa série.

n = int(input())

fib_list = [ ]

a=1 

b=0

for i in range(n ):

  c=a+b 

  a=b 

  b=c

  fib_list.append(str(a))

  fib_string = ' '.join(fib_list)

print(fib_string)