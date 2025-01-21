# Laços
"""Laços (loops) são estruturas de repetição, geralmente usados para processar
coleções de dados, tais como linhas de um arquivo ou registros de um banco
de dados, que precisam ser processados por um mesmo bloco de código."""

# Soma de 0 a 99
s = 0
for x in  range(1, 100):
        s = s + x
print(s)


# Aqui um laço da o valor para cada x que vai de 1 a 99
for x in range(1, 100):
    print("X=", x)
    
    
for frutas in list(['banana', 'maca', 'laranja']):
    print('frutas: ', frutas)
    
print('-----------------')

for combustivel in list(['gasolina', 'etanol', 'diesel']):
    print('combustivel: ', combustivel)