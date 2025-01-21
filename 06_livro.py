"""
Sintaxe do While:
while <conbdição>:
    <bloco de código>
    continue
    break
else: 
    <bloco de código>
    """
    
# Exemplo de uso

#Soma de 0 a 99
s = 0
x = 1

while x < 100:
    s = s + x
    x = x + 1
print('O valor de "S" é: ', s)
