import math

def area_circulo():
    radio = int(input("Introduce el radio de tu círculo: "))
    área = (radio^2) * math.pi
    return print(área)

area_circulo()