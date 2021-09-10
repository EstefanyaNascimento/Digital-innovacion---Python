#Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. 
# Em caso positivo, calcule o perímetro do triângulo e apresente a mensagem:
#Perimetro = XX.X
#Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem


a,b,c=list(map(float,input().split()))

if(a<b+c and b < a + c and c < a + b):

   print("Perimetro = %0.1f"%(a + b + c))

else:

   print("Area = %0.1f"%((c * (a + b)) / 2))