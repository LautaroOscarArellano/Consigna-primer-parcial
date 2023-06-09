import re
import json
import csv
import random

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
    11-Stock por marca
    12-Imprimir bajo stock
    13-Salir del programa
    """)
    opcion=input(" ")
    return opcion
#1
def cargar_datos()->list:
    """Funcion que permite cargar un archivo csv a python para su uso
    retorna una lista.

    Returns:
        list: archivo csv pasado a lista de python.
    """
    with open("insumos.csv",encoding="utf-8")as file: 
        archivo_lector=file.read()
        archivo_lector=archivo_lector.split("\n")
        
        lista_1=list()
        lista_dicc=list()


        for elemento in archivo_lector:
            archivo_lector=re.split("," , elemento.replace("$",""))#Reemplazo de "$" por " " para poder parsear el precio
            if(archivo_lector[0] != "") :
                lista_1.append(archivo_lector)#Soluciona el problema de un elemento vacio
        numero=[1]#creacion de lista
        for elemento in range(len(lista_1)):
            direccio=dict()#Creacion de diccionario iterable
            direccio["ID"]=lista_1[elemento][0]
            direccio["NOMBRE"]=lista_1[elemento][1]
            direccio["MARCA"]=lista_1[elemento][2]
            direccio["PRECIO"]=float(lista_1[elemento][3])  
            direccio["CARACTERISTICAS"]=lista_1[elemento][4]
            numero_random=list(map(lambda  numero: random.randint(0, 10) , numero)) # [1] parcial 21/6/2023
            direccio["STOCK"]=numero_random[0]
            lista_dicc.append(direccio)
        return(lista_dicc) 
    

#2       
def cantidad_marca(lista:list,key_m:str,key_c:str)->None:
    """Funcion que recibe por parametro la lista copiada de la anterior funcion
    y 2 llaves por parametro , muestra todas las marcas y la cantidad de
    insumos.

    Args:
        lista (list): lista anterior funcion
        key_m (marca): marca
        key_c (cantidad): su cantidad
    """
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
    """Funcion filtradora , filtra para que no se repitan marcas.

    Args:
        lista (list): lista
        marca (str): marca

    Returns:
        list: lista filtrada
    """
    esta=False
    for elemento in lista:
        if(elemento == marca):
            esta=True
            break
    return esta
#3        
def insumos_por_marca(lista:list , key_m:str,key_n:str,key_p:str)->None:
    """Funcion que muestra cada marca , nombre y precio de los insumos.

    Args:
        lista (list): lista
        key_m (str): marca
        key_n (str): nombre
        key_p (str): precio
    """
    agrupacion_marca=list()
    lista_insumos=list()
    for marca in lista:
        if not (esta_en_lista(agrupacion_marca,marca[key_m])):#filtro marca
            agrupacion_marca.append(marca[key_m])

    for marca in agrupacion_marca:
        for nombre_insumo in lista: 
            diccionario_marcas_2=dict()#aca se pode el dic para que se vuelva a crear con cada iteracion
            if(marca == nombre_insumo[key_m]):#compara marca == marca 
                #print(nombre_insumo[key_n])
                diccionario_marcas_2[key_m]=nombre_insumo[key_m]
                diccionario_marcas_2[key_n]=nombre_insumo[key_n]
                diccionario_marcas_2[key_p]=nombre_insumo[key_p]
                lista_insumos.append(diccionario_marcas_2)
    print("MARCA                        NOMBRE                       PRECIO")      
    for item in lista_insumos:
        print(f"{item[key_m]:24s}{item[key_n]:30s}{item[key_p]:9.2f}")
#4
def busqueda_caracteristica(recorrer_caracteristica:list(),key_c:str,key_m:str,key_s:str)->None:
    """Funcion que busca por caracteristica  y lista todos los que tengan
    algo que ver.

    Args:
        recorrer_caracteristica (list): lista
        key_c (str): caracteristica
        key_m (str): marca
    """
    lista=list()
    busqueda=input("Buscar caracteristica ->:").capitalize()#por que las caracteristicas empiezan con mayuscula
    for caracteristica in recorrer_caracteristica:
            diccionario=dict()
            if (busqueda in (caracteristica[key_c])) or (busqueda.lower() in (caracteristica[key_c])):#busca si coincide algun str en una caracteristica
                diccionario[key_m]=caracteristica[key_m]
                diccionario[key_c]=caracteristica[key_c]
                diccionario[key_s]=caracteristica[key_s]
                lista.append(diccionario)

    if len(lista) == 0:#si no encontro nada printea no existe
        print ("No existe")
    elif len(lista) > 0:# si encontro algo muestra la catacteristica
        print("STOCK   MARCA     CARACTERISTICAS ")
        for item in lista:
            print(f"{item[key_s]:1d}       {item[key_m]:10s}{item[key_c]:10s}")
#5
def orden_insumos(lista:list,key_m:str,key_n:str,key_i:str,key_p:str,key_s:str)->None:
    """Funcion que muestra los insumos ordenados.

    Args:
        lista (list): lista
        key_m (str): marca
        key_n (str): nombre
        key_i (str): id
        key_p (str): precio
    """
    print("ID    CARACTERISTICA                     PRECIO     MARCA                               STOCK")
    tam=len(lista)
    for i in range(tam-1):
        for j in range(i+1,tam):
            if(lista[i][key_m]>lista[j][key_m]):
                aux=lista[i]
                lista[i]=lista[j]
                lista[j]=aux
    for elemento in lista:
        print(f"{elemento[key_i]:2s}  {elemento[key_n]:35s}  {elemento[key_p]:4.2f}      {elemento[key_m]:35s}{elemento[key_s]:4d}")
#6
def realizar_compras(lista:list,key_m:str,key_p:str)->list:  
    """Funcion que permite al usuario realizar compras.El isuario ingresa
    marca , producto y cantidad , esto se finaliza hasta que el usuario deje
    de ingresar datos.

    Args:
        lista (list): lista
        key_m (str): marca
        key_p (str): _description_

    Returns:
        list: precio
    """
    lista_marcas=list()
    lista_productos=list()
    salida= True
    precio_total=0
    sumatoria_precios=0
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
                #print(f"->{elemento['NOMBRE']} STOCK : {elemento['STOCK']}")
                print(f"->{elemento['NOMBRE']} STOCK : {elemento['STOCK']}")

        while busqueda:
            producto_elegido=input("(2) Elegir un producto : ").capitalize()
            for  elemento in lista_marcas:
                if(producto_elegido == elemento["NOMBRE"]):
                    while True:
                        try:
                            cantiadad =int(input("(3) Cantidad deseada :"))
                            if elemento["STOCK"] <= cantiadad:
                                print("Compra menos cantidad")
                            else:
                                elemento["STOCK"]=elemento["STOCK"]-cantiadad
                                if(elemento["STOCK"]>0):
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
                                    diccionario["STOCK"]=elemento["STOCK"] # guarda el stock
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
                datos=(f"\nSTOCK :{item['STOCK']}| PRODUCTO :{item['PRODUCTO']} | CANTIDAD :{item['CANTIDAD']} | PRECIO :${item[key_p]} | SUBTOTAL :${item['SUBTOTAL']} | PRECIO FINAL :${item['PRECIO FINAL']}")
            archivo.write(datos)
            archivo.close()

    print("Fin de ingreso de datos")   
    with open("recibo.txt","a")as archivo:   
        mensaje=(f"\n-------------------------------------------------------------------------\nTOTAL {sumatoria_precios}")   
        archivo.write(mensaje)
        archivo.close()
    return lista_productos

#7
def guardado_json(lista:list)->None:
    """Genera un archivo json con todos los productos cuyo nombre contiene
    la palabra alimento.

    Args:
        lista (list): lista
    """
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
    
#8
def mostrar_json()->None:
    """Funcion que permite mostrar un listado de los insumos guardados en
    el archivo json.
    """
    with open("Archivo.json","r")as data: 
        datos=json.load(data)#devuelve la lista de diccionarios
        #print(datos) verificar que este ok
        print("Listado de insumos\nPRODUCTO              CANTIDAD    PRECIO   SUBTOTAL STOCK  PRECIO FINAL")
        for item in datos:
            print(f"{item['PRODUCTO']} {item['CANTIDAD']:9.2f} {item['PRECIO']:9.2f} {item['SUBTOTAL']:9.2f}  {item['STOCK']:4d}{item['PRECIO FINAL']:11.2f}")
#9
def actualizacion_precios(lista:list)->None:
    """Funcion que aplica un aumento del 8,4% a todos los productos del archivo
    json csv.

    Args:
        lista (list): lista
    """
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
            dato=(f"{item['ID']},{item['NOMBRE']},{item['MARCA']},${item['PRECIO']},{item['CARACTERISTICAS']},{item['STOCK']}\n")
            file.write(dato)

    print("Datos actualizados")
#10
def agregar_productos():
    """Funcion que agrega productos a un archivo nuevo
    """
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

                    while True:
                        try:
                            stock=int(input("Ingresar stock >: "))
                            if(stock>0):
                                diccionario_agregados["STOCK"]=stock
                                break
                            else:
                                print("stock no valido")
                        except ValueError:
                            print("Pusiste una letra")
                    lista_agregados.append(diccionario_agregados)
    #En esta parte agrega la opcion de guardar en json a csv                
        formato=input("Guardar los datos en formato CSV o JSON ?").upper()
        while (formato!="CSV" and formato !="JSON"):
            formato=input("ERROR ,elegir CSV o JSON :>").upper()
        if(formato=="CSV"):
            with open("agregado.csv","w")as file: #sup que no lo tenga que agregar en insumos
                file.write("Datos Agregados\n")
                for item in lista_agregados:
                    datos=(f"Marca : {item['MARCA']},Nombre producto :{item['NOMBRE']},Precio : ${item['PRECIO']},Caracteristica : {item['CARACTERISTICAS']} , Stock :{item['STOCK']} \n")
                    file.write(datos)

        if(formato=="JSON"):
            with open("agregado.json","w")as file: #supoiendo que no lo tenga que agregar en insumos
                json.dump(lista_agregados,file,indent=4)

#11
def stock_por_marca(lista:list,key_m:str)->None:
    """Funcion que le pide al usuario la marca para mostrar su stock

    Args:
        lista (list): lista
        key_m (str): marca
    """
    lista_marcas=list()
    salida= True
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
    
        print("Lista de stocks \n-----------------------")
        for elemento in lista_marcas:     
                print(f"->{elemento['NOMBRE']} STOCK : {elemento['STOCK']}")

  
#12
def imprimir_bajo_stock(lista:list)->None:
    """Funcion que agarra los elementos de la lista que tengan bajo stock y lo
    guarda a un achivo csv.

    Args:
        lista (list): lista
    """
    lista_nueva=list()
    for elemento in lista:
        if(elemento["STOCK"]<2):
            lista_nueva.append(elemento)

    with open("bajo_stock.csv","w")as file: 
            for elemento in lista_nueva:
                datos=(f"Marca : {elemento['MARCA']},Nombre producto :{elemento['NOMBRE']},Precio : ${elemento['PRECIO']},Caracteristica : {elemento['CARACTERISTICAS']} , Stock :{elemento['STOCK']} \n")
                file.write(datos)

    
#13                
def salir_funcion()->bool:
    opcion=input("desea salir del programa ? s/n ").lower()
    while(opcion!="s" and opcion!="n"):
        opcion=input("error , s/n").lower()
    if(opcion =="s"):
        print("Chao ♪♪♪ ")
        return False
    else :
        return True




#Aclaraciones : no se por que el docstring me aparece en verde.