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

print("--------")

""" 3 - Implementar uma função que receba uma lista de listas de comprimentos quaisquer e
retorne uma lista de uma dimensão. """

def flatten(it):
    """
    "Achata a lista"
    """
    # Se for uma lista
    if isinstance(it, list):
        Is = []

        # Para cada item da lista
        for item in it:
            # Evoca flatten() recursivamente
            Is = Is + flatten(item)
        return Is
    else:
        return [it]

# Teste
a = [[1, [2, 3]], [4, [5, 6]]]
print(flatten(a))

print("--------")

""" 4 -  Implementar uma função que receba um dicionario e retorne um dicionario
 e retorne a soma, a média e a variação dos valores"""

def stat(dic):
    # Soma
    s = sum(dic.values())
    # Media
    med = s / len(dic.values())
    # Variação
    var = max(dic.values()) - min(dic.values())
    return s, med, var

print(stat({1: 1, 2: 2, 3: 3, 4: 4, 5: 5}))

print("--------")

""" 5 - Escreva uma função que:
 - Receba uma frase como parametro.
 - Retorne umanova frase com cada palavra com as letras invertidas.
 Solução"""

def reverse1(t):
    """Usando um loop convencional.
    """
    r = t.split()
    for i in range(len(r)):
        r[i] = r[i][::-1]
    return ' '.join(r)

def reverse2(t):
    """Usando list comprehension."""
    return ' '.join([s[::-1] for s in t.split()])

f = 'Romulo'
print(reverse1(f))
print(reverse2(f))

print("--------")

""" 6 - Crie uma função que:
- Receba uma lista de tuplas (dados), um inteiro (chave, zero por padrão igual) e um booleano (reverso, falso por padrão).
- Retorne dados ordenados pelo item incicado pela chave e em ordem decrescente se reverso for verdadeiro."""

def ord_tab(dados, chave=0, reverso=False):
    # Rotina para extrair a chave para comparação
    dados.sort(key=lambda x: x[chave], reverse=reverso)
    return dados

# Testes
t = [(1, 2, 0), (3, 1, 5), (0, 3, 3)]
print(ord_tab(t))        # Ordena pelo primeiro elemento
print(ord_tab(t, 1))     # Ordena pelo segundo elemento
print(ord_tab(t, 2))     # Ordena pelo terceiro elemento


