"""
    Proyecto Bimestral
    Segundo Bimestre
    
    Problemática:
"""


def main():
    pass
    print("Proceso inicial")
    bandera = True
    contador = 1
    while bandera:
        pass
        valor = int(
            input("• Ingrese 1 para crear una cuenta de Facebook\n• Ingrese 2 para crear una cuenta de Twitter\n"
                  "• Ingrese 3 para crear una cuenta de WhatsApp\n• Ingrese 4 para crear una cuenta de Telegram\n"
                  "• Ingrese 5 para crear una cuenta de Signal\n• Ingrese 6 para crear una cuenta de Instagram\n"
                  "• Ingrese 7 para crear una cuenta de Flickr\n"))

        if valor == 1:
            print(crearFacebook())
        else:
            if valor == 2:
                crearTwitter()
            else:
                if valor == 3:
                    print(crearWhatsapp())
                else:
                    if valor == 4:
                        crearTelegram()
                    else:
                        if valor == 5:
                            print(crearSignal())
                        else:
                            if valor == 6:
                                crearInstagram()
                            else:
                                if valor == 7:
                                    print(crearFlickr())
        n = str(input("Ingrese si para salir del proceso: "))
        if n == "si" or n == "Si":
            bandera = False
        else:
            bandera = True
            contador = contador + 1
    print(obtenerMensaje(contador))

def crearFacebook():
    """En este método se creará una cuenta de Facebook, donde se pedirá su nombre de usuario, edad, ciudad, pais y
    correo, lo cual al ser ingresado por el usuario se agregará a una cadena acumuladora para finalmente retornar
    ese valor a la funcion main en donde se presentará en pantalla"""
    cadena = "%s\n" % "Creando cuenta de Facebook"
    nombre = str(input("Ingrese su nombre de usuario: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = str(input("Ingrese su ciudad: "))
    pais = str(input("Ingrese su país: "))
    correo = str(input("Ingrese su correo: "))
    cadena = "%sNombre de usuario: %s\nEdad: %s\nCiudad: %s\nPaís: %s\nCorreo electrónico: %s\n\n" % (cadena,
                                                                                                      nombre, edad,
                                                                                                      ciudad,
                                                                                                      pais, correo)
    return cadena

def crearTwitter():
    """En este método se creará una cuenta de Twitter, donde se pedirá su nombre de usuario, nombres y apellidos,
    edad, ciudad, pais, idioma y correo, lo cual al ser ingresado por el usuario se agregará a una cadena acumuladora
    pero en este caso no se retornará ningún valor y se presentará en pantalla dentro del mismo procedimiento"""
    cadena = "%s\n" % "Creando cuenta de Twitter"
    nombre = str(input("Ingrese su nombre de usuario: "))
    nombres = str(input("Ingrese sus nombres: "))
    apellido = str(input("Ingrese sus apellidos: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = str(input("Ingrese su ciudad: "))
    pais = str(input("Ingrese su país: "))
    idioma = str(input("Ingrese el idioma: "))
    correo = str(input("Ingrese su correo: "))
    cadena = str("%sNombre de usuario: %s\nNombres: %s\nApellidos: %s\nEdad: %s\nCiudad: %s\nPaís: %s\nIdioma: %s\n"
                 "Correo electrónico: %s\n\n") % (cadena, nombre, nombres, apellido, edad, ciudad, pais, idioma, correo)
    print(cadena)

def crearWhatsapp():
    """En este método se creará una cuenta de Whatsapp, donde se pedirá su nombre de usuario, número de teléfono, edad,
    ciudad y país lo cual al ser ingresado por el usuario se agregará a una cadena acumuladora para finalmente retornar
        ese valor a la funcion main en donde se la mostrará en pantalla"""
    cadena = "%s\n" % "Creando cuenta de WhatsApp"
    nombre = str(input("Ingrese su nombre de usuario: "))
    cell = int(input("Ingrese su número de teléfono: "))
    edad = int(input("Ingrese su edad: "))
    ciudad = str(input("Ingrese su ciudad: "))
    pais = str(input("Ingrese su país: "))
    cadena = str("%sNombre de usuario: %s\nNúmero de teléfono: %d\nEdad: %s\nCiudad: %s\nPaís: %s\n\n") \
             % (cadena, nombre, cell, edad, ciudad, pais)
    return cadena

def crearTelegram():
    """En este método se creará una cuenta de Telegram, donde se pedirá su nombre de usuario, número de teléfono,
    ciudad, país y área de interes, lo cual al ser ingresado por el usuario se agregará a una cadena acumuladora que
     en este caso no retornará ningún valor y se presentará en pantalla directamente del mismo procedimiento"""
    cadena = "%s\n" % "Creando cuenta de Telegram"
    nombre = str(input("Ingrese su nombre de usuario: "))
    cell = int(input("Ingrese su número de teléfono: "))
    ciudad = str(input("Ingrese su ciudad: "))
    pais = str(input("Ingrese su país: "))
    interes = str(input("Ingrese su área de interés: "))
    cadena = str("%sNombre de usuario: %s\nNúmero de teléfono: %d\nCiudad: %s\nPaís: %s\nÁrea de interés: %s\n\n") \
             % (cadena, nombre, cell, ciudad, pais, interes)
    print(cadena)

def crearSignal():
    """En este método se creará una cuenta de Signal, donde se solicitará datos como su nombre de usuario, número de
    teléfono, ciudad, país y hobby principal, lo cual una vez sea ingresado por el usuario se añadirá a una cadena
    acumuladora para finalmente retornar dicho valor a la funcion main en donde se la mostrará en pantalla"""
    cadena = "%s\n" % "Creando cuenta de Signal"
    nombre = str(input("Ingrese su nombre de usuario: "))
    cell = int(input("Ingrese su número de teléfono: "))
    ciudad = str(input("Ingrese su ciudad: "))
    pais = str(input("Ingrese su país: "))
    hobby = str(input("Ingrese su hobbie favorito: "))
    cadena = str("%sNombre de usuario: %s\nNúmero de teléfono: %d\nCiudad: %s\nPaís: %s\nHobby principal: %s\n\n") \
             % (cadena, nombre, cell, ciudad, pais, hobby)
    return cadena

def crearInstagram():
    """En este método se creará una cuenta de Instagram, donde se pedirá su nombre de usuario, ciudad, edad y
    correo electrónico, lo cual al ser ingresado por el usuario se agregará a una cadena acumuladora que no retornará
    ningún valor y  presentará en pantalla desde el mismo procedimiento"""
    cadena = "%s\n" % "Creando cuenta de Instagram"
    nombre = str(input("Ingrese su nombre de usuario: "))
    ciudad = str(input("Ingrese su ciudad: "))
    edad = int(input("Ingrese su edad: "))
    correo = str(input("Ingrese su correo: "))
    cadena = str("%sNombre de usuario: %s\nCiudad: %s\nEdad: %d\nCorreo electrónico: %s\n\n") \
             % (cadena, nombre, ciudad, edad, correo)
    print(cadena)

def crearFlickr():
    """En este método se creará una cuenta de Flickr, donde se solicitará datos como su nombre de usuario y correo
    electrónico, lo cual una vez sea ingresado por el usuario se añadirá a una cadena acumuladora para finalmente
    retornar dicho valor a la funcion main donde será presentada en pantalla"""
    cadena = "%s\n" % "Creando cuenta de Flickr"
    nombre = str(input("Ingrese su nombre de usuario: "))
    correo = str(input("Ingrese su correo: "))
    cadena = "%sNombre de usuario: %s\nCorreo electrónico: %s\n\n" % (cadena, nombre, correo)
    return cadena

def obtenerMensaje(i):
    mensajeFinal = ["Campaña con poca afluencia", "Campaña moderada siga adelante", "Excelente campaña"]
    if 1 == i <= 5:
        return mensajeFinal[0]
    else:
        if 6 <= i <= 15:
            return mensajeFinal[1]
        else:
            if i >= 16:
                return mensajeFinal[2]


if __name__ == "__main__":
    main()
