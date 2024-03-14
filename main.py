import flet as ft
from flet import *
from UI_login import UserWidget
from UI_inventario_admin import AppHeader, AppForm, AppDataTable

def main(page: ft.Page):
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        Column(
            UserWidget()
        ),
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
    pass

if __name__== "__main__":
    ft.app(target=main)