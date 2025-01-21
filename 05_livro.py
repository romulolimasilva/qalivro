"""
for
Sintaxe

for <referenci> in <sequencia>:
    <blocode código>
    continue
    break
else:
    <bloco de código>
    Podemos ter mais de uma instrução no bloco de código.
    """

# Exemplo de uso
#Soma de 0 a 99
s = 0
for x in range(1, 100):
    s = s + x
print('Aquin um laço maior: ', s)
    
print('Aqui um laço menor: ',sum(range(1, 100)))

a = 1
b = sum(range(1, 100))
c = a + b
print('Aqui um inicio de uma def: ',c)
