"""<condição>: sentença que possa ser avaliada como verdadeira ou falsa.
▪ <bloco de código>: sequência de linhas de comando.
▪ As clausulas elif e else são opcionais e podem existir vários elifs para o
mesmo if, porém apenas um else ao final.
▪ Parênteses só são necessários para evitar ambiguidades"""




temp = int(input("Entre com a temperatura: "))

if temp < 0:
    print("Muito frio")
elif 0 <= temp <= 20:
    print('Frio')
elif 21 <= temp <= 25:
    print('Normal')
elif 26 <= temp <= 35:
    print('Quente')
else:
    print('Muito quente')

  

tanque_veiculo = float(input('Tanque: '))

if tanque_veiculo <= 5:
    print('#')
elif tanque_veiculo <= 10:
    print('###')
elif tanque_veiculo <= 20:
    print('####')
else:
    print('########')
    

fehadura = [4525, 3512, 7432, 0000]
senha = int(input('Senha: '))

if senha in fehadura:
    print('Acesso permitido')
else:
    print('Acesso negado')