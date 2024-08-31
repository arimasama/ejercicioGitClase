def numeros_pares(limite):
    for i in range(2, limite + 1, 2):
        print(i, end=" ")

limite = int(input("Introduce un número para ver los números pares hasta ese número: "))
numeros_pares(limite)