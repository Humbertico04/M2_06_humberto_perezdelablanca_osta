def lee_numero():
    numero = int(input("Introduce un número: "))
    return numero

def mayor():
    num1=lee_numero()
    num2=lee_numero()
    num3=lee_numero()
    MAX=max(num1, num2, num3)
    print("El mayor número que introdujo fue:", MAX)
    return num1, num2, num3

mayor()
