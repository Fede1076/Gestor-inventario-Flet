from flet import *
from mongo import connect

def main(page: Page):

    page.bgcolor = "#ebebeb"
    page.padding = 20

    tf_user = TextField(hint_text="Nombre de usuario", label="Nombre de usuario", bgcolor= '#fdfdfd', color="black",)
    tf_password = TextField(hint_text="Contraseña", label="Contraseña", bgcolor= '#fdfdfd', color="black", password=True, can_reveal_password=True)
    submit = ElevatedButton(text="Acceder", bgcolor="#081d33")

    page.add(tf_user, tf_password, submit)
    page.update()
    connect()

app(target=main)