#Esta programa fue creado el martes 8 de marzo de 2022
#Este es el programa de Jaime Serrano Maya y definimos y ponemos en acción la opción buscar dentro de la agenda
def buscar_JSerrano(nombre, agenda):    #Definimos la operación de buscar y sus variables, nombre y agenda
    for nombre, numtel in agenda.items(): 
        if nombre.startswith(cadena):
            print("El número de teléfono de %s es el %s" % (nombre, agenda [nombre]))   #Mostramos la frase con el % que es definido en la misma línea como nombre y número