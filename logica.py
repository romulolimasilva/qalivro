"#-*-coding:<encoding>-*#-"
numero1 = 1
numero2 = 2
numero3 = 3

if numero1 >= numero2 and numero1 >= numero3:
    maior_numero = numero1
elif numero2>= numero1 and numero2 >= numero3:
    maior_numero = numero2
else:
    maior_numero = numero3

print(maior_numero)

# Primeira forma de resolver 
ano = 2021
bisexto = 4
validar = ano % bisexto
if ano / bisexto and validar == 0:
    print('Ano bisexto')
else: 
    print('Ano não bisexto')
    
# Segunda forma de resolver
ano = 2024

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print('Ano bisexto')
        else: 
            print('Ano não bisexto')
    else:
        print('Ano bisexto')
else:
    print('Ano não bisexto')

# Calculando a media  
nota1 = 7
nota2 = 6
nota3 = 8

media = (nota1 + nota2 + nota3) / 3

print(media)

# Outra forma de resolver o calculo da media:
numeros = [7, 6, 8, 9, 5]
soma = 0
tamanho = 0

for numero in numeros:
    soma += numero
    tamanho += 1

media = soma / tamanho
print('A media é: ', media)

"""Problem 4: Escreva um programa para imprimir os números 
de 1 a 100, mas com uma condição: se o número for múltiplo de 3,
imprima "Fizz" em vez do número, e se o número for múltiplo de 5, 
imprima "Buzz" em vez do número. Se o número for múltiplo de ambos 3 e 5,
imprima "FizzBuzz" em vez do número."""

numeros = range(1, 101)

for numero in numeros:
    if numero % 3 == 0 and numero % 5 == 0:
        print('FizzBuzz')
    elif numero % 3 == 0:
        print('Fizz')
    elif numero % 5 == 0:
        print('Buzz')
    else:
        print(numero)
        
"""Escreva um programa para imprimir a tabela de multiplicação
de um número escolhido pelo usuário."""

multiplique = int(input('Qual número deseja multiplicar? '))

# Tabuada de multiplicar
for i in range(1, 11):
    print(multiplique, 'x', i, '=', multiplique * i)
    
"""Escreva um programa para verificar se um número é primo."""

primo = int(input('Qual número deseja verificar? '))

for i in range(2, primo):
    if primo % i == 0:
        print('O número ', primo, ' não é primo')
        break
else:
    print('O número ', primo, ' é primo')
        
        
        
        