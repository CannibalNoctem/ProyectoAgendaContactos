#Es una función que hace la función de listar el nombre y número de la agenda
#AUTOR: Emilio Pastor 
#FECHA: 4/03/2022
#HORA: 14:00
def listar_EPastor(agenda):
    for nombre, numero in agenda.items(): #Significa que nos da la información si está el nombre y número en la agenda
            print("--------------")
            print(nombre)#Nos da el nombre
            print("|| || || ||")
            print("\/ \/ \/ \/")
            print(numero)#Nos da el número del mismo
            print("--------------")