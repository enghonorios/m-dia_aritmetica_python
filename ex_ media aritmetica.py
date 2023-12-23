# Desenvolva um programa que leia as 3 notas de um aluno, calcule e mostre a média

n01= int(input('Nota do trimestre: '))
n02= int(input('Nota do semestre: '))
n03= int(input('Nota do quadrimestre: '))

resultado= n01+n02+n03
média= resultado/3

print(f'A soma das notas é igual {resultado}')
print(f'Sua média foi igual {média:.2f}')
