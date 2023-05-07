import csv
from ClaseViajeroFrecuente import ViajeroFrecuente
class Viajeros:
    __listaViajero=[]

    def __init__(self):
        self.__listaViajero=[]


    def agregar(self, unviajero):
         self.__listaViajero.append(unviajero)
    def inicializar(self):
        archivo=open("Viajeros.csv")
        reader= csv.reader(archivo,delimiter=",")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
    
            else:
                numero =fila[0]
                dni =fila[1]
                nom =fila[2]
                ape =fila[3]
                millas =int(fila[4])
                unViajero=ViajeroFrecuente(numero,dni,nom,ape,millas)
                #print(unViajero)
                self.agregar(unViajero)
        archivo.close()
    def __str__(self) :
        s=""
        for viajero in self.__listaViajero:
            s+=str(viajero)+"\n"

        return s


    def buscar(self,num):
        i=0
        viajeroNuevo=self.__listaViajero[0]
        numero=int(viajeroNuevo.getNumero())
        print(numero)
        #print(type(numero))
        #print(type(num))
        while ((i<(len(self.__listaViajero)-1))and(int(num)!=int(numero))):
            i+=1
            viajeroNuevo=self.__listaViajero[i]
            numero=int(viajeroNuevo.getNumero())
            print(numero)
        print(i)
        return self.__listaViajero[i]
    


    def Mayor (self):
        mayor=self.__listaViajero[0].getMillas()
        indice=0
        i=0
        for viajero in self.__listaViajero:
            millas=viajero.getMillas() 
            if int(millas)>int(mayor):
                mayor=millas
                indice=i
            i+=1
        #print("la cantidad de millas mayor es :{}".format(mayor))
        #print("el viajero con mayor cantidad de millas es {}".format(self.__listaViajero[indice].getDni()))
        return indice 
    
    def ViajerosConMayorMillas(self):
        millas=self.Mayor()
        for viajero in self.__listaViajero:
            if viajero>=self.__listaViajero[millas]:
                print("El viajero {} tiene la mayor cantidad de millas".format(viajero.getDni()))


    def AcumularMillas(self,i):
        viajero=self.__listaViajero[i]
        valor=int(input("Ingrese la cantidad de millas a acumular"))
        viajero+valor
        print("La cantidad de millas se actualizo a {}".format(viajero.getMillas()))

    def CanjearMillas(self,i):
        viajero=self.__listaViajero[i]
        valor=int(input("Ingrese la cantidad de millas a canjear"))
        viajero-valor
        print("La cantidad de millas se actualizo a {}".format(viajero.getMillas()))
