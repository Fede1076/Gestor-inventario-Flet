from flet import *
from mongo import connect

class login(UserControl):
    def __init__(self):
        super().__init__()

    def build(self):
        return Container(
            expand=True,
            height=190,
            bgcolor="white10",
            border=border.all(1, "#ebebeb"),
            border_radius=8,
            padding=15,
            content=Column(
                tf_user = TextField(hint_text="Nombre de usuario", label="Nombre de usuario", bgcolor= '#fdfdfd', color="black",),
                tf_password = TextField(hint_text="Contraseña", label="Contraseña", bgcolor= '#fdfdfd', color="black", password=True, can_reveal_password=True),
                submit = ElevatedButton(text="Acceder", bgcolor="#081d33"),)
            )
        