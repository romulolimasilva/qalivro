# Listas

lista = ['a', 'b', 'c', 'd']

# Uma nova lista: Brit Progs dos anos 70
progs = ['Yes', 'Genesis', 'Pink Floyd', 'ELP']

# Varrendo a lista inteira
for prog in progs:
    print(prog)

# TRocando o ultimo elemento
progs[-1] = 'Romulo'
print(progs)

# Incluindo 
progs.append('Lima')
print(progs)

# Removendo
progs.remove("Yes")
print(progs)

# Ordena a Lista
progs.sort()
print(progs)

num = [5, 3, 1, 2, 4]
num.sort()
print(num)

# Inverte a lista
progs.reverse()
print(progs)

num.reverse()
print(num)

# IMprime numerado
for i, prog in enumerate(progs):
    print(i + 1, "=>", prog)

# Listar HortFruti

itenshorfurti = ['Abacate', 'Abacaxi', 'Abobra de Leite', 'Abobrinha', 'Ameixa', 'Banana', 'Batata Doce', 'Batata Inglesa', 'Beterraba', 'Caqui', 'Cebola Branca', 'Cebola Roxa', 'Cenoura', 'Chuchu', 'Coco Verde', 'Coco Seco', 'Goiaba', 'Laranja', 'Longoma', 'Maçã Nacional', 'Maçã Import.', 'Mamão', 'Manga Tomi', 'Maracujá', 'Melancia', 'Melancia Baby', 'Melão', 'Milho Verde', 'Morango', 'Pepino', 'Pimenta de Cheiro', 'Pimentão', 'Pitaia', 'Tomate', 'Uva Passa', 'Uva Vitória S/ Semente', 'Uva Vitória C/ Semente']

for item in itenshorfurti:
    print(item)

for cesta, item in enumerate(itenshorfurti):
    print(cesta + 1, "=>", item)


#-#- conding: latin1 -*-

# Conjuntos de dados
s1 = set(range(4))
s2 = set(range(10, 7 , -1))
s3 = set(range(2, 10, 2))

# Exibe os dados    
print('s1:', s1, '\ns2:', s2, '\ns3:', s3)

# Uniao
s1s2 = s1.union(s2)
print('União de s1 e s2:', s1s2)

# Diferença
print('Diferença com s3:', s1s2.difference(s3))

# Interseção
print('Interseção de s1 e s2:', s1s2.intersection(s3))

# Testa se um set inclui outro
if s1.issuperset([1, 2]):
    print('s1 contém 1 e 2')

# Testa se não existe elementos em comum
if s1.isdisjoint(s2):
    print('s1 e s2 não têm elementos em comum')