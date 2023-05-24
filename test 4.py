import re
with open(r"C:\Users\arell\Desktop\Consigna primer parcial\insumos.csv",encoding="utf-8")as file: 
    archivo_lector=file.read()
    archivo_lector=archivo_lector.split("\n")

    lista_1=list()
    lista_dicc=list()

    for elemento in archivo_lector:
        archivo_lector=re.split("," , elemento)
        lista_1.append(archivo_lector)

    for elemento in range(1,len(lista_1)):
        direccio=dict()
        direccio["ID"]=lista_1[elemento][0]
        direccio["NOMBRE"]=lista_1[elemento][1]
        direccio["MARCA"]=lista_1[elemento][2]
        direccio["PRECIO"]=lista_1[elemento][3]
        direccio["CARACTERISTICAS"]=lista_1[elemento][4]
        lista_dicc.append(direccio)
    # Realizar compras: Permite realizar compras de productos. El usuario 
    # ingresa una marca y se muestran todos los productos disponibles de 
    # esa marca. Luego, el usuario elige un producto y la cantidad deseada. 
    # Esta acción se repite hasta que el usuario decida finalizar la compra. 
    # Al finalizar, se muestra el total de la compra y se genera un archivo 
    # TXT con la factura de la compra, incluyendo cantidad, producto, 
    # subtotal y el total de la compra.

    for elemento in lista_dicc:
        print(elemento["MARCA"])

    #funcion
    print("------------------\nLista de productos\n------------------")
    lista_check=list()
    i=0
    for elemento in lista_dicc:
        print(elemento["MARCA"])

    flag_compra=False
    while True:
        marca_ingresada=input("Ingresar marca , para finalizar oprima 'N' :").lower()
        if(marca_ingresada.lower()=="n"):
            print("Compra finalizada")
            break
        else:
            print("----------\nProductos\n----------")
            for elemento in lista_dicc:
                if (marca_ingresada == elemento["MARCA"].lower()):
                    print(elemento["NOMBRE"])
                    lista_check.append(elemento["NOMBRE"])

        
            producto_elegido=input("Ingrese producto deseado : ").lower()
            for producto in lista_check: 
                if(producto_elegido == lista_check):
                        cantidad=int(input("Ingresar cantidad deseada :"))
                        resultado=cantidad*producto["PRECIO"]
                        print(f"{cantidad} , f{resultado}")
                        
            # else:
            #     print("Ingrese producto valido")

            
                