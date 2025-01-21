# Função format()


p = 'PYTHON'
print('{}'.format(p[0]),'{}'.format(p[:2]), '{}'.format(p[2:]), '{}'.format(p[-1]) )

# Imprimi invertido
print(p[::-1])

import string

# O alfabeto
a = string.ascii_letters

# Rodando o alfabeto um caractere para a esquerda
b = a[1:] + a[0]

# A função maketrans() cria uma tabela de tradução
# entre os caractres da duas strings que ela
#recebeu como parâmetro.
#Os caractres ausentes nas tabrelas serão
#copiadaso para a sáida.
tab = str.maketrans(a, b)

# A mensagem ..
msg = """Esse texto será traduzido.. Vai ficar bem estranho."""

# A função translate() usa a tabela de tradução
# criada pela maketrans() para traduzir uma string
print(msg.translate(tab))

# Importando o módulo string
import string

# Cria uma string template
st = string.Template('$aviso aconteceu em $quando')

# Preenche o modelo com um diciónario
s = st.substitute({'aviso': 'Falta de eletricidade', 'quando': '03 de abril de 2002'})
print(s)