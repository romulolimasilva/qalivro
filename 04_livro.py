"""
    if <condição>:
        <blocode código>
    elif <condição>:
        <blocode código>
    elif <condição>:
        <blocode código>
    else:
        <blocode código>
        
        Podemos ter mais de im elfi e somente um else no final.
    """



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
        