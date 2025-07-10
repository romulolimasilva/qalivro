""" 01 - Implementar duas funções:
- Uma que converta temperatrura em graus Celsius para Fahrenheit.
- Outra que converta temperatura em graus Fahrenheit para Celsius.
Lembrandoi que:
F = 9/5.C + 32
"""

def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(celsius_para_fahrenheit(10))
print(fahrenheit_para_celsius(70))

""" 2 - Implementar uma função que retorne verdadeiro se o numero for primo(falso caso contrario). 
 Testar de 1 a 100"""

print("--------")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if not n % i:
            return False
    else:
        return True

# Para x de 1  a 100
for x in range(1, 100):
    if is_prime(x):
        print(x)
