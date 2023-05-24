import os
from funciones import*
menu=True
while menu == True:
    os.system("cls")
    match(mostar_menu()):
        case "1":
            datos_cargados=cargar_datos()
        case "2":
            insumos=cantidad_marca(datos_cargados,"MARCA")
            print(insumos)
        case "3":
            mensaje=insumos_por_marca(datos_cargados,"MARCA")
            print(mensaje)
        case "4":
            busqueda_caracteristica(datos_cargados)
        case "5":
            orden_insumos(datos_cargados)
        case "6":
            realizar_compras(datos_cargados)
        case "10":
            menu=salir_funcion()
    os.system("pause")  













# case 10
# opcion=input("desea salir del programa ? s/n ")
# while(opcion!="s" and opcio!="n"):
#     opcion=input("error , S/n")
# if(opcion =="s"):
#     print("Chao ♪♪♪ ")
#     break         