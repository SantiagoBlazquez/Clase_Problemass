def factorial(num):
    """
    Calcula el factorial de forma recursiva
    """

    if num == 0:
        return 1
    else:
        return num * factorial(num)
    
numero = int(input("Ingrese un numero: "))
print(f"El factorial de {numero} es: factorial(numero)")
    