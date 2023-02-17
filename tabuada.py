
#Gerador de tabuada do 1 ao 10, usuário entra com o número que desejar.

numero = int(input("Digite um numero: "))
i = 1
tabuada = 0
for i in range(10):
    i += 1
    tabuada = (numero * i)
    print(f'Tabuada: {numero}x{i} -> {tabuada}')
