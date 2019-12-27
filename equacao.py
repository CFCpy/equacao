print('--'*5 , 'CALCULADORA DE EQUAÇÕES', '--'*5)
a= int(input('Digite o número correspondente ao A: '))
b= int(input('Digite o B: '))
c= int(input('Digite o C: '))
delta = (b**2 - 4*a*c)
bask= (-b+delta**1/2)/2
bask2= (-b -delta**1/2)/2
print(f'As raízes são : {bask} e {bask2} ')
print(f'O delta é igual a: {delta}')
print('---'*5)