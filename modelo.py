from typing import Text
from validar import Validar
from peewee import *
from datetime import datetime


class Tema:
    """
    Esta clase cumple la función de recopilar y notificar sobre 
    determinados eventos que ocurran durante la ejecución de la
    aplicación
    """
    observadores = []

    def agregar(self, obj):
        """
        Este método agrega el evento observado a la lista observadores
        """
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self):
        """
        Este método permite ejecutar alguna acción posterior a la
        ejecución del evento observado
        """
        for observador in self.observadores:
            observador.update()


class ConcreteObserverA():
    """
    Esta clase observa la ejecución de determinado evento
    y realiza una tarea a partir de esa acción 
    """
    def __init__(self, obj):
        """
        Este es el constructor de la clase ConcreteObserverA
        en donde se hace el llamado al metodo agregar para
        adicionar el evento observado a la lista observadores
        """
        self.observador_a = obj
        self.observador_a.agregar(self)

    def update(self):
        """
        Este método realiza un registro de log a partir de la
        eliminacion de un contacto de la agenda
        """
        self.estado_id = self.observador_a.get_estado()
        resultado = Agenda.get_by_id(self.estado_id)
        file = open(datetime.now().strftime("Baja_"+"%Y%m%d-%H%M%S")+".txt", "w")
        file.write("Se eliminó el contacto\n")
        file.write("Nombre: " + resultado.nombre + "\n")
        file.write("Apellido: " + resultado.apellido + "\n")
        file.write("Telefono: " + resultado.telefono + "\n")
        file.write("Fecha: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
        file.close()
 

db = SqliteDatabase('nivel_avanzado.db')

class BaseModel(Model):
    class Meta:
        database = db

class Agenda(BaseModel):
    """
    En esta clase se definen las variables de la base de datos
    """
    nombre = CharField()
    apellido = CharField()
    telefono = TextField(unique = True)
db.connect()
db.create_tables([Agenda])

def decorador_alta(funcion):
    """
    Este método realiza un registro de log posterior a la adición
    de un contacto en la agenda
    """
    def envoltura(*arg, **kargs): 
        
        if funcion(*arg, **kargs)!='alta_error':

            file = open(datetime.now().strftime("Alta_"+"%Y%m%d-%H%M%S")+".txt", "w")
            
            file.write("Se registró el contacto\n")
            file.write("Nombre: " + arg[1].get() + "\n")
            file.write("Apellido: " + arg[2].get() + "\n")
            file.write("Telefono: " + arg[3].get() + "\n")
            file.write("Fecha: " + datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))
            file.close()       

        else:
            return 'alta_error'

    return envoltura

class Abmc(Tema):
    """
    Esta clase está destinada a ser el modelo de la aplicación en donde
    se llevará a cabo la lógica de la aplicación
    """
    def __init__(
        self,
    ):
        """
        Este es el constructor de la clase Abmc
        en donde se definen todos los atributos
        de esta clase
        """
        self.validacion = Validar()
        self.estado = None
        
    def set_estado(self, value):
        """
        Este método tomar el valor del id eliminado de la agenda y notifica
        sobre la ejecución del evento observado
        """
        self.estado = value
        self.notificar()

    def get_estado(self):
        """
        Este método permite obtener el valor del id eliminado de la agenda
        """
        return self.estado

    def actualizar_treeview(self, mitreeview):
        """
        Este método permite actualizar el treeview luego de realizar alguna
        operacion en la base de datos
        """
        #limpieza de tabla 
        records = mitreeview.get_children()
        for element in records:
            mitreeview.delete(element)

        for valor_recuperado in Agenda.select():
            mitreeview.insert('', 0, text = valor_recuperado.id, values = (valor_recuperado.nombre, valor_recuperado.apellido, valor_recuperado.telefono),tags = ('odd',))

    @decorador_alta
    def alta(self, nombre, apellido, telefono, mitreeview):
        """
        Este método permite registrar datos en la base de datos
        """
        print("alta")
        validar_nombre = self.validacion.regex_nombreyapellido(nombre.get())
        validar_apellido = self.validacion.regex_nombreyapellido(apellido.get())
        validar_tel = self.validacion.regex_telefono(telefono.get())
        if validar_nombre!=None and validar_apellido!=None and validar_tel!=None:

            agenda = Agenda()
            agenda.nombre = nombre.get()
            agenda.apellido = apellido.get()
            agenda.telefono = telefono.get()
            try:
                agenda.save()
                self.actualizar_treeview(mitreeview)
            
                return 'alta_ok'
            except:
                return 'alta_error'

            
        else:
            return 'alta_error'

    def baja(
        self,elid,mitreeview
    ):
        """
        Este método permite borrar registros de la base de datos
        """  
        print("baja")
        esteeselid = elid

        borrar = Agenda.get(Agenda.id == esteeselid)

        ConcreteObserverA(self)
        self.set_estado(esteeselid)

        borrar.delete_instance()

        self.actualizar_treeview(mitreeview)
        

    def modificar(
        self,elid,mitreeview,nombre,apellido,telefono
    ):
        """
        Este método permite modificar un registro de la base de datos
        """
        print("modificar")
        validar_nombre = self.validacion.regex_nombreyapellido(nombre.get())
        validar_apellido = self.validacion.regex_nombreyapellido(apellido.get())
        validar_tel = self.validacion.regex_telefono(telefono.get())
        if validar_nombre!=None and validar_apellido!=None and validar_tel!=None:
            esteeselid = elid

            actualizar = Agenda.update(nombre=nombre.get(), apellido=apellido.get(), telefono=telefono.get()).where(
                Agenda.id == esteeselid
            )
            actualizar.execute()


            self.actualizar_treeview(mitreeview)
            return 'modificacion_ok'
        else:
            return 'modificacion_error'
       

    def buscar_registro(self,buscarid):
        """
        Este método permite buscar un registro de la base de datos
        a partir de su ID
        """
    
    
        validar_id = self.validacion.regex_id(buscarid.get())
        
    
        if validar_id!=None:

            try:
                resultado = Agenda.get_by_id(buscarid.get())
                return resultado

            except:
                return 'id_noexiste'

        else:
            return 'id_novalido'

    

    