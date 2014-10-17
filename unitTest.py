'''
Created on Oct 15, 2014

@author: ricardo
'''
import unittest
from funciones import * 


class Test(unittest.TestCase):



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
        print salida
    #Fallo al primer intento, return en posicion equivocada
    #Corrio bien al segundo intento
    #Conductor Francisco Martinez



    #Test de chequeo con matriz mas llena
    def testBasico2(self):
        for i in range(3,7):
            estacionamiento[2][i] = 1
           
        placaPuesto["placa"]=2 
        
        salida = tiempoACobrar("placa",3,6,placaPuesto)
        print salida
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
        print salida
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
        print salida
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
        print salida
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
        print estacionamiento
        desocuparPuesto("placa",0,placaPuesto)
        print estacionamiento
    #Lo hizo bien al primer intento.
    #Funciono bien al primer intento.
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()


#test = Test()
# testBasico()
# testBasico2()
# testBasico3()
# testPlacaErronea()
# testDiccionarioVacio()
# testDV()
testBasicoDesocupar()
testBasicoDesocupar2()
testBasicoDesocupar3()
