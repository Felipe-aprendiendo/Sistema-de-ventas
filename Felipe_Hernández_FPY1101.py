import json
from datetime import datetime
import os

ventas = []

def menu():
    opcion = 0
    try:
        opcion = int(input('''\n******** Sistema de gestión de ventas ********     
        1. Registrar una venta
        2. Mostrar todas las ventas
        3. Buscar venta por cliente
        4. Guardar las ventas en un archivo
        5. Cargar ventas desde un archivo
        6. Generar boleta
        7. salir del programa
        Ingrese una opción: '''))
    except ValueError:
        print("Por favor ingrese una opción válida, entre 1 y 7")
        opcion = 0
    return opcion

def registrar():
    while True:
        cliente = input("\nIndique el nombre del cliente para comenzar con el registro de la venta: ").lower()
        cliente_registrado = False

        for cliente_buscar in ventas:
            if cliente_buscar['cliente'] == cliente:
                print(f"El cliente '{cliente}' ya se encuentra registrado")
                cliente_registrado = True
                break
        
        if cliente_registrado:
            continue
        else:
            print(f"Nuevo cliente '{cliente}', ingresar datos de venta:")
            pep_p = int(input("Indique la cantidad deseada de Peperoni pequeña ($5.000): "))
            pep_m = int(input("Indique la cantidad deseada Peperoni mediana ($8.000): "))
            pep_f = int(input("Indique la cantidad deseada Peperoni familiar ($10.000): "))
            medit_p = int(input("Indique la cantidad deseada de Mediterránea pequeña ($6.000): "))
            medit_m = int(input("Indique la cantidad deseada de Mediterránea mediana ($9.000): "))
            medit_f = int(input("Indique la cantidad deseada de Mediterránea familiar ($12.000): "))
            veg_p = int(input("Indique la cantidad deseada de Vegetariana pequeña ($5.500): "))
            veg_m = int(input("Indique la cantidad deseada de Vegetariana mediana ($8.500): "))
            veg_f = int(input("Indique la cantidad deseada de Vegetariana familiar ($11.000): "))
            subtotal = (pep_p * 5000) + (pep_m * 8000) + (pep_f * 10000) + (medit_p * 6000) + (medit_m * 9000) + (medit_f * 12000) + (veg_p * 5500) + (veg_m * 8500) + (veg_f * 11000)
            while True:
                try:
                    cat_descuento = int(input('''\nSeleccione una categoría de descuento
                    1. Estudiante diurno: descuento de 15%
                    2. Estudiante vespertino: descuento de 20%
                    3. Administrativo: 10%
                    Seleccione una opción: '''))
                    if cat_descuento not in [1, 2, 3]:
                        raise ValueError("Por favor ingrese una opción válida (1, 2 o 3)")
                    break
                except ValueError as e:
                    print(e)
            if cat_descuento == 1:
                descuento = subtotal * 0.15
            elif cat_descuento == 2:
                descuento = subtotal * 0.2
            elif cat_descuento == 3:
                descuento = subtotal * 0.1
            total = subtotal - descuento
            nueva_venta = {
                'cliente': cliente,
                'peperoni pequeña': pep_p,
                'peperoni mediana': pep_m,
                'peperoni familiar': pep_f,
                'mediterránea pequeña': medit_p,
                'mediterránea mediana': medit_m,
                'mediterránea familiar': medit_f,
                'vegetariana pequeña': veg_p,
                'vegetariana mediana': veg_m,
                'vegetariana familiar': veg_f,
                'subtotal': subtotal,
                'descuento': descuento,
                'total': total
            }
            ventas.append(nueva_venta)
            print("\nVenta registrada con éxito!")
            break
    return nueva_venta

def mostrar_ventas():
    print("\n***** Resumen de ventas registradas en el sistema ****")
    for venta in ventas:
        print("\nDatos de venta:")
        for clave, valor in venta.items():
            print(f"- {clave}: {valor}")

def buscar_venta():
    cliente_buscar = input("\nIngrese el nombre del cliente que desea buscar: ").lower()
    cliente_encontrado = False
    for venta in ventas:
        if venta['cliente'] == cliente_buscar:
            cliente_encontrado = True
            print("El cliente se encuentra registrado en el sistema")
            print(f"\nDatos de la venta asociados al cliente '{cliente_buscar}':")
            for clave, valor in venta.items():
                print(f"- {clave}: {valor}")
            break
    if not cliente_encontrado:
        print(f"El cliente {cliente_buscar} no se encuentra registrado en el sistema. registre la venta primero, vaya a opción 1 del menú")

def guardar_ventas():
    with open('ventas.json', 'w', encoding='utf-8') as archivo:
        json.dump(ventas, archivo, ensure_ascii=False)
        print("\ndatos guardados con éxito")
        print(f"Sus datos se han guardado en {os.getcwd()}")

def cargar_ventas():
    global ventas
    try:
        with open('ventas.json', 'r', encoding='utf-8') as archivo:
            ventas = json.load(archivo)
            print("\ndatos cargados exitosamente")
    except FileNotFoundError:
        print("\nEl archivo 'ventas.json' no ha sido creado aun. No hay datos para cargar")

def generar_boleta():
    boleta_cliente = input("\nIngrese el nombre del cliente para generar boleta: ").lower()
    boleta_encontrado = False
    fecha_hora_actual = datetime.now()
    fecha_formato = fecha_hora_actual.strftime("%d-%m")
    hora_formato = fecha_hora_actual.strftime("%H:%M:%S")
    for venta in ventas:
        if venta['cliente'] == boleta_cliente:
            boleta_encontrado = True
            print(f'''\n
        ****** Boleta electrónica ******

{fecha_formato}
{hora_formato}

----------------------------------------------------
Detalle

{venta['peperoni pequeña']} pizza peperoni pequeña                     ${venta['peperoni pequeña']*5000}
{venta['peperoni mediana']} pizza peperoni mediana                      ${venta['peperoni mediana']*8000}
{venta['peperoni familiar']} pizza peperoni familiar                     ${venta['peperoni familiar']*10000}
{venta['mediterránea pequeña']} pizza mediterránea pequeña                  ${venta['mediterránea pequeña']*6000}
{venta['mediterránea mediana']} pizza mediterránea mediana                  ${venta['mediterránea mediana']*9000}
{venta['mediterránea familiar']} pizza mediterránea familiar                 ${venta['mediterránea familiar']*12000}
{venta['vegetariana pequeña']} pizza vegetariana pequeña                   ${venta['vegetariana pequeña']*5500}
{venta['vegetariana mediana']} pizza vegetariana mediana                   ${venta['vegetariana mediana']*8500}
{venta['vegetariana familiar']} pizza vegetariana familiar                  ${venta['vegetariana familiar']*11000}
----------------------------------------------------
Subtotal                                      ${round(venta['subtotal'])}
Descuento                                     ${round(venta['descuento'])}

                
Total                                         ${round(venta['total'])}
----------------------------------------------------
            !Gracias por su preferencia!
                ''') 
            break
    if not boleta_encontrado:
        print(f"No hay datos de venta asociados al cliente'{boleta_cliente}', por lo que no es posible generar la boleta")


while True:
    opcion = menu()

    if opcion == 1:
        registrar()
    elif opcion == 2:
        mostrar_ventas()
    elif opcion == 3:
        buscar_venta()
    elif opcion == 4:
        guardar_ventas()
    elif opcion == 5:
        cargar_ventas()
    elif opcion == 6:
        generar_boleta()
    elif opcion == 7:
        try:
            salir = int(input("\n¿Está seguro de que desea salir? (1:si - 2:no)"))
            if salir == 1:
                print("Gracias por su preferencia")
                break
            else:
                print("Puede continuar operando")
        
            if salir not in [1, 2]:
                raise ValueError("Por favor ingrese una opción válida (1:si - 2:no)")
            break
        except ValueError as e:
            print(e)