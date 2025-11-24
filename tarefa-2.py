def saudacao(nome): #Para criar uma função = Primeiro digitamos "def",
                    # depois o nome da função, em seguida usamos () - que pode ter ou não variáveis.
                    # Outra nomenclatura para a variável aqui é chamadi de "Parâmetro".
    print(f"Eae!, {nome}!") # "print" é o comando que imprime algo no terminal.

saudacao("Lucas")


def soma(a, b): # Definição das variáveis, no caso a, b.
    resultado = a + b # Resultado da variável.
    return resultado  # A instrução return em Python é usada para sair de uma função e enviar um valor de volta para quem a chamou.

total = soma(6,7) # Total da funçao
print(total)

numero1 = int(input("Digite um número "))
numero2 = int(input("Digite um número "))
soma = numero1 + numero2
print(soma)

numero1 = int(input("Digite um número "))
numero2= int(input("Digite um número "))
subtracao = numero1 - numero2
print(subtracao)

numero1 = int(input("Digite um número "))
numero2= int(input("Digite um número "))
divisao = numero1 / numero2
print(divisao)

numero1 = int(input("Digite um número "))
numero2= int(input("Digite um número "))
media = (numero1 + numero2)/2
print(media)


