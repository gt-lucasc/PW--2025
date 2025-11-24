#Criar uma função para calcular a área de um circulo
'''
def circulo(raio):
    pi = 3.1415926
    area = pi * (raio**2)
    return area

x = int(input())
print("Digite um número" + circulo(x))
'''
'''
def aplicar_desconto(preco, percentual):
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    return preco_final

print(aplicar_desconto(80,10))
'''




'''temperatura = int(input("Digite um número"))
resultado = (temperatura) * 1.8 + 32
print(resultado)
'''

def converter(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

x = int(input())
print(converter(x))


