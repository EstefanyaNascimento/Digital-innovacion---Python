#Leia quatro números (N1, N2, N3, N4), cada um deles com uma casa decimal, correspondente às quatro notas de um aluno. 
# Calcule a média com pesos 2, 3, 4 e 1, respectivamente, para cada uma destas notas e 
# mostre esta média acompanhada pela mensagem "Media:

n1, n2, n3, n4 = input().split() # Entrada das notas

n1 = float(n1) # nota 1 em float e atribue a variável = n1

n2 = float(n2) # nota 2 em float e atribue a variável = n2

n3 = float(n3) # nota 3 em float e atribue a variável = n3

n4 = float(n4) # nota 4 em float e atribue a variável = n4

media = ((n1*2) + (n2*3) + (n3*4) + (n4*1))/10 # Atribui o peso de cada nota e calcular a média



print(f'Media: {media:.1f}') # exibe a média na tela

if media > 7.0: # Se esta média for maior que 7.0

 print('Aluno aprovado.') # exibe a média e o resultado na tela

elif media <= 4.9: # caso a média tenha ficado 4.9 ou menos

   print('Aluno reprovado.') # exibe o resultado na tela

elif 5.0 <= media <= 6.9: # Se a média calculada for um valor entre 5.0 e 6.9

 print('Aluno em exame.') # exibe o resultado na tela



 n5 = float(input()) # entrada da nota de exame

 media = (n5 + media) / 2 # calcula a nova média



 print(f'Nota do exame: {n5:.1f}') # exibe a nota

 if media >= 5: # se a nota for maior ou igual a 5.0, aluno aprovado

   print('Aluno aprovado.') # exibe o resultado na tela

 else: # caso a nota NÃO seja maior ou igual a 5.0, aluno reprovado

   print('Aluno reprovado') # exibe o resultado na tela

 print(f'Media final: {media:.1f}') # exibe a média final