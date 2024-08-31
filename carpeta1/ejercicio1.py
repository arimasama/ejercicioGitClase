def tabla_multiplicar(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {numero * i}")

numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
tabla_multiplicar(numero)