import os
from funciones import*
flag_1=False
menu=True
while menu == True:
    os.system("cls")
    match(mostar_menu()):
        case "1":
            datos_cargados=cargar_datos()
        case "2":
            if(flag_1==True):
                insumos=cantidad_marca(datos_cargados,"MARCA")
                print(insumos)
        case "3":
            if(flag_1==True):
                mensaje=insumos_por_marca(datos_cargados,"MARCA","NOMBRE","PRECIO")
                print(mensaje)
        case "4":
            if(flag_1==True):
                busqueda_caracteristica(datos_cargados,"CARACTERISTICAS","MARCA")
        case "5":
            if(flag_1==True):
                orden_insumos(datos_cargados,"MARCA","NOMBRE","ID","PRECIO")
        case "6":
            if(flag_1==True):
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