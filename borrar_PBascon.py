#Autor: Paco Bascón Valle
#Version 3.10.2
#Fecha 10/03/2022
#Definimos borrarnombre
#Buscamos un nombre en la agenda y si esta preguntamos que si queremos borrarlo


def borrarnombre_PBascon(nombre, agenda): 
        if nombre in agenda:
                opc = input("Pulsa 's' si quieres borrarlo!!!")
        if opc == "s":
                del agenda[nombre]

