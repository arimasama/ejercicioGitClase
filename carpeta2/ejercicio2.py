def numeros_impares(limite):
    for i in range(1, limite + 1, 2):
        print(i, end=" ")

limite = int(input("Introduce un número para ver los números impares hasta ese número: "))
numeros_impares(limite)