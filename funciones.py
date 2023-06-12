import re
import json
import csv

def mostar_menu():
    print("""
    1-Cargar datos desde archivo
    2-Listar cantidad por marca
    3-Listar insumo por marca
    4-Buscar insumo por caracteristca
    5-Listar insumos ordenados
    6-Realizar compras
    7-Guardar en formato JSON
    8-Leer desde formato JSON
    9-Actualizar precios
    10-Agregar producto
    11-Salir del programa
    """)
    opcion=input(" ")
    return opcion

def cargar_datos()->list:
    """Funcion para cargar datos del archivo

    Returns:
        list: retorna una lista de diccionarios .
    """
    with open(r"insumos.csv",encoding="utf-8")as file: 
        archivo_lector=file.read()
        archivo_lector=archivo_lector.split("\n")
        
        lista_1=list()
        lista_dicc=list()

        for elemento in archivo_lector:
            archivo_lector=re.split("," , elemento.replace("$",""))#Reemplazo de "$" por " " para poder parsear el precio
            if(archivo_lector[0] != "") :
                lista_1.append(archivo_lector)#Soluciona el problema de un elemento vacio
        
        print(lista_1[0][2])

        for elemento in range(len(lista_1)):
            direccio=dict()#Creacion de diccionario iterable
            direccio["ID"]=lista_1[elemento][0]
            direccio["NOMBRE"]=lista_1[elemento][1]
            direccio["MARCA"]=lista_1[elemento][2]
            direccio["PRECIO"]=float(lista_1[elemento][3])
            direccio["CARACTERISTICAS"]=lista_1[elemento][4]
            lista_dicc.append(direccio)
        print("Datos cargados")
        return(lista_dicc) 
        
def cantidad_marca(lista:list,key_m:str,key_c:str)->None:
    agrupacion_marca=list()
    lista_insumos=list()
    valor=0
    
    for marca in lista:
        if not (esta_en_lista(agrupacion_marca,marca[key_m])):
            agrupacion_marca.append(marca[key_m])#filtrado de marca

    for marca in agrupacion_marca:
        valor=0
        for nombre_producto in lista: 
            diccionario_marcas=dict()
            if(marca == nombre_producto[key_m]):#recorrida de marca
                valor+=1
            diccionario_marcas[key_m] = marca#cantidad de producto con misma marca
            diccionario_marcas[key_c]=valor
        lista_insumos.append(diccionario_marcas)#guarda la cantidad

    print(f"MARCA                    CANTIDAD")
    print("-----------------------------------")
    for elemento in lista_insumos:
       print(f"{elemento[key_m]:24s}{elemento[key_c]:5d}")   

def esta_en_lista (lista:list , marca:str)->list:
    esta=False
    for elemento in lista:
        if(elemento == marca):
            esta=True
            break
    return esta
        
def insumos_por_marca(lista:list , key_m:str,key_n:str,key_p:str)->None:
    agrupacion_marca=list()
    lista_insumos=list()
    for marca in lista:
        if not (esta_en_lista(agrupacion_marca,marca[key_m])):#filtro marca
            agrupacion_marca.append(marca[key_m])

    for marca in agrupacion_marca:
        for nombre_insumo in lista: 
            diccionario_marcas_2=dict()#aca se pode el dic para que se vuelva a crear con cada iteracion
            if(marca == nombre_insumo[key_m]):#compara marca == marca 
                print(nombre_insumo[key_n])
                diccionario_marcas_2[key_m]=nombre_insumo[key_m]
                diccionario_marcas_2[key_n]=nombre_insumo[key_n]
                diccionario_marcas_2[key_p]=nombre_insumo[key_p]
                lista_insumos.append(diccionario_marcas_2)
    print("MARCA                        NOMBRE                       PRECIO")      
    for item in lista_insumos:
        print(f"{item[key_m]:24s}{item[key_n]:30s}{item[key_p]:9.2f}")

def busqueda_caracteristica(recorrer_caracteristica:list(),key_c:str,key_m:str)->None:
    lista=list()
    busqueda=input("Buscar caracteristica ->:").capitalize()#por que las caracteristicas empiezan con mayuscula
    for caracteristica in recorrer_caracteristica:
            diccionario=dict()
            if (busqueda in (caracteristica[key_c])) or (busqueda.lower() in (caracteristica[key_c])):#busca si coincide algun str en una caracteristica
                diccionario[key_m]=caracteristica[key_m]
                diccionario[key_c]=caracteristica[key_c]
                lista.append(diccionario)

    if len(lista) == 0:#si no encontro nada printea no existe
        print ("No existe")
    elif len(lista) > 0:# si encontro algo muestra la catacteristica
        print("MARCA     CARACTERISTICAS")
        for item in lista:
            print(f"{item[key_m]:10s}{item[key_c]:10s}")

def orden_insumos(lista:list,key_m:str,key_n:str,key_i:str,key_p:str)->None:
    print("ID    CARACTERISTICA                     PRECIO     MARCA")
    tam=len(lista)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(lista[i][key_m]>lista[j][key_m]):
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux

    for elemento in lista:
        print(f"{elemento[key_i]:2s}  {elemento[key_n]:35s}  {elemento[key_p]:4.2f}      {elemento[key_m]}")

def realizar_compras(lista:list,key_m:str,key_p:str)->list:  
    lista_marcas=list()
    lista_productos=list()
    salida= True
    precio_total=0
    sumatoria_precios=0
    ##probar aca afuera el mensaje de menu
    while True:
        busqueda=True

        primera=True
        while primera:
            marca_ingresada=input("(1) Ingresar marca : , N para terminar :").capitalize()
            if(marca_ingresada !="N"):
                for marca in lista:
                    if(marca_ingresada == marca[key_m].capitalize()):
                        lista_marcas.append(marca)
                        primera=False
            elif(marca_ingresada == "N"):
                salida= False
                break

        if(salida != True):
            break
    
        print("Lista de productos de la marca\n-----------------------")
        for elemento in lista_marcas:     
                print(f"->{elemento['NOMBRE']}")

        while busqueda:
            producto_elegido=input("(2) Elegir un producto : ").capitalize()
            for  elemento in lista_marcas:
                if(producto_elegido == elemento["NOMBRE"]):
                    while True:
                        try:
                            cantiadad =int(input("(3) Cantidad deseada :")) 
                            if(cantiadad>0):
                                diccionario=dict() 
                                cantidad_compra=cantiadad*elemento[key_p]
                                cantidad_compra=round(cantidad_compra , 2)
                                subtotal=cantidad_compra*0.084
                                subtotal=round(subtotal , 2)
                                precio_total+=cantidad_compra
                                sumatoria_precios+=cantidad_compra
                                busqueda =  False
                                diccionario["PRODUCTO"]=producto_elegido
                                diccionario["CANTIDAD"]=cantiadad
                                diccionario[key_p]=elemento[key_p]
                                diccionario["SUBTOTAL"]=subtotal
                                diccionario["PRECIO FINAL"]=precio_total
                                lista_productos.append(diccionario)
                                cantidad_compra=0
                                subtotal=0
                                precio_total=0
                                break
                        except ValueError:
                            print("No ingresaste un numero")         
        lista_marcas.clear()

        with open("recibo.txt","a")as archivo:
            for item in lista_productos:
                datos=(f"\nPRODUCTO :{item['PRODUCTO']} | CANTIDAD :{item['CANTIDAD']} | PRECIO :${item[key_p]} | SUBTOTAL :${item['SUBTOTAL']} | PRECIO FINAL :${item['PRECIO FINAL']}")
            archivo.write(datos)
            archivo.close()

    print("Fin de ingreso de datos")   
    with open("recibo.txt","a")as archivo:   
        mensaje=(f"\n-------------------------------------------------------------------------\nTOTAL {sumatoria_precios}")   
        archivo.write(mensaje)
        archivo.close()
    return lista_productos


def guardado_json(lista:list)->None:
    lista_productos=list()
    for item in lista:
        if "Alimento" in item["PRODUCTO"]:
            lista_productos.append(item)

    if(len(lista_productos)>0):
        print("Datos cargados")
        with open("Archivo.json","w")as data:
            json.dump(lista_productos ,data,indent=4) 
    else:
        print("Lista vacia")

    

def mostrar_json()->None:
    with open("Archivo.json","r")as data: 
        datos=json.load(data)#devuelve la lista de diccionarios
        #print(datos) verificar que este ok
        print("Listado de insumos\nPRODUCTO              CANTIDAD    PRECIO   SUBTOTAL   PRECIO FINAL")
        for item in datos:
            print(f"{item['PRODUCTO']} {item['CANTIDAD']:9.2f} {item['PRECIO']:9.2f} {item['SUBTOTAL']:9.2f} {item['PRECIO FINAL']:9.2f}")

def actualizacion_precios(lista:list)->None:
    lista_copiada=list()
    lista_copiada=lista.copy()
    i=0
    actualizacion=list(map(lambda item: round(item["PRECIO"] + item["PRECIO"] *0.084,2), lista_copiada))
    for item in lista_copiada:
        item["PRECIO"]=float(actualizacion[i])
        i+=1
    #with open("insumos copy.csv","w")as file:  creador
    with open("insumos.csv","w",encoding="utf-8")as file: 
        for item in lista_copiada:
            dato=(f"{item['ID']},{item['NOMBRE']},{item['MARCA']},${item['PRECIO']},{item['CARACTERISTICAS']}\n")
            file.write(dato)

    print("Datos actualizados")

def agregar_productos():
    with open("marcas.txt")as archivo:
        lista_marcas=list()
        lista_agregados=list()
        validador=True
        leer=archivo.read()
        separador=leer.split("\n")

        print("LISTADO DE MARCAS\n--------------------")
        for marca in separador:
            if (marca != ""):#no agrega el elemento vacio
                lista_marcas.append(marca)
                print(f"{marca}")
        
        while validador:
            marca_elegida=input("Elegir marca >:  , N para terminar ").capitalize()#como poner mensaje de error?
            if(marca_elegida == "N"):
                validador=False            
            for marca in lista_marcas:
                if marca_elegida == marca.capitalize(): 
                    diccionario_agregados=dict()
                    diccionario_agregados["MARCA"]=marca_elegida
                    diccionario_agregados["NOMBRE"]=input("Ingresar nombre del producto >: ")
                    
                    while True:
                        try:
                            precio=float(input("Ingresar precio >: "))
                            if(precio>0):
                                diccionario_agregados["PRECIO"]=precio
                                break
                            else:
                                print("Precio no valido")
                        except ValueError:
                            print("Pusiste una letra")

                    diccionario_agregados["CARACTERISTICAS"]=input("Ingresar caracteristicas (maximo 3)>: ")
                    lista_agregados.append(diccionario_agregados)

        formato=input("Guardar los datos en formato CSV o JSON ?").upper()
        while (formato!="CSV" and formato !="JSON"):
            formato=input("ERROR ,elegir CSV o JSON :>").upper()

        if(formato=="CSV"):
            with open("agregado.csv","w")as file: #supoiendo que no lo tenga que agregar en insumos
                file.write("Datos Agregados\n")
                for item in lista_agregados:
                    datos=(f"Datos Agregados\n{item['MARCA']},{item['NOMBRE']},${item['PRECIO']},{item['CARACTERISTICAS']}\n")
                    file.write(datos)

        if(formato=="JSON"):
            with open("agregado.json","w")as file: #supoiendo que no lo tenga que agregar en insumos
                json.dump(lista_agregados,file,indent=4)

                        
def salir_funcion()->bool:
    opcion=input("desea salir del programa ? s/n ")
    while(opcion!="s" and opcion!="n"):
        opcion=input("error , s/n")
    if(opcion =="s"):
        print("Chao ♪♪♪ ")
        return False
    else :
        return True
    