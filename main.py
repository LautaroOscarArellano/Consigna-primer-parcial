import os
from funciones import*
flag_1=False
flag_6=False
flag_7=False
menu=True
while menu == True:
    os.system("cls")
    match(mostar_menu()):
        case "1":
            datos_cargados=cargar_datos()
            flag_1=True
        case "2":
            if(flag_1==True):
                cantidad_marca(datos_cargados,"MARCA","CANTIDAD")
            else:
                print("Cargar datos primero")
        case "3":
            if(flag_1==True):
                insumos_por_marca(datos_cargados,"MARCA","NOMBRE","PRECIO")
            else:
                print("Cargar datos primero")
        case "4":
            if(flag_1==True):
                busqueda_caracteristica(datos_cargados,"CARACTERISTICAS","MARCA","STOCK")
            else:
                print("Cargar datos primero")      
        case "5":
            if(flag_1==True):
                orden_insumos(datos_cargados,"MARCA","NOMBRE","ID","PRECIO","STOCK")
            else:
                print("Cargar datos primero")  
        case "6":
            if(flag_1==True):
                guardado=realizar_compras(datos_cargados,"MARCA","PRECIO")
                flag_6=True
            else:
                print("Cargar datos primero")
        case "7":
            if(flag_6==True):
                guardado_json(guardado)
                flag_7=True
            else:
                print("Cargar funcion 6")
        case "8":
            if(flag_7==True):
                mostrar_json()
            else:
                print("Cargar funcion 7")
        case "9":
            if(flag_1==True):
                actualizacion_precios(datos_cargados)   
            else:
                print("Cargar datos primero")     
        case "10":
            agregar_productos()    
        case "11":
            if(flag_1==True):
                stock_por_marca(datos_cargados,"MARCA")
            else:
                print("Cargar datos primero")
        case "12":
            imprimir_bajo_stock(datos_cargados)
        case "13":
            menu=salir_funcion()
    os.system("pause")  











# case 10
# opcion=input("desea salir del programa ? s/n ")
# while(opcion!="s" and opcio!="n"):
#     opcion=input("error , S/n")
# if(opcion =="s"):
#     print("Chao ♪♪♪ ")
#     break        