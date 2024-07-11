import os
os.system("cls")
cilindro_5kg = 0
cilindro_15kg = 0
cilindro_45kg = 0

el_pedido = []
pedido = {}

def imprimir_ruta():
    with open('hoja_de_ruta.txt', 'w') as file:
        for pedido in el_pedido:
            file.write(f'cliente: {pedido["cliente"]}, direccion: {pedido["direccion"]}, comuna: {pedido["comuna"]}, cilindros de gas de 5kg: {pedido["cilindrosDe5"]}, cilindros de gas de 15kg: {pedido["cilindrosDe15"]}, cilindros de gas de 45kg: {pedido["cilindrosDe45"]}\n')

def listar_pedidos():
    for pedido in el_pedido:
        print(f'cliente: {pedido["cliente"]}, direccion: {pedido["direccion"]}, comuna: {pedido["comuna"]}, cilindros de gas de 5kg: {pedido["cilindrosDe5"]}, cilindros de gas de 15kg: {pedido["cilindrosDe15"]}, cilindros de gas de 45kg: {pedido["cilindrosDe45"]}')

def registro_del_pedido():
    global cilindro_5kg, cilindro_15kg, cilindro_45kg
    nombre = input("Ingrese el nombre del cliente: ")
    apellido = input("Ingrese el apellido del cliente: ")
    direccion = input("Ingrese la dirección del cliente: ")
    comuna = input("Ingrese la comuna del cliente: ")

    while True:
        cilindros = int(input("Seleccione el tipo de cilindro: 1. 5kg, 2. 15kg, 3. 45kg\n"))
        if cilindros == 1:
            cilindro_5kg += 1
        elif cilindros == 2:
            cilindro_15kg += 1
        elif cilindros == 3:
            cilindro_45kg += 1
        else:
            print("Vuelva a intentar con una opción correcta, por favor.")
            continue

        agregar_mas = input("¿Desea agregar otro tipo de gas? (si/no): ").lower()
        if agregar_mas == "si":
            continue
        else:
            break

    pedido = {
        "cliente": f"{nombre} {apellido}",
        "direccion": direccion,
        "comuna": comuna,
        "cilindrosDe5": cilindro_5kg,
        "cilindrosDe15": cilindro_15kg,
        "cilindrosDe45": cilindro_45kg
    }

    el_pedido.append(pedido)
    print("Pedido registrado exitosamente.")

def main():
    while True:
        print("Opción 1: REGISTRAR PEDIDO")
        print("Opción 2: LISTAR TODOS LOS PEDIDOS")
        print("Opción 3: IMPRIMIR HOJA DE RUTA")
        print("Opción 4: SALIR DEL PROGRAMA")

        opcion_menu = input("Ingrese su opción\n")

        if opcion_menu == "1":
            registro_del_pedido()
        elif opcion_menu == "2":
            listar_pedidos()
        elif opcion_menu == "3":
            imprimir_ruta()
        elif opcion_menu == "4":
            print("Adiós, vuelva pronto.")
            break
        else:
            print("Intenta ingresando uno de los valores a continuación: 1, 2, 3 o 4.")

main()


      



   