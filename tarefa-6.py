temperatura = int(input("Digite a temperatura do ambiente"))
if temperatura <=15:
    print("Frio")
elif temperatura <=25:
    print("Agradável")
elif temperatura >=25:
    print("Quente")
else:
    print("Digite novamente a temperatura")