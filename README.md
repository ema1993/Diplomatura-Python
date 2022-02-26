# Diplomatura Python
Trabajo Final de la Diplomatura de Python de la UTN FRBA

**Aplicación de Agenda**

Esta aplicación permite almacenar contactos en una base de datos local mediante su
nombre, apellido y número de teléfono.

- Funcionamiento:

Mediante el botón Alta se hace el registro del contacto en la agenda a partir de la
creación de la base de datos (en caso que no exista), luego de la tabla (en caso que
no exista) y finalmente la inserción del registro en la tabla.

El botón Mostrar permite seleccionar todos los registros de la tabla y los
muestra en un treeview.

El botón Actualizar permite modificar el nombre, apellido y/o teléfono del
contacto seleccionado en el treeview.

El botón Borrar permite borrar el registro seleccionado desde el treeview.

El botón Buscar por ID permite realizar la búsqueda del registro a partir del ID
ingresado en el campo ID y muestra el resultado de dicha búsqueda en pantalla, el
cual puede ser una ventana que muestra el contacto buscado o una indicando id
inválido o que no se encontró el registro correspondiente a un cierto ID.

El uso de treeview combinado con la función “selectItem” facilita la recuperación del ID del
registro, necesario para realizar la actualización o eliminación de un cierto registro.

Si el alta y la eliminación del contacto resultan ejecutarse con éxito, generan cada una
un log indicando el contacto registrado o eliminado de la base de datos.

- **Vista previa de la app usando tkinter como interfaz gráfica**

![previa](https://user-images.githubusercontent.com/31832843/155847460-b2ee82ac-aca9-4d22-8a59-fdafebe44f88.png)

