def fib(n):
    """Fibonacci
    fib(n) = fib(n - 1) + fib(n - 2) se n > 1
    fb(n) = 1 se n <= 1 """

    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return 1

# Mostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print(fib(i))


def fib(n):
    """Fibonacci:
    fib(n) = fib(n - 1) + fib(n -2 ) se n > 1
    fib(n) = 1 se n <= 1"""

    # Dois primeiros valores
    l = [1, 1]

    # calculando os outros valores
    for i in range(2, n + 1):
        l.append(l[i -1] + l[i -2])
    return l[n]

# Mostrar Fibonacci de 1 a 5
for i in [1, 2, 3, 4, 5]:
    print(i, '->', fib(i))


# -*- coding: latin1 -*-
def rgb_html(r=0, g=0, b=0):
    """Converte R, G, B em #RRGGBB"""
    return '#%02x%02x%02x' % (r, g, b)

def html_rgb(color='#000000'):
    """Converte #RRGGBB em R, G, B"""

    if color.startswith('#'): color = color[1:]

    r = int(color[:2], 16)
    g = int(color[2:4], 16)
    b = int(color[4:], 16)
    return r, g, b

#print(rgb_html(200, 200, 255))
#print(html_rgb(b=200, g=200, r=255))
#print(html_rgb('#c*c8ff'))

# *args - argumentos sem nome (lista)
# **kargs - argumentos com nome (dicionario)

def func(*args, **kargs):
    print(args)
    print(kargs)

func('peso', 10, unidade="kg")

# -*- coding: latin1 -*-

dados = [(4, 3), (5, 1), (7, 2), (9, 0)]

# Comparando pelo ultimo elemento
def _cmp(x, y):
    return cmp(x[-1], y[-1])

print('Lista:', dados)

# Ordena usando _cmp()
print('Ordenada:', sorted(dados))
    