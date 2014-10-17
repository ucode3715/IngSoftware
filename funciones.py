'''
Created on Oct 15, 2014

@author: Ricardo Vethencourt
         Francisco Martinez
'''
estacionamiento = [[0 for i in range(24)] for x in range(5)]
placaPuesto = {}


'''Navegante: Francisco
   Conductor: Ricardo'''
def tiempoACobrar(placa, tEntrada, tSalida, placaPuesto):
    
    try : 
        puesto = placaPuesto[placa]
    except:
        print "Placa Erronea o Diccionario Vacio"
        return 
    ocupado, rOcupado, rNoOcupado = 0, 0, 0
    for i in range(tEntrada, tSalida):
        bloque = estacionamiento[puesto][i]
        if bloque == 1:
            ocupado += 1
        elif bloque == 3:
            rOcupado += 1
        elif bloque == 2:
            rNoOcupado += 1
    return (rNoOcupado, rOcupado, ocupado)

'''Navegante: Ricardo
   Conductor: Francisco'''
def desocuparPuesto(placa,tSalida,placaPuesto):
    try :
        puesto = placaPuesto[placa]
    except:
        print "Placa Erronea, o Diccionario Vacio"
        return
    for i in range(tSalida,24):
        estacionamiento[puesto][i] = 0
    placaPuesto.pop(placa,None)
    pass



if __name__ == '__main__':
    pass
