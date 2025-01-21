# Numeros 

# -*- coding: latin1 -*-
# -*- coding: utf-8 -*-
 # Inteiro(int) i = 1
 # Real de ponto plutuante (float): f = 3.14, aqui utilizamos . (ponto), pq a liguagem é sempre americana.
 # Complexo (complex): c = 3 + 4j
 
# Exemplo:

#Convertando de real para inteiro
print('int(3.14) =', int(3.14))

#Convertendo inteiro pra real
print('float(5) =', float(5))

#Calculo entre inteiro e real resulta em real
print('5.0 / 2 + 3 = ', 5.0 / 2 + 3)

#Inteiros em outra base
print("int('20', 8) = ", int('20', 8)) # base 8
print("int('20', 16) = ", int('20', 16)) # base 16

#Operações com numeros complexos
c = 3 + 4j
print('c =', c)
print('Parte real:', c.real)
print('Parte imaginária:', c.imag)
print('Conjugado:', c.conjugate())
