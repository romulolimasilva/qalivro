import string

# Cria uma string template
st = string.Template("$aviso aconteceu em $quando")

# Preenche o modelo com um diiconario
s = st.substitute({'aviso': "Falta de eletricidade", "quando": "03 de abril de 2002"})

peso = string.Template("$nome hoje é dia de $contar")

p = peso.substitute({'nome': 'Rômulo', 'contar': 'pesar a verdura em bom estado.'})

avaria = string.Template("$nome hoje é dia de $descarte")

av = avaria.substitute({'nome': 'Rômulo', 'descarte': 'contar a perda do HortiFruti'})

# Mostra:
# Falta de eletricidade aconteceu em 03 de abril de 2002
print(s)
print(p)
print(av)

