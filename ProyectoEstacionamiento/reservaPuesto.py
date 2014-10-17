'''
Created on 15/10/2014

@author: Mugul
'''
bloquesDeTiempo = 24

def reservaPuesto(estacionamiento,tiempo,placa,dicPlacaPuesto):
    '''
        Revisa en la matriz si el tiempo solicitado por el vehiculo de placa <placa>
    esta disponible, y en caso afirmativo, lo reserva.
        Retorna la matriz actualizada, un booleano informando si se hizo la 
    reservacion, el puesto que se reservo y el diccionario PlacaPuesto actualizado
    Conductor: MS
    Navegante: GA
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
            estacionamiento[i][j] = -1
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