import flet as ft
from flet import *
from form_login import login
from UI_inventario import AppHeader, AppForm, AppProducts

def main(page: ft.Page):
    page.bgcolor = '#fdfdfd'
    page.padding = 20
    page.add(
        Column(
            expand=True,
            controls=[
                AppHeader(),
                Divider(height= 2, color="transparent"),
                AppForm(),
                Divider(height= 2, color="transparent"),
                AppProducts()
                
            ],
        ),
    )
    page.update()
    pass