from tkinter import StringVar
from tkinter import IntVar
from tkinter import Frame
from tkinter import Entry
from tkinter import Label
from tkinter import Button
from modelo import Abmc
from tkinter import ttk
from tkinter.messagebox import *



class Ventanita():
    """
    Este es una clase destinada a ser la vista
    de la aplicación en donde se colocan
    todos los elementos gráficos para mostrar
    la información 
    """
    def __init__(self, window):
        """
        Este es el constructor de la clase Ventanita
        en donde se definen todos los atributos
        de esta clase y se configuran los distintos
        elementos gráficos
        """
        self.root = window
        self.nom = StringVar()
        self.ape = StringVar()
        self.tel = StringVar()
        self.buscarid = StringVar()
        self.a = IntVar()
        self.opcion = StringVar()
        self.f = Frame(self.root)
        self.tree = ttk.Treeview(self.f)
        self.objeto_base = Abmc()
        #Frame
        self.root.title("Agenda por José Emanuel Ruiz")
        self.f.config(width=1020, height=1020)
        self.f.grid(row=10, column=0, columnspan=4)

        #Etiquetas
        self.superior = Label(
            self.root, text="Ingrese sus datos", bg="orchid", fg="white", width=40
        )
        self.nombre = Label(self.root, text="Nombre")
        self.apellido = Label(self.root, text="Apellido")
        self.telefono = Label(self.root, text="Teléfono")
        self.telefono_hint = Label(self.root, text="*Este campo no puede repetirse en la agenda")
        
        

        self.superior.grid(
            row=0, column=0, columnspan=4, padx=1, pady=1, sticky="w" + "e"
        )
        self.nombre.grid(row=1, column=0, sticky="w")
        self.apellido.grid(row=2, column=0, sticky="w")
        self.telefono.grid(row=3, column=0, sticky="w")
        self.telefono_hint.grid(row=3, column=2, sticky="w")
        
        

        #Entradas
        self.Ent1 = Entry(self.root, textvariable=self.nom)
        self.Ent1.grid(row=1, column=1)
        self.Ent2 = Entry(self.root, textvariable=self.ape)
        self.Ent2.grid(row=2, column=1)
        self.Ent3 = Entry(self.root, textvariable=self.tel)
        self.Ent3.grid(row=3, column=1)
        self.Ent4 = Entry(self.root, textvariable=self.buscarid)
        self.Ent4.grid(row=1, column=3)


        #Botones
        self.boton_alta = Button(self.root, text="Alta", command=lambda: self.alta())
        self.boton_alta.grid(row=6, column=0)

        self.boton_editar = Button(self.root, text="Actualizar", command=lambda: self.modificar())
        self.boton_editar.grid(row=6, column=1)

        self.boton_borrar = Button(self.root, text="Borrar", command=lambda: self.borrar())
        self.boton_borrar.grid(row=6, column=2)

        self.boton_mostrar = Button(self.root, text="Mostrar", command=lambda: self.mostrar())
        self.boton_mostrar.grid(row=6, column=3)

        self.boton_buscar = Button(self.root, text="Buscar por ID", command=lambda: self.buscar_registro())
        self.boton_buscar.grid(row=2, column=3)

        #Tree
        self.tree["columns"] = ("col1", "col2", "col3")
        self.tree.column("#0", width=90, minwidth=50, anchor="w")
        self.tree.column("col1", width=200, minwidth=80)
        self.tree.column("col2", width=200, minwidth=80)
        self.tree.column("col3", width=200, minwidth=80)
        self.tree.heading("#0", text="ID")
        self.tree.heading("col1", text="Nombre")
        self.tree.heading("col2", text="Apellido")
        self.tree.heading("col3", text="Teléfono")
        self.tree.grid(row=10, column=0, columnspan=4)
        self.tree.bind('<ButtonRelease-1>', self.selectItem)

    def selectItem(
        
        self,a
    ):
        """
        Este método permite seleccionar un item del treeview
        para poder disponer de sus datos y realizar la operación de borrar
        un registro de la base de datos
        """
        curItem = self.tree.focus()
        diccionario=self.tree.item(curItem)
        self.Ent1.delete(0,'end')
        self.Ent1.insert(0,diccionario['values'][0])
        self.Ent2.delete(0,'end')
        self.Ent2.insert(0,diccionario['values'][1])
        self.Ent3.delete(0,'end')
        self.Ent3.insert(0,diccionario['values'][2])
        return diccionario['text']

    def selectItemUpdate(
        self,a
    ):
        """
        Este método permite seleccionar un item del treeview
        para poder disponer de sus datos y realizar la operación de actualizar
        un registro de la base de datos
        """
        curItem = self.tree.focus()
        diccionario=self.tree.item(curItem)
        
        return diccionario['text']  
        

    def alta(
        self,
    ):
        """
        Este método permite llamar a la rutina que registra datos en la base de datos
        """
        alta_result = self.objeto_base.alta(self.nom,self.ape,self.tel,self.tree)
        if alta_result!='alta_error':
            showinfo('Notificacion','Contacto añadido con éxito')
        else:
            showerror('Error', 'Los campos nombre y apellido no pueden contener numeros\ny el campo telefono no puede repetirse y debe tener\nal menos 7 cifras')
        
        

    def borrar(
        self,
    ):
        """
        Este método permite llamar a la rutina que borra registros de la base de datos
        """
        try:
            self.objeto_base.baja(self.selectItem(1),self.tree)
            showinfo('Notificacion','Contacto eliminado con éxito')
            
        except:
            showerror('Error', 'Debes seleccionar un item de la lista para poder eliminarlo')

    def modificar(
        self,
    ):
        """
        Este método permite llamar a la rutina que modifica un registro de la base de datos
        """
        modificacion_result = self.objeto_base.modificar(self.selectItemUpdate(1),self.tree,self.nom,self.ape,self.tel)
        if modificacion_result!='modificacion_error':
            showinfo('Notificacion','Contacto actualizado con éxito')
        else:
            showerror('Error', 'Los campos nombre y apellido no pueden contener numeros\ny el campo telefono debe tener al menos 7 cifras')
        
        

    def mostrar(
        self,
    ):
        """
        Este método permite llamar a la rutina que muestra el contenido actual de la base de datos
        """
        treeview_result = self.objeto_base.actualizar_treeview(self.tree)
        if treeview_result == []:
            showerror('Error', 'No hay datos para mostrar, por favor ingrese un registro')

        

    def buscar_registro(
        self,
    ):
        """
        Este método permite llamar a la rutina que busca un registro de la base de datos
        a partir de su ID
        """
        busqueda_result = self.objeto_base.buscar_registro(self.buscarid)
        if busqueda_result!='id_noexiste':
            if busqueda_result!='id_novalido':
                showinfo('Resultado de la busqueda', f'Nombre: {busqueda_result.nombre}\n\nApellido: {busqueda_result.apellido}\n\nTelefono: {busqueda_result.telefono}')
            else:
                showerror('Error','Ingrese un id valido')
        else:
            showerror('Error','El id no existe')


        
