def imc():
    Peso = int(input("Introduce tu peso (kg): "))
    Altura = round(float(input("Introduce tu altura (m): ")), 2)
    IMC = Peso / (Altura * Altura)
    return IMC

def clasificacion_imc(IMC):
    if IMC < 18.50:
        print("Clasificación IMC: Bajo peso")
    elif 18.50 <= IMC < 25.00:
        print("Clasificación IMC: Normal")
    elif 25.00 <= IMC < 30.00:
        print("Clasificación IMC: Sobrepeso")
    else:
        print("Clasificación IMC: Obesidad")

clasificacion_imc(imc())