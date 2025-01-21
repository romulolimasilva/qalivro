# Listas
# Sintaxe: x = ['', '', '',]

# Uma nova lista: Brit Progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']
print('-'*50)

# Varrendo a lista inteira
for prog in progs:
    print(prog)
print('-'*50)
  
# Trocando o ultimo elemento
progs[-1] = 'Romulo'
print(progs)
print('-'*50)

# Imcluindo 
progs.append("Lima")
print(progs)
print('-'*50)

# Removendo
progs.remove("Lima")
print(progs)
print('-'*50)

# Ordena a lista
progs.sort()
print(progs)
print('-'*50)

# Inverte a lista
progs.reverse()
print(progs)
print('-'*50)

# Imprime numerado
for i, prog in enumerate(progs):
    print(i + 1, '=>', prog)
print('-'*50)

# IMprime do segundo item em diante
print(progs[1:])
print('-'*50)

# pop filas e pilhas

lista = ['A', 'B', 'C']
print(lista)
print('-'*50)

# A lista vazia é avaliada como falsa:
while lista:
    
    # em filas, o primeiro item é o primeiro a sair
    # pop(0) remove e rtorna o primeiro item
    print('Saiu', lista.pop(0),', faltam', len(lista))
    
# Mais itens na lista
lista += ['D', 'E', 'F']
print('Lista:', lista)

while lista:
    
    # Em pilhas, o primeiro item é o último a sair
    # pop() remove e retorna o último item
    print('Saiu', lista.pop(),', faltam', len(lista))