'''
Created on 15/10/2014

@author: Mugul
Conductor: GA
Navegante: MS
'''
import unittest
from reservaPuesto import *

matriz = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ]
x = dict()
tiempo = (1 , 2)
reservaPuesto(matriz,tiempo,"asdsad",x)

class TestReservaPuesto(unittest.TestCase):
    
    ##################################################################
    ######################     reservaPuesto    ######################
    ##################################################################
    def testReservaPuestoDicNoInicializado(self):
        self.assertEqual("El diccionario Placa-Puesto no existe",
                         reservaPuesto(matriz,tiempo,"123123",None),"Diccionario no existe" )
    
    def testReservaPuestoTiemposIncorrectos(self):
        tiempo = (-1 , 2)
        self.assertEqual("El tiempo reservado debe ser positivo y menor que 24",
                         reservaPuesto(matriz,tiempo,"123123",x),"Tiempo incorrecto" )
    
    def testReservaMatrizIncorrecta(self):
        matriz = [
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
          ]
        self.assertEqual("Matriz de dimension invalida, debe ser Nx%d"%bloquesDeTiempo,
                         reservaPuesto(matriz,tiempo,"123123",x),"Dimension de matriz incorrecta" )
        
    def testReservaPuestoPlacaNoInicializada(self):
        self.assertEqual("Placa debe ser un string",
                         reservaPuesto(matriz,tiempo,None,x),"Placa no esta creada" )
        
    def testReservaPuestoMatrizOcupada(self):
        matriz = [
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",x),"Estacionamiento ocupado" )
    
    def testReservaPuestoMatrizReservadaDesocupado(self):
        matriz = [
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",x),"Estacionamiento reservado desocupado" )
    
    def testReservaPuestoMatrizReservadaOcupada(self):
        matriz = [
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
          ]
        self.assertEqual("No hay puestos desocupados",
                         reservaPuesto(matriz,tiempo,"123123",x),"Estacionamiento reservado ocupado" )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
                
