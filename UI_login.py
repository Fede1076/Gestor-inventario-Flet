import flet as ft
from flet import *
from pymongo import MongoClient

# Conexión a la base de datos MongoDB
client = MongoClient('mongodb://localhost:27017/')
#Seleccionar una base de datos y la colección
bd = client ["GestorInventarioDB"]
coleccion = bd ["Usuarios"]

# Definición de la clase UserWidget, que representa un widget de usuario
class UserWidget(UserControl):
    def __init__(
            self, 
            title:str,
            sub_title:str,
            input_text:str,
            password_text:str,
            btn_name:str,
    ):
        # Llama al constructor de la superclase
        super().__init__()
        # Inicializa los atributos de la clase
        self._title = title
        self._sub_title = sub_title
        self._input_text = input_text
        self._password_text = password_text
        self.btn_name = btn_name

    # Método para crear un campo de entrada de texto
    def InputTextField(self):
        return Container(
            alignment=alignment.center,
            content=ft.TextField(
                height=40,
                width=255,
                bgcolor='#f0f3f6',
                color="black",
                hint_text=self._input_text,
                hint_style=TextStyle(
                    size=14,
                    color="black",
                )
            ),
        )

    # Método para crear un campo de entrada de contraseña
    def InputPasswordField(self):
        return Container(
            alignment=alignment.center,
            content=ft.TextField(
                height=40,
                width=255,
                bgcolor='#f0f3f6',
                color="black",
                hint_text=self._password_text,  
                cursor_color="black",
                password=True, 
                can_reveal_password=True,  # Para ocultar el texto ingresado
                hint_style=TextStyle(
                    size=14,
                    color="black",
                ),
            ),
        )
    
    # Método para crear un botón de inicio de sesión
    def SignIn(self):
        return ElevatedButton(
            on_click=self.SignInClick,  # Ahora estamos pasando la función, no llamándola
            content=Text(
                self.btn_name,
                size=11,
                weight="bold",
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
            height=38,
            width=255,
            data=True  # Esto pasará los datos del formulario al evento
        )
    
    # Método para construir la interfaz del widget
    def build(self):
        # Contenedor para el título
        title_container = Container(
            alignment=alignment.center,
            content=Text(
                self._title,
                size=18,
                text_align="center",
                weight="bold",
                color="black",
            ),
        )

        # Contenedor para el sub título
        sub_title_container = Container(
            alignment=alignment.center,
            content=Text(
                self._sub_title,
                size=14,
                text_align="center",
                color="black",
            )
        )

        # Crear campos de entrada de texto y contraseña
        input_field = self.InputTextField()
        password_field = self.InputPasswordField()

        self._sign_in = Container(
            content=self.SignIn()
        )

        
        # Construir la estructura de la interfaz del widget
        return Column(
            horizontal_alignment='center',
            controls=[
                Container(padding=10),
                title_container,
                sub_title_container, 
                Divider(height= 2, color="transparent"), 
                input_field,
                password_field,
                Container(padding=5),
                self._sign_in,
            ]
        )

    # Método para manejar el evento de clic en el botón de "Acceder"
    def SignInClick(self, event):
        # Obtener el usuario ingresado y la contraseña ingresada directamente de los campos de texto y contraseña
        usuario = self._input_text
        contrasena = self._password_text

        # Verificar si el usuario y la contraseña existen en la base de datos MongoDB
        user_data = coleccion.find_one({"usuario": usuario, "contrasena": contrasena})
        
        if user_data:
            # Si se encuentra el usuario y la contraseña, mostrar un mensaje de éxito
            print("Inicio de sesión exitoso")
        else:
            # Mostrar mensaje de error si el usuario no existe o la contraseña es incorrecta
            print("Usuario o contraseña incorrectos")


# Función principal para iniciar la aplicación
def main(page: ft.Page):
    # Configuración de la página
    page.title = "Login"
    page.bgcolor = "#f0f3f6"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"

    # Función para crear la columna principal
    def _main_column_():
        return Container(
            width=400, 
            height=400, 
            bgcolor="#ffffff",
            padding=12,
            border_radius=35,
            border=border.all(3, "#ebebeb"),
            content=Column(
                expand=True,
                spacing=20,
                horizontal_alignment="center",
            ),
        )
    
    # Crear instancia de UserWidget con los parámetros necesarios
    _sign_in_ = UserWidget(
        title="Bienvenido",
        sub_title="Ingrese con su nombre de usuario",
        input_text="Usuario", # Agrega el texto del campo de entrada
        password_text="Contraseña",
        btn_name="Acceder",
    )

    # Construir la interfaz principal
    _sign_in_main = _main_column_()
    _sign_in_main.content.controls.append(Container(padding=15))
    _sign_in_main.content.controls.append(_sign_in_)

    # Añadir la interfaz principal a la página
    page.add(
        Row(
            alignment='center',
            spacing=25,
            controls=[
                _sign_in_main,
            ]
        )
    )

if __name__== "__main__":
    ft.app(target=main)