# Importar las clases necesarias de Flet
import flet as ft
from flet import *
import os
import csv
from controls import add_to_control_reference, return_control_reference
import pymongo as pm

#conexion a la base de datos
#establecer la cvonexion con el servidor
cliente =pm.MongoClient("mongodb://localhost:27017/")

#Seleccionar una base de datos y la colección
bd = cliente ["GestorInventarioDB"]
coleccion = bd ["Inventario"]

# Definición de la clase AppHeader, que representa el encabezado de la aplicación
class AppHeader(UserControl):
    def __init__(self):
        super().__init__()

    # Método para agregar la instancia de 'AppHeader' al diccionario de referencias a los controles
    def app_header_instance(self):
        add_to_control_reference("AppHeader", self)

    # Método para crear el área de la marca del encabezado
    def app_header_brand(self):
        return Container(
            content=Text(
                "Inventario",
                size=15
            )
        )
    
    # Método para crear la barra de búsqueda del encabezado
    def app_header_search(self):
        return Container(
            width=320,
            bgcolor='white10',
            border_radius=6,
            opacity=0,
            animate_opacity=0,
            padding=8,
            content=Row(
                spacing=10,
                vertical_alignment=CrossAxisAlignment.CENTER,
                controls=[
                    Icon(
                        name=icons.SEARCH_ROUNDED,
                        size=17,
                        opacity=0.85
                    ),
                    TextField(
                        border_color="transparent",
                        height=20,
                        text_size=14,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="white",
                        hint_text="Buscar",
                    )
                ],
            ),
        )
    
    # Método para crear el avatar del usuario en el encabezado
    def app_header_avatar(self):
        return Container(content=IconButton(icons.PERSON))

    # Método para mostrar o ocultar la barra de búsqueda según el evento recibido
    def show_search_bar(self, e):
        if e.data == 'true':
            self.controls[0].content.controls[1].opacity = 1
            self.controls[0].content.controls[1].update()
        else:
            self.controls[0].content.controls[1].content.controls[1].value = ""
            self.controls[0].content.controls[1].opacity = 0
            self.controls[0].content.controls[1].update()

    # Método para construir la interfaz del encabezado
    def build(self):
        self.app_header_instance()

        return Container(
            expand=True,
            on_hover=lambda e: self.show_search_bar(e),
            height=60,
            bgcolor=ft.colors.BLUE_900,
            border_radius=6,
            padding=padding.only(left=15, right=15),
            content=Row(
                expand=True,
                alignment=MainAxisAlignment.SPACE_BETWEEN, 
                controls=[
                    self.app_header_brand(),
                    self.app_header_search(),
                    self.app_header_avatar(),
                ],
            ),
        )

# Definición de la clase AppForm, que representa el formulario para añadir productos al inventario
class AppForm(UserControl):
    def __init__(self):
        super().__init__()

    def app_form_input_instance(self):
        # Agrega la instancia de AppForm al diccionario de referencias de controles
        add_to_control_reference("AppForm", self)

    def app_form_input_field(self, name:str, expand:int):
        # Crea un campo de entrada de formulario con un título y expansión específica
        return Container(
            expand=expand,
            height=60,
            bgcolor="#ebebeb",
            border_radius=6,
            padding=8,
            content=Column(
                spacing=1,
                controls=[
                    Text(
                        value=name, size=12, color="black", weight="bold"
                    ),
                    TextField(
                        border_color="transparent",
                        height=29,
                        text_size=13,
                        content_padding=0,
                        cursor_color="black",
                        cursor_width=1,
                        cursor_height=18,
                        color="black",
                    )
                ],
            ),
        )

    def build(self):
        # Agrega la instancia de AppForm al diccionario de referencias de controles
        self.app_form_input_instance()
        
        # Campos de entrada de texto para nombre del producto y cantidad
        self.nombre_producto_field = TextField(hint_text="Nombre del producto")
        self.cantidad_field = TextField(hint_text="Cantidad")

        # Construye la interfaz del formulario
        return Container(
            expand=True,
            height=190,
            bgcolor="white10",
            border=border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                expand=True,
                controls=[
                    Container(
                        padding=8,
                        content=Text(
                            value="Añadir al inventario", 
                            size=15,
                            color='black',
                            weight="bold"
                        )
                    ),
                    Row(
                        controls=[
                            self.app_form_input_field("Nombre del producto", 3),
                            self.app_form_input_field("Cantidad", 1),
                        ],
                    ),
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            return_form_button()
                        ]
                    )
                ],
            ),
        )
    
def add_to_db(self, e):
        # Obtiene el valor de los campos de entrada de texto
        nombre_producto = self.nombre_producto_field.value
        cantidad = self.cantidad_field.value

        # Inserta el producto en la base de datos
        nuevo_producto = {
            "nombre": nombre_producto,
            "cantidad": cantidad
        }
        coleccion.insert_one(nuevo_producto)


# Función para devolver un botón de formulario
def return_form_button():
    return Container(
        alignment=alignment.center,
        content=ElevatedButton(
            # Define la acción al hacer clic en el botón
            on_click= add_to_db,
            # Configuración de colores y estilos del botón
            bgcolor=ft.colors.BLUE_900,
            color="white",
            content=Row(
                controls=[
                    # Icono para agregar un campo de entrada a la tabla
                    Icon(
                        name=icons.ADD_ROUNDED,
                        size=12,
                    ),
                    # Texto del botón
                    Text(
                        "Añadir producto",
                        size=11,
                        weight="bold",
                    ),
                ],
            ),
            style=ButtonStyle(
                # Estilo de la forma del botón: borde redondeado
                shape={
                    "": RoundedRectangleBorder(radius=8),
                },
                # Color del texto del botón
                color={
                    "": "white",
                },
            ),
            height=42,
            width=170,
        ),
    )
    
class AppDataTable(UserControl):
    def __init__(self):
        super().__init__()

    def app_data_table_instance(self):
        # Agrega la instancia de AppDataTable al diccionario de referencias de controles
        add_to_control_reference("AppDataTable", self)

    def build(self):
        # Construye la interfaz de visualización de productos en el inventario
        self.app_data_table_instance()
        return Row(
            expand=True,
            controls=[
                DataTable(
                    expand=True,
                    border_radius=8,
                    border=border.all(2, "#ebebeb"),
                    horizontal_lines=border.BorderSide(1, "#ebebeb"),
                    columns=[
                        DataColumn(
                            Text("Producto", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Cantidad total", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Cantidad Bod.", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Cantidad Excib.", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Precio Uni.", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Precio Caja", size=12, color='black', weight='bold')
                        ),
                        DataColumn(
                            Text("Editar", size=12, color='black', weight='bold')
                        ),
                    ],
                    rows=[]
                )
            ],
        )
    
def main(page: ft.Page):
    # Configuración de la página principal
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.navigation_bar = ft.NavigationBar(
        height=70,
        bgcolor=ft.colors.BLUE_900,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.INVENTORY,
                label="Inventario",
            ),
            ft.NavigationDestination(icon=ft.icons.SUPERVISED_USER_CIRCLE, label="Clientes"),
            ft.NavigationDestination(icon=ft.icons.SUPERVISED_USER_CIRCLE_OUTLINED, label="Usuarios"),
            ft.NavigationDestination(icon=ft.icons.REQUEST_PAGE_ROUNDED, label="Facturas"),
        ]
    )
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height= 2, color="transparent"),
                AppForm(),
                Divider(height= 2, color="transparent"),
                Column(
                    scroll='hidden',
                    expand=True,
                    controls=[
                        AppDataTable()
                    ]
                )
                
            ],
        ),
    )
    page.update()


if __name__== "__main__":
    ft.app(target=main)