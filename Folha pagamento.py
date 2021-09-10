#Escreva um programa que leia o número de um colaborador, seu número de horas trabalhadas, 
# o valor que recebe por hora e calcula o salário desse colaborador. Em seguida, 
# apresente o número e o salário do colaborador, com duas casas decimais.


empregados = int(input())
horas_recebidas = int(input())
horas_trabalhadas = float(input())
salario = horas_trabalhadas * horas_recebidas

print(f"NUMBER = {empregados}")
print(f"SALARY = U$ {salario: .2f}")