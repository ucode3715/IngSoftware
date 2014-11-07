'''
Created on Oct 15, 2014

@author: Ricardo Vethencourt
         Francisco Martinez
         F.Miguel Saraiva
         Gabriel Alvarez
         Carlos Farinha
         Karla Alzuro
'''

estacionamiento = [[0 for i in range(24)] for x in range(5)]
placaPuesto = {}
bloquesDeTiempo = 24
tiempo = (1,2)

'''Navegante: Francisco
   Conductor: Ricardo'''
def tiempoACobrar(placa, tEntrada, tSalida, placaPuesto):
    
    try : 
        puesto = placaPuesto[placa]
    except:
        print ("Placa Erronea o Diccionario Vacio")
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
        print ("Placa Erronea, o Diccionario Vacio")
        return
    for i in range(tSalida,24):
        estacionamiento[puesto][i] = 0
    placaPuesto.pop(placa,None)
    pass

'''Navegante: Carlos Farinha
   Conductor: Karla Alzuro'''
def IntentarEstacionar(placa, HoraLlegada):
    hayPuesto = False
    for j in range(5):
        if estacionamiento[j][HoraLlegada]==0:
            placaPuesto = {placa:j}
            hayPuesto = True
            for n in range(24-HoraLlegada):
                estacionamiento[j][n]=1
    return(hayPuesto)

'''Navegante: Gabriel Alvarez
   Conductor: F.Miguel Saraiva'''
def reservaPuesto(estacionamiento,tiempo,placa,dicPlacaPuesto):
    '''
        Revisa en la matriz si el tiempo solicitado por el vehiculo de placa <placa>
    esta disponible, y en caso afirmativo, lo reserva.
        Retorna la matriz actualizada, un booleano informando si se hizo la 
    reservacion, el puesto que se reservo y el diccionario PlacaPuesto actualizado
    '''
    ## Verificaciones de datos erroneos
    i = 0
    if ((tiempo[0] >= tiempo[1]) or (tiempo[0] < 0) or (tiempo[1] > 24)):
        return "El tiempo reservado debe ser positivo y menor que 24"
    while i < len(estacionamiento):
        if len(estacionamiento[i]) != bloquesDeTiempo:
            print ("Matriz de dimension invalida, debe ser Nx%d"%bloquesDeTiempo)
            return "Matriz de dimension invalida, debe ser Nx%d"%bloquesDeTiempo
        i += 1
    if not placa:
        print ("Placa debe ser un string")
        return "Placa debe ser un string"
    if (dicPlacaPuesto == None):
        print ("El diccionario Placa-Puesto no existe")
        return "El diccionario Placa-Puesto no existe"
    
    i = 0   
    puestoEncontrado = False
    while i < len(estacionamiento):
        j = tiempo[0]
        while j < bloquesDeTiempo:
            if (estacionamiento[i][j] != 0):
                break
            j += 1
        if j == bloquesDeTiempo:
            dicPlacaPuesto[placa] = i
            puestoEncontrado = True
            break
        i += 1
    if puestoEncontrado:
        j = 0
        while j < tiempo[0]:
            estacionamiento[i][j] = 1
            j += 1
        while j < tiempo[1]:
            estacionamiento[i][j] = 2
            j += 1
        while j < bloquesDeTiempo:
            estacionamiento[i][j] = 1
            j += 1
        return (estacionamiento,puestoEncontrado,i,dicPlacaPuesto)
    else:
        return ("No hay puestos desocupados")


if __name__ == '__main__':
    pass