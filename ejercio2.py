from ClaseViajeroFrecuente import ViajeroFrecuente
from claseManejadorViajeros import Viajeros
    
if __name__=="__main__":
    lista=Viajeros()
    lista.inicializar()
    print(lista)
    numero=input("ingrese un numero de viajero frecuente")
    viajeroNuevo=lista.buscar(numero)
    opcion=0
    while opcion!=4:
       print("__MENU__")
       print("1-Comparar millas \n2-Acumular millas \n3- Canjear millas \n4- Salir menu")
       opcion=int(input("Ingrese la opcion que desea realizar"))
       if opcion==1:
           print(viajeroNuevo.getMillas())
           valor= input("ingrese un valor")
           i=(viajeroNuevo==valor)
           if i==True:
               print("Sobregarga por izquierda\nLas millas son iguales")
           else:
               print("Las millas no son iguales")
           d=(valor==viajeroNuevo)
           if d==True:
               print("Sobregarga por derecha\nLas millas son iguales")
           else:
               print("Las millas no son iguales")
       if opcion==2:
           valor=int(input("Ingrese la cantidad de millas a acumular"))
           valor+viajeroNuevo
           print("La cantidad de millas se actualizo a {}".format(viajeroNuevo.getMillas()))
       if opcion==3:
           valor=int(input("Ingrese la cantidad de millas a canjear"))
           valor-viajeroNuevo
           print("La cantidad de millas se actualizo a {}".format(viajeroNuevo.getMillas()))

            


    

    
    
    