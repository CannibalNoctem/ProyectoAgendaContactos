#Función añadir o modificar.
#Se pide un nombre y un número.
#Se comprueba si está en la agenda, si es así se le da la opción a modificarlo.
#Sino está en la agenda se le pide un número de teléfono y un nombre para añadir el nuevo contacto a la agenda.
def agregarModificarAllamas (nombre,agenda):
    if nombre in agenda:
        print("%s ya existe su número de teléfono es %s" % (nombre,agenda[nombre]))
        opcion = input("Pulsa 's' si quieres modificarlo. Otra tecla para continuar.")
        if opcion == "s":
            numero = input("Dame el nuevo número de teléfono:")
            agenda[nombre]=numero
        else:
            numero = input("Dame el número de teléfono:")
            agenda[nombre]=numero