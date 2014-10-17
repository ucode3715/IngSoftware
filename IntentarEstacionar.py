'''
Created on 15/10/2014

@author: karla, carlos
'''
estacionamiento = [[0 for i in range(24)] for x in range(5)]
placaPuesto = {}


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
                    
            

if __name__ == '__main__':
    pass
        