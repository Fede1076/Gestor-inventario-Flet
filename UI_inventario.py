# Importar las clases necesarias de Flet
from flet import *
from controls import add_to_control_reference

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
                        color="black",
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
            bgcolor="#081d33",
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

    # Método para agregar la instancia de 'AppForm' al diccionario de referencias a los controles
    def app_form_input_instance(self):
        add_to_control_reference("AppForm", self)

    # Método para crear un campo de entrada de formulario con un título y expansión específica
    def app_form_input_field(self, name:str, expand:int):
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

    # Método para construir la interfaz del formulario
    def build(self):
        self.app_form_input_instance()
        
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
                    # Título "Añadir producto"
                    Container(
                        padding=8,
                        content=Text(
                            value="Añadir producto", 
                            size=15,
                            color = 'black',
                            weight="bold"
                        )
                    ),
                    # Fila con campos de entrada para nombre del producto y cantidad
                    Row(
                        controls=[
                            self.app_form_input_field("Nombre del producto", 3),
                            self.app_form_input_field("Cantidad", 1),
                        ],
                    ),
                    # Fila con botón para agregar producto
                    Row(
                        alignment=MainAxisAlignment.END,
                        controls=[
                            ElevatedButton(text="Agregar producto", bgcolor="#081d33", color="white"),
                        ]
                    )
                ],
            ),
        )
    
# Definición de la clase AppProducts, que representa la visualización de productos en el inventario
class AppProducts(UserControl):
    def __init__(self):
        super().__init__()

    # Método para construir la interfaz de visualización de productos en el inventario
    def build(self):
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
                    # Títulos "Referencia", "Nombre" y "Cantidad"
                    Row(
                        controls=[
                            Container(
                                padding=8,
                                content=Text(
                                    value="Inventario", 
                                    size=15,
                                    color = 'black',
                                    weight="bold"
                                )
                            ),
                        ]
                    ),
                    Row(
                        controls=[
                            Text(value="Referencia", size=12, color="black", weight="bold"),
                            Text(value="Nombre", size=12, color="black", weight="bold"),
                            Text(value="Cantidad", size=12, color="black", weight="bold"),
                        ]
                    ),
                    # Aquí se mostrarían los productos del inventario con referencia, nombre y cantidad
                ],
            ),
        )