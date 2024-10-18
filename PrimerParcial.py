'''
La oficina de distribución recibe un informe sobre el detalle de los paquetes que enviará cada
uno de los 15 clientes.
Necesitamos un programa que permita realizar la carga de los paquetes (entre 0 y 5 por cada
cliente, por cada tamaño como máximo). Luego realizar un menú que en cada opción resuelva
los siguientes requerimientos:


1. Cantidad de paquetes que envía cada cliente.

3. Generar un informe de clientes ordenados por el total a pagar de sus envíos de forma
descendente.
 

'''




cantidad_mediano = 0
cliente_mas_mediano = 0





cantidad_clientes_ni_grandes_ni_pequeños = 0
cliente = 0

cantidad_de_pequeño = 0
cantidad_de_mediano = 0
cantidad_de_grande = 0
dinero_total_recaudado = 0
while cliente < 15:
    tipo = input("ingrese el tamaño del paquetes que desea (pequeño, mediano, grande): ")
    if tipo != "pequeño" and tipo != "mediano" and tipo != "grande":
        print("error")
        tipo = input("ingrese el tamaño del paquetes que desea (pequeño, mediano, grande): ")
        
    paquete = int(input("ingrese la cantidad de paquetes que desea (entre 0 y 5): "))
    if  paquete > 0 and paquete < 5:
        print("error")
        paquete = int(input("ingrese la cantidad de paquetes que desea (entre 0 y 5): "))

    desicion = input("desea volver a registrar: (si/no)")
    if desicion != "si" and desicion != "no":
        print("error")
        desicion = input("desea volver a registrar: (si/no)")
    if desicion == 'si':
        cliente += 1
    else: 
        ("FIN")
        cliente += 15

if tipo == "mediano":
    cantidad_clientes_ni_grandes_ni_pequeños += 1
    cantidad_mediano += paquete
    cliente_mas_mediano += cliente
if cantidad_mediano < paquete:
    cantidad_mediano = paquete
    cliente_mas_mediano = cliente
    
    
if tipo == "pequeño":
    cantidad_de_pequeño += 1000 * paquete
if tipo == "mediano":
    cantidad_de_mediano += 1500 * paquete
if tipo == "grande":
    cantidad_de_grande += 2000 * paquete
dinero_total_recaudado += cantidad_de_grande+cantidad_de_mediano+cantidad_de_pequeño

if cantidad_de_mediano >  cantidad_de_grande and cantidad_de_mediano > cantidad_de_pequeño:
    cantidad_que_mas_recauda = "mediano"
if cantidad_de_grande > cantidad_de_mediano and cantidad_de_grande > cantidad_de_pequeño:
    cantidad_que_mas_recauda = "grande"
if cantidad_de_pequeño > cantidad_de_mediano and cantidad_de_pequeño > cantidad_de_grande:
    cantidad_que_mas_recauda = "pequeño"
if cantidad_de_mediano == cantidad_de_pequeño and cantidad_de_mediano == cantidad_de_grande:
    cantidad_que_mas_recauda = "recaudaron la misma cantidad"
    

   
        



mj = (f'''
    2. La cantidad de clientes que no enviaron ni paquetes pequeños ni grandes fue de {cantidad_clientes_ni_grandes_ni_pequeños}.
    4. El Total de la recaudación en pesos por cada tipo de paquete es {dinero_total_recaudado}. y el tamaño que más recaudó fue {cantidad_que_mas_recauda}.
    5. el/los clientes que enviaron más cantidad de paquetes medianos es el cliente nº{cliente_mas_mediano}.
    ''')

print(mj)