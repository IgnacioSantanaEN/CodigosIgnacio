num1 = int(input("numero 1: "))
num2 = int(input("numero 2: "))
valor = 0
while True:
    print("""Seleccione opcion
    1. Sumar
    2. Restar
    3. Multiplicar
    3. Dividir
    """)

    valor = int(input("Ingrese una opcion"))
    if valor == 1:
        print("La suma es:", num1+num2)
        break;
    elif valor == 2:
        print("La resta es:", num1-num2)
        break;
    elif valor == 3:
        print("La muliplicación es:", num1*num2)
        break;
    elif valor == 4:
        print("La division es:", num1/num2)
        break;
    else:
        print("Opcion incorrecta")
        break;