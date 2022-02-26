import re


class Validar:
    """
    Este clase está destinada a realizar la validación
    de datos mediante regex antes de crearlos o modificarlos en la base de datos
    """
    def __init__(
        self,
    ):
        print("validar")

    def regex_nombreyapellido(self, avalidar):
        """
        Este método permite validar los campos de 
        nombre y apellido
        """
        patron = re.compile(r'^[A-Za-z ]{2,}$')
        validar_nombreyapellido = re.match(patron, avalidar)
        return validar_nombreyapellido

    def regex_telefono(self, avalidar):
        """
        Este método permite validar el campo telefono
        """
        patron_tel = re.compile(r'^[0-9]{7,10}$')
        validar_telefono = re.match(patron_tel, avalidar)
        return validar_telefono

    def regex_id(self, avalidar):
        """
        Este método permite validar el campo ID
        """
        patron_id = re.compile(r'^[0-9]+$')
        validar_id = re.match(patron_id, avalidar)
        return validar_id