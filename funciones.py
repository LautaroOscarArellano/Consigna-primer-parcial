import re

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
    10-Salir del  programa
    """)
    opcion=input(" ")
    return opcion
#ID,NOMBRE,MARCA,MARCA,CARACTERISTICAS

     

def cargar_datos():
    with open(r"insumos.csv",encoding="utf-8")as file: 
        archivo_lector=file.read()
        archivo_lector=archivo_lector.split("\n")

        lista_1=list()
        lista_dicc=list()
        

        for elemento in archivo_lector:
            archivo_lector=re.split("," , elemento.replace("$",""))
            lista_1.append(archivo_lector)

        for elemento in range(1,len(lista_1)):
            direccio=dict()
            direccio["ID"]=lista_1[elemento][0]
            direccio["NOMBRE"]=lista_1[elemento][1]
            direccio["MARCA"]=lista_1[elemento][2]
            direccio["PRECIO"]=float(lista_1[elemento][3])
            direccio["CARACTERISTICAS"]=lista_1[elemento][4]
            lista_dicc.append(direccio)
        print("Funcion cargada")
        return(lista_dicc)
    
def cantidad_marca(lista:list,key_m:str)->list:
    agrupacion_marca=list()
    lista_insumos=list()
    valor=0
    
    for marca in lista:
        if not (esta_en_lista(agrupacion_marca,marca[key_m])):
            agrupacion_marca.append(marca[key_m])

    for marca in agrupacion_marca:
        valor=0
        for nombre_insumo in lista: 
            diccionario_marcas=dict()
            if(marca == nombre_insumo[key_m]):
                valor+=1
            diccionario_marcas[marca] = valor
        lista_insumos.append(diccionario_marcas)
    return lista_insumos

def esta_en_lista (lista:list , marca:str)->list:
    esta=False
    for elemento in lista:
        if(elemento == marca):
            esta=True
            break
    return esta
            

def insumos_por_marca(lista:list , key_m:str,key_n:str,key_p:str)->list:
    agrupacion_marca=list()
    lista_insumos=list()
    valor=0
    for marca in lista:
        if not (esta_en_lista(agrupacion_marca,marca[key_m])):
            agrupacion_marca.append(marca[key_m])

    for marca in agrupacion_marca:
        valor=0
        for nombre_insumo in lista: 
            diccionario_marcas_2=dict()
            if(marca == nombre_insumo[key_m]):
                valor+=1
                andor= ":" , nombre_insumo[key_n] , " precio " , nombre_insumo[key_p]
            diccionario_marcas_2[marca]=andor
        lista_insumos.append(diccionario_marcas_2)
    return lista_insumos


#Buscar insumo por característica:
def busqueda_caracteristica(recorrer_caracteristica:list(),key_c:str,key_m:str)->None:
    lista=list()
    busqueda=input(" Buscar caracteristica  ")
    for caracteristica in recorrer_caracteristica:
            if busqueda in (caracteristica[key_c]):
                concatenado= "Marca : " +caracteristica[key_m] + "├ Caracteristica : " + caracteristica[key_c]
                lista.append(concatenado)
    if len(lista) == 0:
        print ("No existe")
    elif len(lista) > 0:
        for item in lista:
            print(item)

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
        print(f"{elemento[key_i]:2s}  {elemento[key_n]:35s}  {elemento[key_p]:10.0f} {elemento[key_m]:2s}")

def realizar_compras(lista:list):
    datos="///"
    while True:
        resultado=0
        marca_ingresada=input("Ingresar marca : , N para terminar :")
        if(marca_ingresada.lower() == "n"):
            break

        print("Productos de la marca")
        
        for producto in lista: 
            if(producto["MARCA"].lower() == marca_ingresada.lower()):
                print(f"->{producto['NOMBRE']}")

        eleccion=input("Elegir un pructo : ")
        for compra in lista:

            producto=compra["NOMBRE"]
            marca=compra["MARCA"]
            precio=compra["PRECIO"]


            if(eleccion.lower() in producto.lower()) :
                cantidad=int(input("Ingresar cantidad "))
                resultado += cantidad * precio
                datos=f"Producto :{eleccion}\n Marca :{marca}\n Precio :${precio}\n Cantidad :{cantidad}\n Precio Total :${resultado}"
                break
        archivo=open("precios.txt","w")
        archivo.write(datos)
        archivo.close()

    
def salir_funcion()->bool:
    opcion=input("desea salir del programa ? s/n ")
    while(opcion!="s" and opcion!="n"):
        opcion=input("error , s/n")
    if(opcion =="s"):
        print("Chao ♪♪♪ ")
        return False
    else :
        return True
    
        
