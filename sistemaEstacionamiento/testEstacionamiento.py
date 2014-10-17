'''
Created on 16/10/2014

@author: Mugul
'''
import unittest
from estacionamiento import *

class Test(unittest.TestCase):
    
    ##################################################################
    ######################     reservaPuesto    ######################
    ##################################################################
    def testReservaPuestoDicNoInicializado(self):
        self.assertEqual("El diccionario Placa-Puesto no existe",
                         reservaPuesto(estacionamiento,tiempo,"123123",None),"Diccionario no existe" )
    
    def testReservaPuestoTiemposIncorrectos(self):
        tiempo = (-1 , 2)
        self.assertEqual("El tiempo reservado debe ser positivo y menor que 24",
                         reservaPuesto(estacionamiento,tiempo,"123123",placaPuesto),"Tiempo incorrecto" )
    
    def testReservaMatrizIncorrecta(self):
        matriz = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ]
        self.assertEqual("Matriz de dimension invalida, debe ser Nx%d"%bloquesDeTiempo,
                         reservaPuesto(matriz,tiempo,"123123",placaPuesto),"Dimension de matriz incorrecta" )
        
    def testReservaPuestoPlacaNoInicializada(self):
        self.assertEqual("Placa debe ser un string",
                         reservaPuesto(estacionamiento,tiempo,None,placaPuesto),"Placa no esta creada" )
        
    def testReservaPuestoMatrizOcupada(self):
        matriz = [
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",placaPuesto),"Estacionamiento ocupado" )
    
    def testReservaPuestoMatrizReservadaDesocupado(self):
        matriz = [
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",placaPuesto),"Estacionamiento reservado desocupado" )
    
    def testReservaPuestoMatrizReservadaOcupada(self):
        matriz = [
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",placaPuesto),"Estacionamiento reservado ocupado" )

    
    #######################################
    # En esta seccion se prueba la funcion#
    #        de tiempoACobrar.            #
    #######################################



    #Test de funcionamiento basico
    #Se verifica en matriz sencilla
    def testBasico(self):
        for i in range(3,6):
            estacionamiento[2][i] = 1
           
        placaPuesto["placa"]=2 
        
        salida = tiempoACobrar("placa",3,6,placaPuesto)
        print (salida)
    #Fallo al primer intento, return en posicion equivocada
    #Corrio bien al segundo intento
    #Conductor Francisco Martinez



    #Test de chequeo con matriz mas llena
    def testBasico2(self):
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        placaPuesto["placa"]=2 
        
        salida = tiempoACobrar("placa",3,6,placaPuesto)
        print (salida)
    #Corrio bien al primer intento
    #Conductor Francisco Martinez



    #Test de chequeo con multiples valores para la salida
    def testBasico3(self):
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        for i in range(7,9):
            estacionamiento[2][i] = 2

        for i in range(9,10):
            estacionamiento[2][i] = 3
        
        placaPuesto["placa"]=2 
    
        salida = tiempoACobrar("placa",3,10,placaPuesto)
        print (salida)
    #Corrio bien al primer intento
    #Conductor Francisco Martinez


    #Test para probar caso con placa erronea
    def testPlacaErronea(self):
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        for i in range(7,9):
            estacionamiento[2][i] = 2

        for i in range(9,10):
            estacionamiento[2][i] = 3
        
        placaPuesto["placa"]=2 
    
        salida = tiempoACobrar("placa2",3,10,placaPuesto)
        print (salida)
    #Fallo al primer intento, corregido con un try
    #Funciono bien al siguiente intento
    #Conductor Francisco Martinez



    #Probar darle un diccionario vacio
    def testDiccionarioVacio(self):
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        for i in range(7,9):
            estacionamiento[2][i] = 2

        for i in range(9,10):
            estacionamiento[2][i] = 3
        
        placaPuesto["placa"]=2 
    
        salida = tiempoACobrar("placa",3,10,None)
        print (salida)
    #Funciono bien al primer intento
    #Conductor Francisco Martinez




    #######################################
    # En esta seccion se prueba la funcion#
    #        de desocupar puesto.         #
    #######################################
    
    #Se probara enviar un Diccionario vacio
    def testDV(self) : 
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        for i in range(7,9):
            estacionamiento[2][i] = 2

        for i in range(9,10):
            estacionamiento[2][i] = 3
        
        placaPuesto["placa"]=2 
    
        desocuparPuesto("placa",10,None)
    #Funciono al primer intento
    


    #Caso Basico en el cual debe liberar el puesto del 
    #diccionario, y limpiar la matriz
    def testBasicoDesocupar(self) : 
        for i in range(3,7):
            estacionamiento[2][i] = 1
 
        for i in range(10,24):
            estacionamiento[2][i] = 1 
        
        placaPuesto["placa"]=2
        desocuparPuesto("placa",10,placaPuesto)
    #Lo hizo bien al primer intento.

    #Caso de malicia en el cual se libera desde el final 
    #diccionario, y limpiar la matriz
    def testBasicoDesocupar2(self) : 
        for i in range(3,7):
            estacionamiento[2][i] = 1
 
        for i in range(10,24):
            estacionamiento[2][i] = 1 
        
        placaPuesto["placa"]=2
       
        desocuparPuesto("placa",24,placaPuesto)
       
    #Lo hizo bien al primer intento.


    #Caso de malicia en el cual se libera desde el inicio 
    #diccionario, y limpiar la matriz
    def testBasicoDesocupar3(self) : 
        estacionamiento[2][0]=1
        for i in range(3,7):
            estacionamiento[2][i] = 1
 
        for i in range(10,24):
            estacionamiento[2][i] = 1 
        
        placaPuesto["placa"]=2
        print (estacionamiento)
        desocuparPuesto("placa",0,placaPuesto)
        print (estacionamiento)
    #Lo hizo bien al primer intento.
    #Funciono bien al primer intento.

    def testCuatroFunciones(self):
        tiempo = (1,2)
        placaPuesto["placa"] = 2
        reservaPuesto(estacionamiento,tiempo,"placa",placaPuesto)
        tiempoACobrar("placa",1,2,placaPuesto)
        desocuparPuesto("placa",2,placaPuesto)
        IntentarEstacionar("placa",1)
        print ("No hubo errores.")
         

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()