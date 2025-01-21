# Operçãoes com strings

s = 'Camel'
x = 'Vivo'

# Concatenação
print('The ' + s + ' run away!')

# Interpolação
print('tamanho de %s => %d' % (s , len(s)))

# String tratada como sequencia
for ch in s: print(ch)

# String são objetos
if s.startswith('C'): print( s.upper())

# o que acontecerá
print(3 * s) 

#Zeros a esquerda
print("Agora são %02d:%02d." % (2, 00))

#Real (números após o ponto controla as casas decimais)
print("Percentagem: %.2f%%, Exponecial: %.2e" % (5.333, 0.00314))

# Octal e hexadecimal
print('Decimal: %d, Octal: %o, Hexadecial: %x' % (10, 10, 10))

# -#- coding: latin1
musicos = [('Page', 'guitarrista', 'Led Zeppelin'),
           ('Fripp', 'guitarrista', 'King Crimson')]

# Parametros identificados pela ordem
msg = '{0} é {1} do {2}'

for nome, funcao, banda in musicos:
    print(msg.format(nome, funcao, banda))
    
# Parametros identificados pelo nome
msg = '{saudacao}, são {hora:02d}:{minuto:02d}'

print(msg.format(saudacao="Bom dia", hora=7, minuto=30))

# Função builtin format()
print('Pi = ', format(3.14159, '.3e'))    
nome = 'Romulo'
romulo = len(nome)
print('Meu nome é,', nome, 'e tem', romulo, 'letras.')