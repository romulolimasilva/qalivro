"""def func(paremetor1, paramentor2=padrao):
    "Doc String"

    <bloco de codigo>
    return valor"""
    
# Fatyorial implementantado de frma recusiva

def fatorial(num):
    if num <= 1:
        return 1
    else:
        return(num * fatorial(num -1))
# Testando fatorial
print(fatorial(5))


def fatorial(n):
    n = n if n > 1 else 1
    j = 1
    for i in range(1, n + 1):
        j = j * i
    return j

# Testatndo 
for i in range(1, 7):
    print(i, '->', fatorial(i))