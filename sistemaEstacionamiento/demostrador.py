'''
Created on 29/10/2014

@author: Mugul
'''
numOfParkings = 0

import re
reOwnerName = re.compile('( |[a-zA-Z])*$')
rePhoneCode = re.compile('0(212|4(1(2|4|6)|2(4|6)))$')
rePhoneNumber = re.compile('^[1-9][0-9][0-9][0-9][0-9][0-9][0-9]$')
reEmailAddress = re.compile('[a-zA-Z][_0-9a-zA-Z]*@[a-zA-Z]+(\.[a-zA-Z])+$')
reRif = re.compile('(j|J|v|V|e|E|g|G|p|P)-?[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]-?[0-9]$')

def askPhone():
    parkingPhoneCode = input("Por favor introduzca el codigo de area del telefono\n")
    while (rePhoneCode.match(parkingPhoneCode) == None):
        parkingPhoneCode = input("Introduzca un codigo de area valido (Por Ejemplo: 0212)\n")
#    print("parkingPhoneCode:",parkingPhoneCode,"\n")
    parkingPhone = input("Por favor introduzca el numero telefonico\n")
    while (rePhoneNumber.match(parkingPhone) == None):
        parkingPhone = input("Por favor introduzca un numero valido (Por Ejemplo: 9876543)\n")   
#    print("parkingPhone:",parkingPhone,"\n")
    return (parkingPhoneCode,parkingPhone)

def addParking():
    ownerName = input("Por favor introduzca el nombre del Duenho\n")
    while (reOwnerName.match(ownerName) == None):
        ownerName = input("Por favor introduzca un nombre valido (Solo letras)\n")
    #print("Nombre:",ownerName)
    parkingName = input("Por favor introduzca el nombre del Estacionamiento\n")
    #print("parkingName:",parkingName)
    parkingAddress = input("Por favor introduzca la direccion del Estacionamiento\n")
    #print("parkingAddress:",parkingAddress)
    phoneAux = askPhone()
    parkingPhoneCode1 = phoneAux[0]
    parkingPhone1 = phoneAux[1]
    if (input("Desea agregar otro telefono? (si/no)\n") == "si"):
        phoneAux = askPhone()
        parkingPhoneCode2 = phoneAux[0]
        parkingPhone2 = phoneAux[1]
        if (input("Desea agregar otro telefono? (si/no)\n") == "si"):
            phoneAux = askPhone()
            parkingPhoneCode3 = phoneAux[0]
            parkingPhone3 = phoneAux[1]
    parkingEmailAddr1 = input("Por favor introduzca el correo electronico\n")
    #print("Correo:",parkingEmailAddr1,"\n")
    while (reEmailAddress.match(parkingEmailAddr1) == None):
        parkingEmailAddr1 = input("Por favor introduzca un correo valido (Por ejemplo: nombre@dominio.ve\n")
    #print("parkingEmailAddr1:",parkingEmailAddr1)
    if (input("Desea agregar otro correo? (si/no)\n") == "si"):
        parkingEmailAddr2 = input("Por favor introduzca el correo electronico\n")
        while (reEmailAddress.match(parkingEmailAddr2) == None):
            parkingEmailAddr2 = input("Por favor introduzca un correo valido (Por ejemplo: nombre@dominio.ve\n")
    rif = input("Introduzca el numero de rif\n")
    while (reRif.match(rif) == None):
        rif = input("Introduzca un rif valido (Por ejemplo: J-31277937-3\n")
    #print("rif:",rif)
        
    numOfParkings += 1
    print ("Restan",5-numOfParkings,"espacios de estacionamiento")
    return (ownerName,parkingName,parkingAddress,parkingPhoneCode1,parkingPhone1,parkingPhoneCode2,parkingPhone2,
            parkingPhoneCode3,parkingPhone3,parkingEmailAddr1,parkingEmailAddr2,rif)

salir = "no"        
while ((numOfParkings < 6) or (salir == "si")):
    addParking()
    salir = input("Desea salir del programa? (si/no)")